import os
import tempfile
import unittest
from io import BytesIO

import pandas as pd

import app_account
import batch_account_summaries
from summary_database import connect_database, initialize_database


MAIN_COLUMNS = [
    'Serial',
    'Acknowledgement No.',
    'Debited Account No.',
    'Debited Transaction ID',
    'Bank Name',
    'Layer',
    'Credited Account No.',
    'IFSC',
    'Transaction Date',
    'Credited Transaction ID',
    'Transaction Amount',
    'Disputed Amount',
    'Reference',
    'Remarks',
    'Debited Bank Name',
    'Reported Date',
    'Unused',
]


def main_rows():
    return [
        [
            1, 'ACK-1', '00001111', 'DEBIT-1', 'Credit Bank', 1,
            '00009999', 'IFSC-1', '2026-08-20', 'CREDIT-X', 2500, 2500,
            'REF-1', 'first', 'Debit Bank', '2026-08-20', '',
        ],
        [
            2, 'ACK-1', '00001111', 'DEBIT-2', 'Changed Bank', 2,
            '00009999', 'IFSC-2', '2026-08-21', 'CREDIT-X', 7777, 7777,
            'REF-2', 'later duplicate credit', 'Debit Bank', '2026-08-21', '',
        ],
    ]


def other_sheet_rows(amount):
    return [
        [1, 'x', '00009999', 'CREDIT-X', 'x', amount],
        [2, 'x', '00009999', 'CREDIT-X', 'x', amount],
    ]


class CreditOnlyDuplicateTests(unittest.TestCase):
    def setUp(self):
        app_account.df_main = None
        app_account.df_other_sheets = {}
        app_account.uploaded_files_count = 0
        app_account.last_duplicate_transaction_details = []
        app_account.rebuild_maps()

    def tearDown(self):
        app_account.df_main = None
        app_account.df_other_sheets = {}
        app_account.uploaded_files_count = 0
        app_account.last_duplicate_transaction_details = []
        app_account.rebuild_maps()

    def load_workbook(self):
        handle = tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False)
        workbook_path = handle.name
        handle.close()
        try:
            with pd.ExcelWriter(workbook_path, engine='openpyxl') as writer:
                pd.DataFrame(main_rows(), columns=MAIN_COLUMNS).to_excel(
                    writer, sheet_name='Money Transfer', index=False
                )
                pd.DataFrame(
                    other_sheet_rows(400),
                    columns=['No', 'Info', 'Account', 'TID', 'Info 2', 'Amount'],
                ).to_excel(writer, sheet_name='Recovery', index=False)
                pd.DataFrame(
                    other_sheet_rows(1),
                    columns=['No', 'Info', 'Account', 'TID', 'Info 2', 'Amount'],
                ).to_excel(
                    writer, sheet_name='Others Less Than 500', index=False
                )

            success, message = app_account.process_excel_file(
                workbook_path, is_first_file=True
            )
            self.assertTrue(success, message)
        finally:
            os.unlink(workbook_path)

    def test_only_credited_total_uses_duplicate_identity(self):
        self.load_workbook()

        self.assertEqual(len(app_account.df_main), 2)
        credit_rows, excluded_count = app_account.credited_rows_for_totals(
            app_account.df_main
        )
        self.assertEqual(excluded_count, 1)
        self.assertEqual(len(credit_rows), 1)
        self.assertEqual(float(credit_rows.iloc[0, 11]), 2500)

        # Equal-value rows from other sheets are all counted. The same physical
        # row found via TID and account lookup is still returned only once.
        breakdown = app_account.get_transaction_breakdown(
            'CREDIT-X', '00009999'
        )
        self.assertEqual(len(breakdown), 4)
        self.assertEqual(sum(item['amount'] for item in breakdown), 1800)

        client = app_account.app.test_client()
        account_api = client.get('/api/all-transactions').get_json()
        credited = next(
            row for row in account_api if str(row['account_number']).endswith('9999')
        )
        debited = next(
            row for row in account_api if str(row['account_number']).endswith('1111')
        )
        self.assertEqual(credited['total_credited'], 2500)
        self.assertEqual(credited['updated_amount'], 1800)
        self.assertEqual(debited['total_debited'], 10277)

        transaction_api = client.get('/api/all-transactions-by-id').get_json()
        transaction = next(
            row for row in transaction_api
            if row['credited_transaction_id'] == 'CREDIT-X'
        )
        self.assertEqual(transaction['total_credited'], 2500)
        self.assertEqual(transaction['updated_amount'], 1800)
        self.assertIn(
            'Debit and other-sheet matching remain counted.',
            transaction['duplicate_entry_info'],
        )

    def test_downloads_and_overnight_route_use_same_rule(self):
        self.load_workbook()
        client = app_account.app.test_client()

        account_response = client.get('/download-account-summary')
        self.assertEqual(account_response.status_code, 200)
        account_summary = pd.read_excel(
            BytesIO(account_response.data), sheet_name='Account Wise Summary'
        )
        credited = account_summary.loc[
            account_summary['Total Credited Amount'] == 2500
        ].iloc[0]
        debited = account_summary.loc[
            account_summary['Total Debited Amount'] == 10277
        ].iloc[0]
        self.assertEqual(float(credited['Updated Amount (Recovery)']), 1800)
        self.assertIn(
            'Debit and other-sheet matching remain counted.',
            credited['Duplicate Entry Info'],
        )
        self.assertTrue(
            pd.isna(debited['Duplicate Entry Info'])
            or debited['Duplicate Entry Info'] == 'None'
        )

        transaction_response = client.get('/download-transaction-id-summary')
        self.assertEqual(transaction_response.status_code, 200)
        transaction_summary = pd.read_excel(
            BytesIO(transaction_response.data),
            sheet_name='Transaction ID Wise Summary',
        )
        transaction = transaction_summary.loc[
            transaction_summary['Credited Transaction ID'] == 'CREDIT-X'
        ].iloc[0]
        self.assertEqual(float(transaction['Total Credited Amount']), 2500)
        self.assertEqual(float(transaction['Updated Amount (Recovery)']), 1800)

    def test_overnight_database_is_requeued_once_for_logic_upgrade(self):
        with tempfile.TemporaryDirectory() as directory:
            database_path = initialize_database(
                os.path.join(directory, 'account_summaries.sqlite')
            )
            connection = connect_database(database_path)
            try:
                with connection:
                    connection.execute(
                        """
                        INSERT INTO source_files (
                            source_path, file_name, file_size, mtime_ns,
                            fingerprint, status, discovered_at, last_seen_at
                        ) VALUES (?, ?, 1, 1, '1:1', 'completed', ?, ?)
                        """,
                        ('C:/input/test.xlsx', 'test.xlsx', 'now', 'now'),
                    )
            finally:
                connection.close()

            self.assertEqual(
                batch_account_summaries.requeue_for_summary_logic_upgrade(
                    database_path
                ),
                1,
            )
            connection = connect_database(database_path)
            try:
                status = connection.execute(
                    "SELECT status FROM source_files"
                ).fetchone()['status']
                version = connection.execute(
                    "SELECT value FROM schema_metadata WHERE key = ?",
                    ('account_summary_logic_version',),
                ).fetchone()['value']
                with connection:
                    connection.execute(
                        "UPDATE source_files SET status = 'completed'"
                    )
            finally:
                connection.close()
            self.assertEqual(status, 'pending')
            self.assertEqual(
                version, batch_account_summaries.SUMMARY_LOGIC_VERSION
            )

            self.assertEqual(
                batch_account_summaries.requeue_for_summary_logic_upgrade(
                    database_path
                ),
                0,
            )
            connection = connect_database(database_path)
            try:
                status = connection.execute(
                    "SELECT status FROM source_files"
                ).fetchone()['status']
            finally:
                connection.close()
            self.assertEqual(status, 'completed')

    def test_all_matching_cheque_rows_are_added_even_when_amounts_repeat(self):
        handle = tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False)
        workbook_path = handle.name
        handle.close()
        cheque_amounts = [50000, 49000, 50000, 50000, 50000, 50000]
        cheque_columns = [
            'S No.', 'Acknowledgement No.', 'Account No.',
            'Transaction Id / UTR Number', 'Account No 2', 'IFSC Code',
            'Cheque No', 'Withdrawal Date & Time', 'Withdrawal Amount',
            'Disputed Amount', 'Branch Location',
        ]
        cheque_rows = [
            [
                index, '31108260194533', '0057041000000564',
                'ICICR42026081900511569', f'account-{index}', 'JAKA0FATTEH',
                f'9302{index}', '', amount, amount, 'FATEH KADAL SRINAGAR',
            ]
            for index, amount in enumerate(cheque_amounts, start=1)
        ]
        source_row = main_rows()[0]
        source_row[1] = '31108260194533'
        source_row[6] = '57041000000564'
        source_row[9] = 'ICICR42026081900511569'
        source_row[10] = 300000
        source_row[11] = 300000

        try:
            with pd.ExcelWriter(workbook_path, engine='openpyxl') as writer:
                pd.DataFrame([source_row], columns=MAIN_COLUMNS).to_excel(
                    writer, sheet_name='Money Transfer', index=False
                )
                pd.DataFrame(cheque_rows, columns=cheque_columns).to_excel(
                    writer, sheet_name='Cash Withdrawal through Cheque',
                    index=False,
                )

            success, message = app_account.process_excel_file(
                workbook_path, is_first_file=True
            )
            self.assertTrue(success, message)
        finally:
            os.unlink(workbook_path)

        breakdown = app_account.get_transaction_breakdown(
            'ICICR42026081900511569'
        )
        self.assertEqual(len(breakdown), 6)
        self.assertEqual(sum(item['amount'] for item in breakdown), 299000)

        rows = app_account.app.test_client().get(
            '/api/all-transactions'
        ).get_json()
        account = next(
            row for row in rows
            if str(row['account_number']).endswith('0564')
        )
        self.assertEqual(account['total_credited'], 300000)
        self.assertEqual(account['updated_amount'], 299000)
        self.assertIn(
            'Cash Withdrawal through Cheque: ₹299,000.00',
            account['breakdown_by_sheet'],
        )


if __name__ == '__main__':
    unittest.main()
