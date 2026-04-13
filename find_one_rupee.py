"""Find where the 1 rupee entry is coming from"""
import pandas as pd

xl = pd.ExcelFile('LAYERS.xlsx')

trans_id = '530378689613'

print(f"Searching for transaction {trans_id} in all sheets...\n")

for sheet in xl.sheet_names:
    print(f"=== {sheet} ===")
    df = pd.read_excel('LAYERS.xlsx', sheet_name=sheet)
    
    # Check column 3 (index 3) for transaction ID
    if len(df.columns) > 3:
        matches = df[df.iloc[:, 3].astype(str) == trans_id]
        
        if len(matches) > 0:
            print(f"Found {len(matches)} match(es)!")
            for idx, row in matches.iterrows():
                print(f"\nRow {idx}:")
                # Print first 10 columns
                for i in range(min(10, len(row))):
                    print(f"  Column {i}: {row.iloc[i]}")
        else:
            print("No matches")
    else:
        print("Sheet has less than 4 columns")
    print()
