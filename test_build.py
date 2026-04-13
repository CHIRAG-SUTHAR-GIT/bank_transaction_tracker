import sys
sys.path.insert(0, '.')

from app import build_hierarchical_data

print("Testing build_hierarchical_data...")
try:
    data = build_hierarchical_data()
    print(f"✅ Success! Generated {len(data)} rows")
    
    # Show first few rows
    for i, row in enumerate(data[:5]):
        print(f"\nRow {i+1}:")
        print(f"  Level: {row['Level']}, Layer: {row['Layer']}")
        print(f"  Path: {row['Hierarchy Path'][:50]}...")
        print(f"  Status: {row['Status']}, Has Children: {row['Has Children']}")
        
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
