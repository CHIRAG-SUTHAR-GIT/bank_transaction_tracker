import sqlite3

conn = sqlite3.connect('transactions.db')
cursor = conn.cursor()

# Check all sheets
cursor.execute('SELECT DISTINCT sheet_name FROM other_transactions')
print('All sheets in database:')
for row in cursor.fetchall():
    print(f'  - {row[0]}')

# Check a specific transaction
trans_id = '109061067970'
cursor.execute('SELECT sheet_name, amount FROM other_transactions WHERE transaction_id = ?', (trans_id,))
results = cursor.fetchall()

print(f'\nTransaction {trans_id} breakdown:')
if results:
    total = 0
    for sheet, amount in results:
        print(f'  {sheet}: ₹{amount:,.2f}')
        total += amount
    print(f'  TOTAL: ₹{total:,.2f}')
else:
    print('  No entries found')

# Check another transaction
trans_id2 = 'IN12602720384346'
cursor.execute('SELECT sheet_name, amount FROM other_transactions WHERE transaction_id = ?', (trans_id2,))
results2 = cursor.fetchall()

print(f'\nTransaction {trans_id2} breakdown:')
if results2:
    total = 0
    for sheet, amount in results2:
        print(f'  {sheet}: ₹{amount:,.2f}')
        total += amount
    print(f'  TOTAL: ₹{total:,.2f}')
else:
    print('  No entries found')

# Count entries per sheet
print('\nEntries per sheet:')
cursor.execute('SELECT sheet_name, COUNT(*), SUM(amount) FROM other_transactions GROUP BY sheet_name')
for sheet, count, total in cursor.fetchall():
    print(f'  {sheet}: {count} entries, ₹{total:,.2f}')

conn.close()
