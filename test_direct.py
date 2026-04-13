"""Test the download function directly without Flask"""
import sys
sys.path.insert(0, '.')

# Import after adding to path
from app_new import build_hierarchical_data, init_database, process_excel_file
import pandas as pd
from io import BytesIO

print("1. Initializing database...")
init_database()

print("2. Processing Excel file...")
success, message = process_excel_file('LAYERS.xlsx')
print(f"   {message}")

if success:
    print("\n3. Building hierarchical data...")
    try:
        all_data = build_hierarchical_data()
        print(f"   Generated {len(all_data)} rows")
        
        if all_data:
            print("\n4. Creating Excel file...")
            df = pd.DataFrame(all_data)
            
            output = BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name='Hierarchical Report', index=False)
            
            output.seek(0)
            
            # Save to file
            with open('Direct_Test_Report.xlsx', 'wb') as f:
                f.write(output.read())
            
            print(f"   Excel file created: Direct_Test_Report.xlsx")
            print(f"   File size: {len(output.getvalue()):,} bytes")
            
            # Verify
            df_verify = pd.read_excel('Direct_Test_Report.xlsx')
            print(f"\n5. Verification:")
            print(f"   Rows: {len(df_verify)}")
            print(f"   Columns: {len(df_verify.columns)}")
            print(f"\n   First 3 rows:")
            print(df_verify[['Level', 'Layer', 'Child Transaction ID', 'Status']].head(3))
            
            print("\nSUCCESS! Download feature is working!")
        else:
            print("   No data generated")
            
    except Exception as e:
        print(f"   ERROR: {e}")
        import traceback
        traceback.print_exc()
