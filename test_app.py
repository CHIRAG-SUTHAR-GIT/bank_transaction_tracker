"""Test script to verify the application works with LAYERS.xlsx"""
import requests
import time

# Wait for server to start
time.sleep(2)

# Test file upload
print("Testing file upload...")
with open('LAYERS.xlsx', 'rb') as f:
    files = {'file': f}
    response = requests.post('http://localhost:5000/upload', files=files)
    result = response.json()
    print(f"Upload result: {result}")

# Test getting Layer 1 transactions
print("\nFetching Layer 1 transactions...")
response = requests.get('http://localhost:5000/api/transactions?layer=1')
transactions = response.json()
print(f"Found {len(transactions)} Layer 1 transactions")

if transactions:
    print("\nFirst transaction:")
    trans = transactions[0]
    print(f"  Parent Account: {trans['parent_account']}")
    print(f"  Child Account: {trans['child_account']}")
    print(f"  Bank: {trans['bank']}")
    print(f"  Child Trans ID: {trans['child_transaction_id']}")
    print(f"  Disputed Amount: ₹{trans['disputed_amount']}")
    print(f"  updated: ₹{trans['updated_amount']}")
    print(f"  Pending: ₹{trans['pending_amount']}")
    print(f"  Status: {trans['status']}")
    print(f"  Has Children: {trans['has_children']}")
    
    # Test getting child transactions
    if trans['has_children']:
        print(f"\nFetching child transactions for {trans['child_transaction_id']}...")
        response = requests.get(f"http://localhost:5000/api/transactions?layer=2&parent_id={trans['child_transaction_id']}")
        children = response.json()
        print(f"Found {len(children)} child transactions")
    
    # Test transaction details
    print(f"\nFetching details for transaction {trans['child_transaction_id']}...")
    response = requests.get(f"http://localhost:5000/api/transaction-details/{trans['child_transaction_id']}")
    details = response.json()
    print(f"Found {len(details)} entries in other sheets")
    for detail in details:
        print(f"  - {detail['sheet']}: ₹{detail['amount']}")

print("\n✅ Test completed! Open http://localhost:5000 in your browser")
