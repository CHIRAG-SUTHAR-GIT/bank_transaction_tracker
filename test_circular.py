import sqlite3

conn = sqlite3.connect('transactions.db')
cursor = conn.cursor()

# Find the transaction with 7 children
trans_id = 'IN12602720384553'

print(f"Checking transaction: {trans_id}")

# Get the transaction
cursor.execute('SELECT * FROM transactions WHERE child_transaction_id = ?', (trans_id,))
row = cursor.fetchone()
if row:
    print(f"  Layer: {row[5]}")
    print(f"  Parent ID: {row[3]}")
    print(f"  Child ID: {row[9]}")

# Get its children
cursor.execute('''
    SELECT child_transaction_id, layer, parent_transaction_id 
    FROM transactions 
    WHERE parent_transaction_id = ? AND layer > 1
    ORDER BY layer
''', (trans_id,))

children = cursor.fetchall()
print(f"\nFound {len(children)} children:")
for child_id, layer, parent_id in children:
    print(f"  Child: {child_id}, Layer: {layer}, Parent: {parent_id}")
    
    # Check if this child has children
    cursor.execute('''
        SELECT COUNT(*) FROM transactions 
        WHERE parent_transaction_id = ? AND layer > ?
    ''', (child_id, layer))
    grandchildren_count = cursor.fetchone()[0]
    print(f"    Has {grandchildren_count} children")
    
    # Check for circular reference
    if child_id == trans_id:
        print(f"    ⚠️ CIRCULAR REFERENCE DETECTED!")

conn.close()
