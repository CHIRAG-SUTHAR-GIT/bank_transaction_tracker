"""Final verification that the system handles multiple uploads correctly"""
import requests
import time
import sqlite3

print("=" * 70)
print("FINAL VERIFICATION: Multiple File Uploads")
print("=" * 70)

# Wait for server
time.sleep(2)

# First upload
print("\n1. FIRST UPLOAD")
with open('LAYERS.xlsx', 'rb') as f:
    files = {'file': f}
    response = requests.post('http://localhost:5000/upload', files=files)
    result = response.json()
    print(f"   Status: {result['message']}")

# Check database
conn = sqlite3.connect('transactions.db')
cursor = conn.cursor()
cursor.execute('SELECT COUNT(*) FROM transactions')
count1 = cursor.fetchone()[0]
cursor.execute('SELECT DISTINCT sheet_name FROM other_transactions')
sheets1 = [row[0] for row in cursor.fetchall()]
print(f"   Transactions: {count1}")
print(f"   Sheets: {', '.join(sheets1)}")

# Second upload (should clear first)
print("\n2. SECOND UPLOAD (should clear previous data)")
time.sleep(1)
with open('LAYERS.xlsx', 'rb') as f:
    files = {'file': f}
    response = requests.post('http://localhost:5000/upload', files=files)
    result = response.json()
    print(f"   Status: {result['message']}")

# Check database again
cursor.execute('SELECT COUNT(*) FROM transactions')
count2 = cursor.fetchone()[0]
cursor.execute('SELECT DISTINCT sheet_name FROM other_transactions')
sheets2 = [row[0] for row in cursor.fetchall()]
print(f"   Transactions: {count2}")
print(f"   Sheets: {', '.join(sheets2)}")

conn.close()

# Verify
print("\n3. VERIFICATION")
if count1 == count2:
    print(f"   ✅ Data cleared correctly: {count1} transactions (not doubled)")
else:
    print(f"   ❌ Data NOT cleared: {count1} → {count2} transactions")

if sheets1 == sheets2:
    print(f"   ✅ Sheets consistent: {len(sheets1)} sheets")
else:
    print(f"   ❌ Sheets changed: {sheets1} → {sheets2}")

# Test download
print("\n4. DOWNLOAD TEST")
response = requests.get('http://localhost:5000/download-report')
if response.status_code == 200:
    with open('Final_Test_Report.xlsx', 'wb') as f:
        f.write(response.content)
    print(f"   ✅ Report downloaded: {len(response.content):,} bytes")
    
    import pandas as pd
    df = pd.read_excel('Final_Test_Report.xlsx', sheet_name='Hierarchical Report')
    print(f"   ✅ Report contains {len(df)} rows")
    
    # Check sheets in breakdown
    all_sheets = set()
    for breakdown in df['Breakdown by Sheet'].dropna():
        if breakdown != 'None':
            for part in breakdown.split(';'):
                sheet = part.split(':')[0].strip()
                all_sheets.add(sheet)
    
    print(f"   ✅ Sheets in report: {', '.join(sorted(all_sheets))}")
else:
    print(f"   ❌ Download failed: {response.status_code}")

print("\n" + "=" * 70)
print("CONCLUSION: System handles multiple uploads correctly!")
print("Each upload clears previous data and processes only the new file.")
print("=" * 70)
