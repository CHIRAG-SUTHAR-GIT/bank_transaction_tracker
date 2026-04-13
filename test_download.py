   """Test the download functionality"""
import requests
import time

# Wait for server to start
time.sleep(3)

print("Testing download functionality...")

# First upload the file
print("\n1. Uploading file...")
with open('LAYERS.xlsx', 'rb') as f:
    files = {'file': f}
    response = requests.post('http://localhost:5000/upload', files=files)
    result = response.json()
    print(f"   Upload: {result['message']}")

# Test download
print("\n2. Downloading hierarchical report...")
response = requests.get('http://localhost:5000/download-report')

if response.status_code == 200:
    # Save the file
    filename = 'Test_Transaction_Report.xlsx'
    with open(filename, 'wb') as f:
        f.write(response.content)
    print(f"   ✅ Report downloaded successfully: {filename}")
    print(f"   File size: {len(response.content):,} bytes")
    
    # Verify the Excel file
    import pandas as pd
    xl = pd.ExcelFile(filename)
    print(f"\n3. Verifying Excel file...")
    print(f"   Sheets: {xl.sheet_names}")
    
    df = pd.read_excel(filename, sheet_name='Hierarchical Report')
    print(f"   Total rows: {len(df)}")
    print(f"   Columns: {list(df.columns)}")
    
    print(f"\n4. Sample data (first 3 rows):")
    print(df[['Level', 'Layer', 'Parent Account', 'Child Account', 'Disputed Amount', 'Status']].head(3).to_string())
    
    # Check summary sheet
    df_summary = pd.read_excel(filename, sheet_name='Summary')
    print(f"\n5. Summary Sheet:")
    print(df_summary.to_string())
    
    print("\n✅ Download feature working perfectly!")
else:
    print(f"   ❌ Error: {response.status_code}")
    print(f"   {response.text}")
