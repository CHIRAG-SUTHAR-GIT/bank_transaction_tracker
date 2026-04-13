"""Test that uploading a new file clears old data"""
from app import init_database, process_excel_file
import sqlite3

print("Testing data clearing on new upload...\n")

# Initialize
init_database()

# First upload
print("1. First upload of LAYERS.xlsx")
success, msg = process_excel_file('LAYERS.xlsx')
print(f"   {msg}")

# Check data
conn = sqlite3.connect('transactions.db')
cursor = conn.cursor()
cursor.execute('SELECT COUNT(*) FROM transactions')
count1 = cursor.fetchone()[0]
cursor.execute('SELECT COUNT(*) FROM other_transactions')
other_count1 = cursor.fetchone()[0]
print(f"   Transactions: {count1}")
print(f"   Other sheets: {other_count1}")

# Second upload (should clear first)
print("\n2. Second upload of LAYERS.xlsx (should clear previous data)")
success, msg = process_excel_file('LAYERS.xlsx')
print(f"   {msg}")

# Check data again
cursor.execute('SELECT COUNT(*) FROM transactions')
count2 = cursor.fetchone()[0]
cursor.execute('SELECT COUNT(*) FROM other_transactions')
other_count2 = cursor.fetchone()[0]
print(f"   Transactions: {count2}")
print(f"   Other sheets: {other_count2}")

conn.close()

# Verify counts are the same (not doubled)
if count1 == count2 and other_count1 == other_count2:
    print("\n✅ SUCCESS! Data is cleared before each upload")
    print(f"   Data not duplicated: {count1} transactions each time")
else:
    print("\n❌ FAILED! Data was not cleared")
    print(f"   First upload: {count1} transactions")
    print(f"   Second upload: {count2} transactions (should be same)")
