"""Test the new direct pandas app"""
import requests
import time

print("Testing new pandas-based app (no SQL)...\n")

time.sleep(2)

# Upload file
print("1. Uploading LAYERS.xlsx...")
with open('LAYERS.xlsx', 'rb') as f:
    files = {'file': f}
    response = requests.post('http://localhost:5000/upload', files=files)
    result = response.json()
    print(f"   {result['message']}")

time.sleep(1)

# Get Layer 1 transactions
print("\n2. Getting Layer 1 transactions...")
response = requests.get('http://localhost:5000/api/transactions?layer=1')
transactions = response.json()
print(f"   Found {len(transactions)} transactions")

if transactions:
    trans = transactions[0]
    print(f"\n3. First transaction details:")
    print(f"   Child Trans ID: {trans['child_transaction_id']}")
    print(f"   Disputed: ₹{trans['disputed_amount']:,.2f}")
    print(f"   updated: ₹{trans['updated_amount']:,.2f}")
    print(f"   Status: {trans['status']}")
    
    # Get breakdown
    print(f"\n4. Getting breakdown for {trans['child_transaction_id']}...")
    response = requests.get(f"http://localhost:5000/api/transaction-details/{trans['child_transaction_id']}")
    details = response.json()
    print(f"   Found {len(details)} entries:")
    for detail in details:
        print(f"     - {detail['sheet']}: ₹{detail['amount']:,.2f}")
    
    # Check for phantom data
    sheets_found = set(detail['sheet'] for detail in details)
    expected_sheets = {'Withdrawal through ATM', 'Transaction put on hold', 'Others Less Then 500'}
    
    print(f"\n5. Verification:")
    print(f"   Expected sheets: {expected_sheets}")
    print(f"   Found sheets: {sheets_found}")
    
    if 'Layered_Transaction_Report' in sheets_found:
        print("   ❌ PHANTOM DATA FOUND: Layered_Transaction_Report")
    else:
        print("   ✅ NO PHANTOM DATA!")

# Download report
print("\n6. Downloading report...")
response = requests.get('http://localhost:5000/download-report')
if response.status_code == 200:
    with open('Direct_App_Report.xlsx', 'wb') as f:
        f.write(response.content)
    print(f"   ✅ Downloaded: {len(response.content):,} bytes")
    
    import pandas as pd
    df = pd.read_excel('Direct_App_Report.xlsx', sheet_name='Hierarchical Report')
    
    # Check breakdown column
    print(f"\n7. Checking breakdown column in Excel...")
    sample_breakdowns = df['Breakdown by Sheet'].dropna().head(5)
    for idx, breakdown in enumerate(sample_breakdowns):
        if breakdown != 'None':
            print(f"   Transaction {idx+1}: {breakdown[:100]}...")
            if 'Layered_Transaction_Report' in breakdown:
                print("     ❌ PHANTOM DATA IN EXCEL!")
else:
    print(f"   ❌ Download failed: {response.status_code}")
