# Clickable Sheet Details Feature

## Overview
Users can now click on any sheet entry in the "Other Sheets" bar to view all transactions from that specific sheet in a detailed modal.

## How It Works

### 1. Visual Indication
- Each sheet item is now clickable (cursor changes to pointer)
- Hover effect: Background lightens when you hover over an item
- Clear visual feedback that items are interactive

### 2. Click Action
When you click on any sheet item (e.g., "🏧 ATM Withdrawal: ₹17,83,559 (112)"):
1. Modal opens immediately
2. Shows loading indicator
3. Fetches all transactions from that sheet
4. Displays in a formatted table

### 3. Modal Display

#### Header:
- Icon and sheet name (e.g., "🏧 ATM Withdrawal")
- Close button (X) in top-right
- Purple gradient background

#### Summary Section:
- Full sheet name from Excel
- Total number of records

#### Transaction Table:
Columns displayed:
1. **#** - Row number
2. **Bank** - Bank name
3. **Account Number** - Full account number
4. **Transaction ID** - Transaction/UTR number
5. **Amount** - Disputed amount (or transaction amount)
6. **Extra Info** - Location (ATM), Merchant (POS), or other details

#### Features:
- Alternating row colors for readability
- Scrollable if many transactions
- Monospace font for account/transaction IDs
- Green color for amounts
- Responsive design

## Example Display

### Click on: 🏧 ATM Withdrawal: ₹17,83,559 (112)

**Modal shows:**
```
┌─────────────────────────────────────────────────────────────┐
│ 🏧 ATM Withdrawal                                      ✕    │
├─────────────────────────────────────────────────────────────┤
│ Sheet: Withdrawal through ATM                               │
│ Total Records: 112                                          │
│                                                             │
│ ┌───┬──────────────┬─────────────────┬──────────────┬──────┐│
│ │ # │ Bank         │ Account Number  │ Trans ID     │ Amt  ││
│ ├───┼──────────────┼─────────────────┼──────────────┼──────┤│
│ │ 1 │ Bandhan Bank │ 20200135212801  │ 109061067970 │₹10K  ││
│ │ 2 │ Bandhan Bank │ 20200140774487  │ 109061067971 │₹2.2L ││
│ │ 3 │ Axis Bank    │ 050402...3863   │ 109061067972 │₹4.5L ││
│ │...│ ...          │ ...             │ ...          │...   ││
│ └───┴──────────────┴─────────────────┴──────────────┴──────┘│
└─────────────────────────────────────────────────────────────┘
```

## API Endpoint

### Route: `/api/sheet-details/<sheet_name>`

**Parameters:**
- `sheet_name`: URL-encoded name of the sheet

**Response:**
```json
{
  "sheet_name": "Withdrawal through ATM",
  "count": 112,
  "transactions": [
    {
      "trans_id": "109061067970",
      "account": "20200135212801",
      "bank": "Bandhan Bank",
      "amount": 10000.00,
      "extra": "howrah"
    },
    ...
  ]
}
```

## Sheet-Specific Logic

### ATM Withdrawals:
- Amount: Column 6 (Disputed Amount)
- Bank: Column 11 (Action Taken By bank)
- Extra: Column 8 (Place/Location of ATM)

### Cheque Withdrawals:
- Amount: Disputed Amount column (if exists)
- Bank: Column 6 (Action Taken By bank)
- Extra: None

### POS Withdrawals:
- Amount: Disputed Amount column (if exists)
- Bank: Column 6 (Action Taken By bank)
- Extra: Column 8 (Merchant Name)

### Transaction Hold:
- Amount: Column 5 (Put on hold Amount)
- Bank: Column 6 (Action Taken By bank)
- Extra: None

### Others Less Than 500:
- Amount: Fixed ₹500 per record
- Bank: Column 6 (Action Taken By bank)
- Extra: None

## User Experience

### Opening Modal:
1. Click on any sheet item
2. Hear click sound (if enabled)
3. Modal opens with loading indicator
4. Data loads (usually < 1 second)
5. Table displays with all transactions

### Closing Modal:
- Click X button in top-right
- Click outside the modal (on dark overlay)
- Press ESC key (browser default)

### Scrolling:
- Modal body is scrollable if content exceeds viewport
- Table header stays visible while scrolling
- Smooth scrolling experience

## Benefits

### For Investigation:
- Quick access to all transactions in a sheet
- See complete details without opening Excel
- Easy to scan through records
- Copy account numbers or transaction IDs

### For Verification:
- Verify amounts match expectations
- Check bank names are correct
- Confirm transaction IDs
- Review locations or merchants

### For Reporting:
- Take screenshots of specific sheets
- Reference specific transactions
- Share details with team
- Document findings

## Technical Implementation

### Frontend (JavaScript):
```javascript
async function showSheetDetails(sheetName, displayName, icon) {
    // Fetch data from API
    const response = await fetch(`/api/sheet-details/${encodeURIComponent(sheetName)}`);
    const data = await response.json();
    
    // Build table HTML
    // Display in modal
}
```

### Backend (Python):
```python
@app.route('/api/sheet-details/<sheet_name>')
def get_sheet_details(sheet_name):
    # Get sheet data
    # Extract transactions
    # Return JSON
```

### Styling:
- Purple gradient header (matches theme)
- Clean table design
- Responsive layout
- Professional appearance

## Example Use Cases

### Use Case 1: Verify ATM Locations
1. Click "🏧 ATM Withdrawal"
2. Scan "Extra Info" column for locations
3. Identify suspicious patterns (same location, multiple withdrawals)

### Use Case 2: Check Frozen Amounts
1. Click "🔒 Transaction Hold"
2. Review all frozen transactions
3. Calculate total secured amount
4. Identify which banks have frozen funds

### Use Case 3: Analyze Small Transactions
1. Click "📊 Others (<₹500)"
2. See all small transactions
3. Count frequency per account
4. Identify patterns

### Use Case 4: Review Cheque Withdrawals
1. Click "📝 Cheque Withdrawal"
2. See all cheque transactions
3. Note high-value withdrawals
4. Cross-reference with main flow

## Future Enhancements

Possible additions:
- Export sheet data to Excel
- Filter/search within modal
- Sort by column
- Highlight specific transactions
- Link to main transaction flow
- Show related transactions

---

**Last Updated:** April 11, 2026
