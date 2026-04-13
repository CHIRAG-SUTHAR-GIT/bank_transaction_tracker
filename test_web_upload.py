"""Test upload through web interface"""
import requests
import time
import sqlite3

print("Testing web upload...\n")

# Upload file
print("1. Uploading LAYERS.xlsx through web interface...")
with open('LAYERS.xlsx', 'rb') as f:
    files = {'file': f}
    response = requests.post('http://localhost:5000/upload', files=files)
    result = response.json()
    print(f"   {result['message']}")

time.sleep(1)

# Check database
conn = sqlite3.connect('transactions.db')
cursor = conn.cursor()

print("\n2. Checking database contents...")
cursor.execute('SELECT DISTINCT sheet_name FROM other_transactions')
sheets = [row[0] for row in cursor.fetchall()]
print(f"   Sheets in database: {len(sheets)}")
for sheet in sheets:
    cursor.execute('SELECT COUNT(*), SUM(amount) FROM other_transactions WHERE sheet_name = ?', (sheet,))
    count, total = cursor.fetchone()
    print(f"     - {sheet}: {count} entries, ₹{total:,.2f}")

# Check a specific transaction
print("\n3. Checking transaction 530378689613...")
cursor.execute('SELECT sheet_name, amount FROM other_transactions WHERE transaction_id = ?', ('530378689613',))
results = cursor.fetchall()
if results:
    print(f"   Found {len(results)} entries:")
    for sheet, amount in results:
        print(f"     - {sheet}: ₹{amount:,.2f}")
else:
    print("   No entries found")

conn.close()

print("\n4. Expected sheets from LAYERS.xlsx:")
print("   - Withdrawal through ATM")
print("   - Transaction put on hold")
print("   - Others Less Then 500")

if len(sheets) == 3 and 'Layered_Transaction_Report' not in sheets:
    print("\n✅ SUCCESS! Only correct sheets are in database")
else:
    print(f"\n❌ ISSUE! Found {len(sheets)} sheets, expected 3")
    if 'Layered_Transaction_Report' in sheets:
        print("   ⚠️ 'Layered_Transaction_Report' should not be there!")
