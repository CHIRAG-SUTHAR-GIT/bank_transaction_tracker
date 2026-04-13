import sqlite3

conn = sqlite3.connect('transactions.db')
cursor = conn.cursor()

# Test query
cursor.execute('''
    SELECT COUNT(*) FROM transactions 
    WHERE parent_transaction_id = "109061067970" AND layer > 1
''')
print('Children of 109061067970:', cursor.fetchone()[0])

# Check all layer 1 transactions
cursor.execute('SELECT child_transaction_id, layer FROM transactions WHERE layer = 1')
print('\nLayer 1 transactions:')
for row in cursor.fetchall():
    print(f'  {row[0]} - Layer {row[1]}')
    
    # Check children
    cursor.execute('''
        SELECT COUNT(*) FROM transactions 
        WHERE parent_transaction_id = ? AND layer > ?
    ''', (row[0], row[1]))
    children_count = cursor.fetchone()[0]
    print(f'    Has {children_count} children')

conn.close()
