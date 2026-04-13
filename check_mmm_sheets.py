import pandas as pd
import sys

if len(sys.argv) < 2:
    print("Usage: python check_mmm_sheets.py <filepath>")
    sys.exit(1)

filepath = sys.argv[1]

try:
    xl = pd.ExcelFile(filepath)
    print(f"\nFile: {filepath}")
    print(f"Total sheets: {len(xl.sheet_names)}\n")
    
    for idx, sheet in enumerate(xl.sheet_names):
        print(f"{idx + 1}. {sheet}")
        if 'money transfer' in sheet.lower():
            print(f"   ✓ This is the Money Transfer sheet!")
    
    print("\nSearching for 'money transfer' in sheet names...")
    found = False
    for sheet in xl.sheet_names:
        if 'money transfer' in sheet.lower():
            print(f"✓ Found: '{sheet}'")
            found = True
    
    if not found:
        print("✗ No sheet with 'money transfer' in name found!")
        
except Exception as e:
    print(f"Error: {e}")
