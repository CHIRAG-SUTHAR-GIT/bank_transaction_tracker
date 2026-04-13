"""
Test script for Flow Diagram functionality
"""
import requests
import json

BASE_URL = 'http://127.0.0.1:5001'

def test_flow_diagram():
    print("Testing Flow Diagram API...")
    print("=" * 60)
    
    # Test 1: Get Layer 1 transactions
    print("\n1. Getting Layer 1 transactions...")
    response = requests.get(f'{BASE_URL}/api/get_layer1_transactions')
    if response.status_code == 200:
        data = response.json()
        transactions = data.get('transactions', [])
        print(f"   ✓ Found {len(transactions)} Layer 1 transactions")
        
        if transactions:
            # Show first few
            for i, txn in enumerate(transactions[:3]):
                print(f"   - {txn['trans_id']}: {txn['bank']} - ₹{txn['amount']:,.2f}")
            
            # Test 2: Get flow diagram for first transaction
            print(f"\n2. Getting flow diagram for transaction: {transactions[0]['trans_id']}")
            trans_id = transactions[0]['trans_id']
            response = requests.get(f'{BASE_URL}/api/get_flow_diagram/{trans_id}')
            
            if response.status_code == 200:
                flow_data = response.json()
                
                if 'error' in flow_data:
                    print(f"   ✗ Error: {flow_data['error']}")
                else:
                    print(f"   ✓ Flow diagram generated successfully")
                    print(f"   - Acknowledgement: {flow_data.get('ack_no', 'N/A')}")
                    print(f"   - Total Disputed: ₹{flow_data.get('total_disputed', 0):,.2f}")
                    print(f"   - Layers: {len(flow_data.get('layers', []))}")
                    
                    # Show layer details
                    for layer in flow_data.get('layers', []):
                        print(f"     Layer {layer['layer']}: {layer['description']} - {len(layer['nodes'])} nodes")
                    
                    # Show cashout summary
                    cashout = flow_data.get('cashout', {})
                    print(f"\n   Cash-out channels:")
                    for cat_key, cat_data in cashout.items():
                        if cat_data['count'] > 0:
                            print(f"     - {cat_data['title']}: {cat_data['count']} txns, ₹{cat_data['total']:,.2f}")
                    
                    print("\n   ✓ All tests passed!")
            else:
                print(f"   ✗ Failed to get flow diagram: {response.status_code}")
        else:
            print("   ⚠ No Layer 1 transactions found. Please upload data first.")
    else:
        print(f"   ✗ Failed to get transactions: {response.status_code}")
    
    print("\n" + "=" * 60)
    print("Test complete!")

if __name__ == '__main__':
    try:
        test_flow_diagram()
    except requests.exceptions.ConnectionError:
        print("✗ Error: Could not connect to server.")
        print("  Make sure the Flask app is running on http://127.0.0.1:5001")
    except Exception as e:
        print(f"✗ Error: {str(e)}")
