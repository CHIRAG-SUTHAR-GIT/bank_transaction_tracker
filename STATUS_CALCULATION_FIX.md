# Status Calculation Fix

## Issue
Some nodes showed a red dot (PENDING status) but when clicked, the modal showed COMPLETE status.

## Root Cause
The status calculation was using the wrong transaction ID to check for children.

### How Transaction Flow Works:
```
Transaction A (debited_trans_id: 123, credited_trans_id: 456)
    ↓
Transaction B (debited_trans_id: 456, credited_trans_id: 789)
```

Money flows from A to B when:
- A's `credited_trans_id` (456) matches B's `debited_trans_id` (456)

### The Bug:
The code was checking if `debited_trans_id` had children, but it should check if `credited_trans_id` has children (because that's where money flows to).

**Before (Wrong):**
```python
status_info = calculate_status(trans_id, amount, layer, account)
# trans_id = debited_trans_id (123)
# Checking if 123 has children - WRONG!
```

**After (Correct):**
```python
status_info = calculate_status(credited_trans_id, amount, layer, account)
# credited_trans_id = 456
# Checking if 456 has children - CORRECT!
```

## Status Logic

### PENDING (Red Dot 🔴)
- No children found (money didn't flow further)
- No recovery in other sheets (ATM, Cheque, etc.)
- All money is still pending

### PARTIAL (Orange Dot 🟠)
- Some children found OR some recovery in other sheets
- But `pending_amount > 0.01`
- Part of the money is accounted for, but not all

### COMPLETE (Green Dot 🟢)
- Children found OR recovery in other sheets
- `pending_amount <= 0.01` (allowing for rounding errors)
- All money is accounted for

## Example

### Transaction Details:
```
Debited Account: 20200135212801
Debited Trans ID: 109061067970
Credited Trans ID: 403299369700
Amount: ₹10,000
Layer: 2
```

### Status Calculation:
1. Check if `403299369700` (credited_trans_id) has children in layer 3+
2. Check if `109061067970` (debited_trans_id) or `20200135212801` (account) appears in other sheets
3. Calculate: `pending = 10,000 - (children_total + recovery_total)`
4. Determine status based on pending amount

### Scenario 1: Complete Flow
- Children found: ₹8,000 (layer 3)
- ATM recovery: ₹2,000
- Total accounted: ₹10,000
- Pending: ₹0
- **Status: COMPLETE** ✅

### Scenario 2: Partial Flow
- Children found: ₹6,000 (layer 3)
- ATM recovery: ₹2,000
- Total accounted: ₹8,000
- Pending: ₹2,000
- **Status: PARTIAL** ⚠️

### Scenario 3: No Flow
- Children found: ₹0
- ATM recovery: ₹0
- Total accounted: ₹0
- Pending: ₹10,000
- **Status: PENDING** ❌

## Modal Display Consistency

The modal now uses the same status as the dot:

**Before:**
- Dot color: From node's calculated status
- Modal status: From API call (might be different)
- **Result: Inconsistency** ❌

**After:**
- Dot color: From node's calculated status
- Modal status: From node's calculated status (with API as fallback)
- **Result: Consistent** ✅

## Code Changes

### 1. Backend (app_account.py)
```python
# In organize_tree_by_layers function
credited_trans_id = node.get('credited_trans_id', '')
status_info = calculate_status(credited_trans_id, amount, layer, account)
```

### 2. Frontend (flow_diagram.html)
```javascript
// In showDetails function
const displayStatus = node.status || data.status || 'PENDING';
// Use displayStatus instead of data.status
```

## Testing

To verify the fix:
1. Look at a transaction with a red dot
2. Click to view details
3. Check if status in modal matches the dot color
4. Verify by checking:
   - Does it have children in next layer?
   - Is there recovery in other sheets?
   - What's the pending amount?

## Benefits

✅ Accurate status calculation
✅ Consistent display between dot and modal
✅ Correct identification of pending transactions
✅ Better investigation workflow
✅ Reliable reporting

---

**Last Updated:** April 11, 2026
