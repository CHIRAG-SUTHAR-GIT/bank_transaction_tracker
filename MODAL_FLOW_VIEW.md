# 📊 Transaction Details Modal - Hierarchical Flow View

## Overview
When you click on any transaction box in the Flow Diagram, a modal popup now displays a complete hierarchical view showing:
- Where the money came FROM (parent transaction)
- The CURRENT transaction details
- Where the money went TO (child transactions)
- Any CASH-OUT channels detected

## Modal Layout

### 1. **Money Received From** (Parent) - Orange Section
```
⬆️ Money Received From (Layer X):
┌─────────────────────────────────────────────────┐
│ Debited Account: XXXX...XXXX                    │
│ Bank Name                                       │
│                                                 │
│ Credited Account: YYYY...YYYY                   │
│ Bank Name                                       │
│                                                 │
│ Amount: ₹XX,XX,XXX                             │
└─────────────────────────────────────────────────┘
```
- Shows the transaction that sent money to the current account
- Only displayed if this is not a Layer 1 transaction

### 2. **Current Transaction** (Highlighted) - Blue Gradient Section
```
📍 Current Transaction (Layer X):
┌─────────────────────────────────────────────────┐
│ Debited Account: XXXX...XXXX                    │
│ Bank Name                                       │
│                                                 │
│ Credited Account: YYYY...YYYY                   │
│ Bank Name                                       │
│                                                 │
│ Amount: ₹XX,XX,XXX                             │
│ Transaction ID: XXXXXXXXXX                      │
│ Status: [COMPLETE/PARTIAL/PENDING]             │
└─────────────────────────────────────────────────┘
```
- Prominently displayed with gradient background
- Shows complete transaction details
- Status badge with color coding

### 3. **Money Transferred To** (Children) - Green Section
```
⬇️ Money Transferred To (X transactions):
┌─────────────────────────────────────────────────┐
│ Layer Y                                         │
│ Debited: XXXX...XXXX (Bank Name)               │
│ Credited: YYYY...YYYY (Bank Name)              │
│ ₹XX,XXX                                        │
├─────────────────────────────────────────────────┤
│ Layer Y+1                                       │
│ Debited: XXXX...XXXX (Bank Name)               │
│ Credited: YYYY...YYYY (Bank Name)              │
│ ₹XX,XXX                                        │
└─────────────────────────────────────────────────┘
```
- Lists all child transactions
- Shows where the money flowed next
- Each child in a separate card

### 4. **Cash-out Channels** - Red/Green Section
```
💰 Cash-out Channels (X):
┌─────────────────────────────────────────────────┐
│ ATM Withdrawal                                  │
│ Withdrawal through ATM                          │
│ ₹XX,XXX                                        │
├─────────────────────────────────────────────────┤
│ Frozen/Hold                                     │
│ Transaction put on hold                         │
│ ₹XX,XXX                                        │
└─────────────────────────────────────────────────┘
```
- Shows all cash-out activities for this transaction
- Color coded:
  - Pink background: ATM/Cheque/POS withdrawals
  - Green background: Frozen/Hold transactions
- Includes sheet name and amount

### 5. **Summary** - Gray Section
```
📊 Summary:
┌─────────────────────────────────────────────────┐
│ Total Amount: ₹XX,XX,XXX                       │
│ Recovered: ₹XX,XXX                             │
│ Pending: ₹XX,XXX                               │
└─────────────────────────────────────────────────┘
```
- Quick overview of amounts
- Shows recovery status

## Color Scheme

### Section Colors
- **Parent (Orange)**: `#fff3e0` background, `#ff9800` border
- **Current (Blue Gradient)**: `#4facfe` to `#00f2fe` gradient, `#0288d1` border
- **Children (Green)**: `#e8f5e9` background, `#4caf50` border
- **Cash-out (Red/Green)**: 
  - Withdrawals: `#ffebee` background, `#f44336` border
  - Frozen: `#c8e6c9` background
- **Summary (Gray)**: `#f5f5f5` background

### Status Badges
- **COMPLETE**: Green badge
- **PARTIAL**: Yellow badge
- **PENDING**: Red badge

## Example Flow Visualization

```
┌─────────────────────────────────────────────────┐
│ ⬆️ PARENT (Layer 1)                            │
│ ICICI Bank → SBI                               │
│ ₹1,43,40,000                                   │
└─────────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────────┐
│ 📍 CURRENT (Layer 2) - HIGHLIGHTED             │
│ SBI → Punjab National Bank                     │
│ ₹21,55,497                                     │
│ Status: PARTIAL                                │
└─────────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────────┐
│ ⬇️ CHILDREN (3 transactions)                   │
│ Layer 3: Axis Bank → HDFC (₹4,49,940)        │
│ Layer 3: Punjab Bank → Yes Bank (₹4,00,000)  │
│ Layer 3: ICICI → Paytm (₹1,59,740)           │
└─────────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────────┐
│ 💰 CASH-OUT (2 channels)                       │
│ ATM Withdrawal: ₹2,19,700                      │
│ Frozen/Hold: ₹1,02,248                         │
└─────────────────────────────────────────────────┘
```

## Key Features

### 1. **Complete Flow Visibility**
- See the entire transaction chain in one view
- Understand money movement at a glance
- Identify all related transactions

### 2. **Cash-out Detection**
- Automatically shows if money was withdrawn via ATM/Cheque/POS
- Highlights frozen/hold amounts
- Includes "Others Less Than 500" entries

### 3. **Visual Hierarchy**
- Parent at top (where money came from)
- Current in middle (highlighted)
- Children below (where money went)
- Cash-out at bottom (final destinations)

### 4. **Responsive Design**
- Scrollable for long transaction chains
- Grid layout for account pairs
- Clean card-based design

### 5. **Color-Coded Information**
- Orange: Incoming money
- Blue: Current transaction (focus)
- Green: Outgoing money
- Red: Cash-out withdrawals
- Light green: Frozen/secured funds

## Use Cases

### Investigation
1. Click on suspicious transaction
2. See complete flow in modal
3. Identify all related accounts
4. Track cash-out channels

### Reporting
1. Click on key transactions
2. Take screenshots of modal
3. Include in investigation reports
4. Show complete money trail

### Analysis
1. Compare multiple transaction flows
2. Identify patterns in cash-out methods
3. Track common intermediate accounts
4. Monitor recovery status

## Technical Details

### Data Sources
- **Parent**: Found by matching credited account in previous layer
- **Current**: Direct from selected transaction
- **Children**: Found by matching debited transaction ID in next layer
- **Cash-out**: From breakdown_map (ATM, Cheque, POS, Hold, Others sheets)

### Performance
- Instant loading (pre-built maps)
- No additional database queries
- Cached breakdown data
- Smooth animations

---

**Version**: 2.0  
**Last Updated**: April 11, 2026  
**Feature**: Hierarchical Flow Modal View
