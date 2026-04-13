# Cash-Out Section Display Format

## Overview
The cash-out section shows all final destinations of money across layers 2-6, grouped by type.

## Display Format for Each Category

### 1. ATM Withdrawals
**Shows 4 items:**
1. Bank Name
2. Account Number (full)
3. Disputed Amount (Column 6 - "Disputed Amount")
4. ATM Location (Column 8 - "Place/Location of ATM") with 📍 icon

**Example:**
```
Bandhan Bank
20200140774487
₹2,19,700
📍 Gwalior
```

### 2. Cheque Withdrawals
**Shows 3 items:**
1. Bank Name
2. Account Number (full)
3. Disputed Amount

**Example:**
```
Bank of Baroda
36770100009568
₹9,50,000
```

### 3. POS Withdrawals
**Shows 4 items (3+1):**
1. Bank Name
2. Account Number (full)
3. Disputed Amount
4. Merchant Name (Column 8) with 🏪 icon

**Example:**
```
Shankar Petroleum
Bhilwara - Bandhan Bank
₹57,000
🏪 Bhilwara merchant
```

### 4. Transactions Frozen/Put on Hold
**Shows 3 items:**
1. Bank Name
2. Account Number (full)
3. Frozen Amount

**Example:**
```
Yes Bank
61 recs · ₹11,02,248
```

### 5. Others Less Than 500
**Shows 3 items:**
1. Bank Name
2. Account Number (full)
3. Fixed Amount (₹500)

**Example:**
```
Others
7319_0358
₹500
```

## Column Mappings

### ATM Sheet ("Withdrawal through ATM")
- Column 0: S No.
- Column 1: Acknowledgement No.
- Column 2: Account No./ (Wallet /PG/PA) Id
- Column 3: Transaction Id / UTR Number
- Column 4: Withdrawal Date & Time
- Column 5: Withdrawal Amount
- **Column 6: Disputed Amount** ← Used for display
- Column 7: ATM ID
- **Column 8: Place/Location of ATM** ← Used for display
- Column 9: Reference No
- Column 10: Remarks
- **Column 11: Action Taken By bank** ← Bank name
- Column 12: Date of Action
- Column 13: pisnodal

### Transaction Put on Hold Sheet
- Column 0: S No.
- Column 1: Acknowledgement No.
- Column 2: Account No./ (Wallet /PG/PA) Id
- Column 3: Transaction Id / UTR Number
- Column 4: Put on hold Date
- Column 5: Put on hold Amount
- **Column 6: Action Taken By bank** ← Bank name
- Column 7: Date of Action
- Column 8: pisnodal

### Others Less Then 500 Sheet
- Column 0: S No.
- Column 1: Acknowledgement No.
- Column 2: Account No./ (Wallet /PG/PA) Id
- Column 3: Transaction Id / UTR Number
- Column 4: Reference No
- Column 5: Remarks
- **Column 6: Action Taken By bank** ← Bank name
- Column 7: Date of Action
- Column 8: pisnodal

### Cheque Sheet ("Cash withdrawal through cheque")
- Column 2: Account No.
- Column 3: Transaction Id
- **Column 6: Action Taken By bank** ← Bank name (expected)
- **Column J (9): Disputed Amount** ← Used for display

### POS Sheet ("Withdrawal through POS")
- Column 2: Account No.
- Column 3: Transaction Id
- **Column 6: Action Taken By bank** ← Bank name (expected)
- Column 6: Withdrawal Amount
- **Column 8: Merchant Name** ← Used for display

## Visual Features

1. **Color Coding:**
   - ATM/Cheque/POS: Pink shades (#ffcdd2, #f8bbd0, #fce4ec)
   - Frozen: Green (#c8e6c9)
   - Others: Purple (#e1bee7)

2. **Icons:**
   - 📍 for ATM locations
   - 🏪 for POS merchants

3. **Grouping:**
   - Each category shows summary: "X txns · ₹Y total · subtitle"
   - Collapsed view for >3 items per category
   - Click to expand and see all

4. **No Status Dots:**
   - Cash-out nodes don't show status indicators
   - Only hierarchical flow nodes show status dots

## Data Source Priority

For each cash-out item, the code:
1. Checks if transaction ID or account number exists in the main flow tree
2. Deduplicates by transaction ID and account number
3. Uses disputed amount (not withdrawal amount) for ATM
4. Shows full account numbers (no truncation)
5. Adds location/merchant info where available

## Summary Statistics

Each category header shows:
- **ATM**: "X ATMs · Y accounts"
- **Cheque**: "₹X L disputed"
- **POS**: "X merchants"
- **Frozen**: "₹X L secured"
- **Others**: "X records"

---

**Last Updated:** April 11, 2026
