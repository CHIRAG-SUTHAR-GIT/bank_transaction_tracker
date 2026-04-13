# Other Sheets Total Display Feature

## Overview
The main web view now displays the total amount from all other sheets (excluding Money Transfer sheet) at the top of the page.

## Display Location
The total appears in the header section, right after the record count:

```
Showing 150 account(s)  💰 Other Sheets Total: ₹17,09,145.00
```

## What's Included

### Sheets Counted:
1. **Withdrawal through ATM** - Uses Disputed Amount (Column 6)
2. **Cash withdrawal through cheque** - Uses Disputed Amount (if available)
3. **Withdrawal through POS** - Uses Disputed Amount (if available)
4. **Transaction put on hold** - Uses Put on hold Amount (Column 5)
5. **Others Less Then 500** - ₹500 per record

### Amount Priority:
1. **First Priority**: Disputed Amount column (if exists)
2. **Second Priority**: Transaction Amount or configured amount column
3. **Special Case**: Others Less Than 500 = ₹500 per record

## Visual Design

### Badge Style:
- **Background**: Purple gradient (matches the theme)
- **Icon**: 💰 (money bag)
- **Format**: ₹17,09,145.00 (Indian number format with 2 decimals)
- **Position**: Top right, next to record count

### Tooltip:
Hover over the badge to see breakdown by sheet:
```
Breakdown:
Withdrawal through ATM: ₹10,00,000 (58 records)
Transaction put on hold: ₹5,09,145 (61 records)
Others Less Then 500: ₹2,00,000 (400 records)
```

## API Endpoint

### Route: `/api/other-sheets-total`

**Response Format:**
```json
{
  "total": 1709145.00,
  "breakdown": {
    "Withdrawal through ATM": {
      "total": 1000000.00,
      "count": 58
    },
    "Transaction put on hold": {
      "total": 509145.00,
      "count": 61
    },
    "Others Less Then 500": {
      "total": 200000.00,
      "count": 400
    }
  },
  "count": 519
}
```

## When It Appears

### Shows:
- ✅ When data is loaded
- ✅ When total > 0
- ✅ After file upload
- ✅ After switching views

### Hidden:
- ❌ When no data loaded
- ❌ When total = 0
- ❌ When no other sheets exist

## Calculation Logic

### ATM Withdrawals:
```python
# Use Disputed Amount (Column 6)
for row in atm_sheet:
    amount = row[6]  # Disputed Amount
    total += amount
```

### Transaction Put on Hold:
```python
# Use Put on hold Amount (Column 5)
for row in hold_sheet:
    amount = row[5]  # Put on hold Amount
    total += amount
```

### Others Less Than 500:
```python
# Fixed ₹500 per record
total = number_of_records * 500
```

### Other Sheets (Cheque, POS):
```python
# Try to find Disputed Amount column first
disputed_col = find_column_with_name("disputed")
if disputed_col:
    amount = row[disputed_col]
else:
    amount = row[configured_amount_col]
total += amount
```

## Benefits

1. **Quick Overview**: See total recovery/cash-out at a glance
2. **No Calculation Needed**: Automatic calculation from all sheets
3. **Detailed Breakdown**: Hover to see per-sheet totals
4. **Always Visible**: Stays at top while scrolling
5. **Professional Look**: Matches the application theme

## Use Cases

### For Investigators:
- Quickly see total amount in other sheets
- Compare with main transaction flow
- Identify recovery patterns

### For Reporting:
- Include in summary reports
- Show total cash-out/recovery
- Breakdown by category

### For Analysis:
- Compare ATM vs Cheque vs POS
- See frozen amount total
- Track small transactions (Others)

## Technical Implementation

### Backend (Python):
```python
@app.route('/api/other-sheets-total')
def get_other_sheets_total():
    # Iterate through all other sheets
    # Calculate total based on disputed amount
    # Return JSON with total and breakdown
```

### Frontend (JavaScript):
```javascript
async function loadOtherSheetsTotal() {
    const response = await fetch('/api/other-sheets-total');
    const data = await response.json();
    // Display total in badge
    // Add tooltip with breakdown
}
```

## Example Display

### Scenario 1: Multiple Sheets
```
💰 Other Sheets Total: ₹17,09,145.00

Tooltip:
Withdrawal through ATM: ₹10,00,000 (58 records)
Transaction put on hold: ₹5,09,145 (61 records)
Others Less Then 500: ₹2,00,000 (400 records)
```

### Scenario 2: Only ATM
```
💰 Other Sheets Total: ₹10,00,000.00

Tooltip:
Withdrawal through ATM: ₹10,00,000 (58 records)
```

### Scenario 3: No Other Sheets
```
(Badge is hidden)
```

## Future Enhancements

Possible additions:
- Click to see detailed breakdown modal
- Filter main view by sheet type
- Export other sheets summary
- Compare with main sheet total
- Show percentage of total disputed amount

---

**Last Updated:** April 11, 2026
