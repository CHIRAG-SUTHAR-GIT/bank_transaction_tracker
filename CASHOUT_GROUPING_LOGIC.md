# Cash-Out Grouping Logic

## Overview
The cash-out section now groups entries by account number and sums the amounts for duplicate accounts within each category.

## Grouping Rules

### 1. Group by Account Number
- All entries with the same account number are grouped together
- Amounts are summed for the same account
- Only groups within the same category (ATM, Cheque, POS, Frozen, Others)

### 2. Safety Check
- The code only processes accounts that appear in the main transaction tree
- This ensures we're only summing accounts that are actually part of the flow
- Prevents mixing debited and credited accounts from different contexts

### 3. Display Format

#### Single Entry (No Grouping)
```
Bandhan Bank
20200135212801
₹10,000
📍 howrah
```

#### Multiple Entries (Grouped)
```
Bandhan Bank
20200135212801
₹45,000
📍 3 locations · 5 txns
```

## Examples

### Example 1: Same Account, Multiple ATM Withdrawals
**Input Data:**
- Account: 20200135212801
- Entry 1: ₹10,000 at howrah
- Entry 2: ₹15,000 at kolkata
- Entry 3: ₹20,000 at delhi

**Output:**
```
Bandhan Bank
20200135212801
₹45,000
📍 3 locations · 3 txns
```

### Example 2: Same Account, Multiple Frozen Transactions
**Input Data:**
- Account: 20200135212801
- Entry 1: ₹470.87
- Entry 2: ₹1,200.00
- Entry 3: ₹800.00

**Output:**
```
Bandhan Bank
20200135212801
₹2,470.87
3 transactions
```

### Example 3: Same Account, Multiple Others Entries
**Input Data:**
- Account: 20200135444766
- Entry 1: ₹500
- Entry 2: ₹500
- Entry 3: ₹500

**Output:**
```
Bandhan Bank
20200135444766
₹1,500
3 transactions
```

## Location/Merchant Handling

### Single Location/Merchant
Shows the actual location or merchant name:
```
📍 howrah
```
or
```
🏪 Shankar Petroleum
```

### Multiple Locations/Merchants
Shows count instead of listing all:
```
📍 3 locations · 5 txns
```
or
```
🏪 2 merchants · 4 txns
```

## Transaction Count Display

When multiple entries are grouped:
- Shows "X transactions" or "X txns"
- Helps identify accounts with multiple withdrawals
- Useful for spotting patterns

## Benefits

1. **Cleaner Display**: Reduces clutter by grouping duplicate accounts
2. **Better Analysis**: Easy to see total amount per account
3. **Pattern Detection**: Quickly identify accounts with multiple transactions
4. **Accurate Totals**: Sums are calculated correctly per account

## Technical Details

### Data Structure
```python
account_data = {
    'account_number': {
        'bank': 'Bank Name',
        'amounts': [10000, 15000, 20000],
        'trans_ids': ['id1', 'id2', 'id3'],
        'extras': {'📍 howrah', '📍 kolkata', '📍 delhi'},
        'count': 3
    }
}
```

### Processing Steps
1. Iterate through all rows in the sheet
2. Check if account is in the transaction tree
3. Group by account number
4. Collect amounts, transaction IDs, and extra info
5. Sum amounts per account
6. Format display with count and location info

### Safety Measures
- Only processes accounts in `all_accounts` set (from tree)
- Only processes transaction IDs in `all_trans_ids` set (from tree)
- Prevents mixing unrelated accounts
- Ensures data integrity

## Edge Cases

### Different Banks, Same Account Number
If two different banks have the same account number (unlikely but possible):
- They are treated as separate entries
- Bank name is stored with each account
- No cross-bank grouping occurs

### Missing Bank Name
If bank name is not found:
- Uses "Unknown Bank" as fallback
- Still groups by account number
- Maintains data integrity

### Zero or Negative Amounts
- Entries with amount ≤ 0 are skipped
- Not included in grouping
- Not counted in totals

---

**Last Updated:** April 11, 2026
