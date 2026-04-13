"""Test both download options"""
import requests
import pandas as pd
import time

print("Testing both download options...\n")

time.sleep(2)

# Test 1: Hierarchical Report
print("1. Testing Hierarchical Report...")
r1 = requests.get('http://localhost:5000/download-report')
if r1.status_code == 200:
    with open('Test_Hierarchical.xlsx', 'wb') as f:
        f.write(r1.content)
    df1 = pd.read_excel('Test_Hierarchical.xlsx')
    print(f"   ✅ Downloaded: {len(r1.content):,} bytes")
    print(f"   ✅ Total transactions: {len(df1)}")
    print(f"   ✅ Transactions with children: {len(df1[df1['Has Children'] == 'Yes'])}")
    print(f"   ✅ Leaf nodes (no children): {len(df1[df1['Has Children'] == 'No'])}")
else:
    print(f"   ❌ Failed: {r1.status_code}")

# Test 2: Leaf Nodes Report
print("\n2. Testing Leaf Nodes Report...")
r2 = requests.get('http://localhost:5000/download-leaf-nodes')
if r2.status_code == 200:
    with open('Test_LeafNodes.xlsx', 'wb') as f:
        f.write(r2.content)
    df2 = pd.read_excel('Test_LeafNodes.xlsx')
    print(f"   ✅ Downloaded: {len(r2.content):,} bytes")
    print(f"   ✅ Total leaf nodes: {len(df2)}")
    print(f"   ✅ All have no children: {(df2['Has Children'] == 'No').all()}")
    
    # Status breakdown
    print(f"\n   Status Breakdown:")
    for status in ['PENDING', 'PARTIAL', 'COMPLETE']:
        count = len(df2[df2['Status'] == status])
        if count > 0:
            print(f"     - {status}: {count} transactions")
else:
    print(f"   ❌ Failed: {r2.status_code}")

print("\n3. Comparison:")
print(f"   Hierarchical Report: {len(df1)} total transactions")
print(f"   Leaf Nodes Report: {len(df2)} final transactions")
print(f"   Difference: {len(df1) - len(df2)} intermediate transactions")

print("\n✅ Both download options are working!")
print("\nIn your browser, you'll see:")
print("   📥 Download Hierarchical Excel Report (blue button)")
print("   📄 Download Leaf Nodes Only (orange button)")
