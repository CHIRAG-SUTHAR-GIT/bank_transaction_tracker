import sqlite3

def calculate_transaction_status(child_trans_id, disputed_amount, current_layer=None):
    """Calculate status and pending amount for a transaction"""
    conn = sqlite3.connect('transactions.db')
    cursor = conn.cursor()
    
    # Check if transaction has children in Money Transfer sheet
    # Exclude same layer to avoid self-reference
    if current_layer:
        cursor.execute('''
            SELECT COUNT(*) FROM transactions 
            WHERE parent_transaction_id = ? AND layer > ?
        ''', (child_trans_id, current_layer))
    else:
        cursor.execute('''
            SELECT COUNT(*) FROM transactions 
            WHERE parent_transaction_id = ? AND child_transaction_id != parent_transaction_id
        ''', (child_trans_id,))
    has_children = cursor.fetchone()[0] > 0
    
    # Get sum of amounts from other sheets
    cursor.execute('''
        SELECT COALESCE(SUM(amount), 0) FROM other_transactions 
        WHERE transaction_id = ?
    ''', (child_trans_id,))
    other_sheets_total = cursor.fetchone()[0]
    
    # Check if transaction exists in other sheets
    cursor.execute('''
        SELECT COUNT(*) FROM other_transactions 
        WHERE transaction_id = ?
    ''', (child_trans_id,))
    in_other_sheets = cursor.fetchone()[0] > 0
    
    conn.close()
    
    pending_amount = disputed_amount - other_sheets_total
    
    # Determine status
    if not has_children and not in_other_sheets:
        status = 'PENDING'
    elif pending_amount > 0:
        status = 'PARTIAL'
    else:
        status = 'COMPLETE'
    
    return {
        'status': status,
        'updated_amount': other_sheets_total,
        'pending_amount': max(0, pending_amount),
        'has_children': has_children,
        'in_other_sheets': in_other_sheets
    }

def build_hierarchical_data(parent_id=None, layer=1, parent_path="", level=0, visited=None):
    """Recursively build hierarchical transaction data"""
    if visited is None:
        visited = set()
    
    print(f"{'  ' * level}Level {level}, Layer {layer}, Parent: {parent_id}")
    
    # Prevent infinite recursion
    if level > 10:  # Max 10 levels deep
        print(f"{'  ' * level}⚠️ Max level reached!")
        return []
    
    conn = sqlite3.connect('transactions.db')
    cursor = conn.cursor()
    
    if layer == 1:
        query = 'SELECT * FROM transactions WHERE layer = 1 ORDER BY s_no'  # All rows
        cursor.execute(query)
    else:
        # Prevent circular references
        if parent_id in visited:
            print(f"{'  ' * level}⚠️ Already visited {parent_id}")
            conn.close()
            return []
        visited.add(parent_id)
        
        # Get children - must be in higher layer to avoid self-reference
        query = '''SELECT * FROM transactions 
                   WHERE parent_transaction_id = ? 
                   AND layer > (SELECT layer FROM transactions WHERE child_transaction_id = ? LIMIT 1)
                   ORDER BY s_no'''
        cursor.execute(query, (parent_id, parent_id))
    
    columns = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()
    
    print(f"{'  ' * level}Found {len(rows)} transactions")
    
    all_data = []
    
    for row in rows:
        trans_dict = dict(zip(columns, row))
        child_id = trans_dict['child_transaction_id']
        trans_layer = trans_dict['layer']
        
        print(f"{'  ' * level}Processing: {child_id} (Layer {trans_layer})")
        
        # Calculate status
        status_info = calculate_transaction_status(
            child_id,
            trans_dict['disputed_amount'],
            trans_layer
        )
        
        print(f"{'  ' * level}  Has children: {status_info['has_children']}")
        
        # Create row data (simplified for testing)
        row_data = {
            'Level': level,
            'Layer': trans_layer,
            'Child Transaction ID': child_id,
            'Has Children': status_info['has_children']
        }
        
        all_data.append(row_data)
        
        # Recursively get children
        if status_info['has_children']:
            print(f"{'  ' * level}  Drilling down...")
            children_data = build_hierarchical_data(
                child_id,
                trans_layer + 1,
                "",
                level + 1,
                visited.copy()  # Pass a copy to avoid affecting siblings
            )
            all_data.extend(children_data)
    
    conn.close()
    return all_data

# Test
print("Testing build_hierarchical_data with debug output...\n")
try:
    data = build_hierarchical_data()
    print(f"Success! Generated {len(data)} rows")
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
