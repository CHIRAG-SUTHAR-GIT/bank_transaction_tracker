import requests
import pandas as pd
import time

print("Testing new Excel features...")

# Upload file
print("\n1. Uploading file...")
with open('uploads/current.xlsx', 'rb') as f:
    r = requests.post('http://localhost:5000/upload', files={'file': f})
    print(f"   {r.json()['message']}")

time.sleep(2)

# Download report
print("\n2. Downloading report...")
r = requests.get('http://localhost:5000/download-report')
with open('Test_Excel_Features.xlsx', 'wb') as f:
    f.write(r.content)
print(f"   Downloaded: {len(r.content):,} bytes")

# Check columns
print("\n3. Checking columns...")
df = pd.read_excel('Test_Excel_Features.xlsx')
print(f"   Total columns: {len(df.columns)}")
print(f"   First 5 columns:")
for i, col in enumerate(df.columns[:5]):
    print(f"     {i+1}. {col}")

if 'Parent Trans ID (Filter)' in df.columns:
    print("\n✅ SUCCESS! New column added")
    print(f"   Column position: {df.columns.tolist().index('Parent Trans ID (Filter)') + 1}")
else:
    print("\n❌ Column not found. Columns are:")
    for i, col in enumerate(df.columns):
        print(f"     {i+1}. {col}")

print("\n4. Checking Excel features...")
print("   Open 'Test_Excel_Features.xlsx' in Excel to see:")
print("   - Collapsible groups (click [-] and [+] on left)")
print("   - Filter dropdowns (click ▼ in headers)")
print("   - Outline levels (click 1, 2, 3 at top left)")
