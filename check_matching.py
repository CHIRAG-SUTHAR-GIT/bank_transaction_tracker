import sqlite3

conn = sqlite3.connect('transactions.db')
cursor = conn.cursor()

# Get all child transaction IDs from Money Transfer
cursor.execute('SELECT DISTINCT child_transaction_id FROM transactions')
money_transfer_ids = set(row[0] for row in cursor.fetchall())

print(f'Total unique transaction IDs in Money Transfer: {len(money_transfer_ids)}')
print('Sample IDs:', list(money_transfer_ids)[:5])

# Get all transaction IDs from other sheets
cursor.execute('SELECT DISTINCT transaction_id FROM other_transactions')
other_sheets_ids = set(row[0] for row in cursor.fetchall())

print(f'\nTotal unique transaction IDs in other sheets: {len(other_sheets_ids)}')
print('Sample IDs:', list(other_sheets_ids)[:5])

# Find matches
matches = money_transfer_ids.intersection(other_sheets_ids)
print(f'\nMatching transaction IDs: {len(matches)}')

if matches:
    print('\nMatching IDs:')
    for trans_id in list(matches)[:10]:
        print(f'  {trans_id}')
        
        # Show breakdown
        cursor.execute('SELECT sheet_name, amount FROM other_transactions WHERE transaction_id = ?', (trans_id,))
        for sheet, amount in cursor.fetchall():
            print(f'    - {sheet}: ₹{amount:,.2f}')

conn.close()
