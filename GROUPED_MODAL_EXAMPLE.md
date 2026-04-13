# Grouped Transaction Modal Display

## Overview
When you click on a cash-out box that shows grouped transactions (e.g., "3 locations · 5 txns"), the modal now displays all individual transactions with their details.

## Modal Display Format

### Header Section
Shows the summary information:
- Bank Name
- Account Number
- Total Amount (sum of all transactions)
- Number of Transactions

### Individual Transactions Section
Lists each transaction separately with:
- Transaction number (1, 2, 3, etc.)
- Transaction ID
- Individual amount
- Location (for ATM) or Merchant (for POS)

## Example 1: Multiple ATM Withdrawals

### Box Display:
```
Bandhan Bank
20200135212801
₹45,000
📍 3 locations · 5 txns
```

### Modal Display (when clicked):
```
┌─────────────────────────────────────────────┐
│ Transaction Details                    ✕    │
├─────────────────────────────────────────────┤
│                                             │
│ Bank: Bandhan Bank                          │
│ Account Number: 20200135212801              │
│ Total Amount: ₹45,000                       │
│ Number of Transactions: 5                   │
│                                             │
│ ─────────────────────────────────────────  │
│                                             │
│ Individual Transactions:                    │
│                                             │
│ ┌─────────────────────────────────────┐   │
│ │ Transaction 1                        │   │
│ │ ID: 109061067970                     │   │
│ │ ₹10,000                              │   │
│ │ 📍 howrah                            │   │
│ └─────────────────────────────────────┘   │
│                                             │
│ ┌─────────────────────────────────────┐   │
│ │ Transaction 2                        │   │
│ │ ID: 109061067971                     │   │
│ │ ₹8,000                               │   │
│ │ 📍 kolkata                           │   │
│ └─────────────────────────────────────┘   │
│                                             │
│ ┌─────────────────────────────────────┐   │
│ │ Transaction 3                        │   │
│ │ ID: 109061067972                     │   │
│ │ ₹12,000                              │   │
│ │ 📍 delhi                             │   │
│ └─────────────────────────────────────┘   │
│                                             │
│ ┌─────────────────────────────────────┐   │
│ │ Transaction 4                        │   │
│ │ ID: 109061067973                     │   │
│ │ ₹7,000                               │   │
│ │ 📍 mumbai                            │   │
│ └─────────────────────────────────────┘   │
│                                             │
│ ┌─────────────────────────────────────┐   │
│ │ Transaction 5                        │   │
│ │ ID: 109061067974                     │   │
│ │ ₹8,000                               │   │
│ │ 📍 pune                              │   │
│ └─────────────────────────────────────┘   │
│                                             │
└─────────────────────────────────────────────┘
```

## Example 2: Multiple POS Transactions

### Box Display:
```
Shankar Petroleum
Bhilwara - Bandhan Bank
₹1,71,000
🏪 2 merchants · 4 txns
```

### Modal Display (when clicked):
```
┌─────────────────────────────────────────────┐
│ Transaction Details                    ✕    │
├─────────────────────────────────────────────┤
│                                             │
│ Bank: Bandhan Bank                          │
│ Account Number: 20200140774487              │
│ Total Amount: ₹1,71,000                     │
│ Number of Transactions: 4                   │
│                                             │
│ ─────────────────────────────────────────  │
│                                             │
│ Individual Transactions:                    │
│                                             │
│ ┌─────────────────────────────────────┐   │
│ │ Transaction 1                        │   │
│ │ ID: 403299369700                     │   │
│ │ ₹57,000                              │   │
│ │ 🏪 Shankar Petroleum                 │   │
│ └─────────────────────────────────────┘   │
│                                             │
│ ┌─────────────────────────────────────┐   │
│ │ Transaction 2                        │   │
│ │ ID: 403299369701                     │   │
│ │ ₹45,000                              │   │
│ │ 🏪 Shankar Petroleum                 │   │
│ └─────────────────────────────────────┘   │
│                                             │
│ ┌─────────────────────────────────────┐   │
│ │ Transaction 3                        │   │
│ │ ID: 403299369702                     │   │
│ │ ₹38,000                              │   │
│ │ 🏪 Prahalad Filling Stn.             │   │
│ └─────────────────────────────────────┘   │
│                                             │
│ ┌─────────────────────────────────────┐   │
│ │ Transaction 4                        │   │
│ │ ID: 403299369703                     │   │
│ │ ₹31,000                              │   │
│ │ 🏪 Prahalad Filling Stn.             │   │
│ └─────────────────────────────────────┘   │
│                                             │
└─────────────────────────────────────────────┘
```

## Example 3: Multiple Frozen Transactions

### Box Display:
```
Yes Bank
61 recs · ₹11,02,248
3 transactions
```

### Modal Display (when clicked):
```
┌─────────────────────────────────────────────┐
│ Transaction Details                    ✕    │
├─────────────────────────────────────────────┤
│                                             │
│ Bank: Yes Bank                              │
│ Account Number: 002261...025                │
│ Total Amount: ₹11,02,248                    │
│ Number of Transactions: 3                   │
│                                             │
│ ─────────────────────────────────────────  │
│                                             │
│ Individual Transactions:                    │
│                                             │
│ ┌─────────────────────────────────────┐   │
│ │ Transaction 1                        │   │
│ │ ID: 449864123456                     │   │
│ │ ₹5,50,000                            │   │
│ └─────────────────────────────────────┘   │
│                                             │
│ ┌─────────────────────────────────────┐   │
│ │ Transaction 2                        │   │
│ │ ID: 449864123457                     │   │
│ │ ₹3,25,000                            │   │
│ └─────────────────────────────────────┘   │
│                                             │
│ ┌─────────────────────────────────────┐   │
│ │ Transaction 3                        │   │
│ │ ID: 449864123458                     │   │
│ │ ₹2,27,248                            │   │
│ └─────────────────────────────────────┘   │
│                                             │
└─────────────────────────────────────────────┘
```

## Example 4: Multiple "Others Less Than 500"

### Box Display:
```
Bandhan Bank
20200135444766
₹1,500
3 transactions
```

### Modal Display (when clicked):
```
┌─────────────────────────────────────────────┐
│ Transaction Details                    ✕    │
├─────────────────────────────────────────────┤
│                                             │
│ Bank: Bandhan Bank                          │
│ Account Number: 20200135444766              │
│ Total Amount: ₹1,500                        │
│ Number of Transactions: 3                   │
│                                             │
│ ─────────────────────────────────────────  │
│                                             │
│ Individual Transactions:                    │
│                                             │
│ ┌─────────────────────────────────────┐   │
│ │ Transaction 1                        │   │
│ │ ID: 403299369700                     │   │
│ │ ₹500                                 │   │
│ └─────────────────────────────────────┘   │
│                                             │
│ ┌─────────────────────────────────────┐   │
│ │ Transaction 2                        │   │
│ │ ID: 403299369701                     │   │
│ │ ₹500                                 │   │
│ └─────────────────────────────────────┘   │
│                                             │
│ ┌─────────────────────────────────────┐   │
│ │ Transaction 3                        │   │
│ │ ID: 403299369702                     │   │
│ │ ₹500                                 │   │
│ └─────────────────────────────────────┘   │
│                                             │
└─────────────────────────────────────────────┘
```

## Visual Features

### Color Coding
- Header section: White background
- Individual transactions: Light gray background (#f8f9fa)
- Left border: Blue (#3498db) for each transaction card
- Amount: Green (#27ae60) for emphasis

### Typography
- Transaction number: Bold, dark gray
- Transaction ID: Small, gray text
- Amount: Bold, green, larger font
- Location/Merchant: Small, gray text with icon

### Layout
- Clean card-based design for each transaction
- Proper spacing between cards
- Scrollable if many transactions
- Responsive design

## Benefits

1. **Complete Transparency**: See every individual transaction
2. **Easy Verification**: Check each amount and location
3. **Pattern Analysis**: Identify suspicious patterns
4. **Audit Trail**: Full transaction history at a glance
5. **Professional Presentation**: Clean, organized display

## Technical Implementation

### Data Flow
1. User clicks grouped cash-out box
2. JavaScript checks if `node.is_grouped === true`
3. If grouped, displays `node.grouped_details` array
4. Each detail contains: trans_id, amount, extra (location/merchant)
5. Modal renders all transactions in a scrollable list

### No API Call Needed
- All data is already in the node object
- No additional server request required
- Instant display
- Works offline (for downloaded reports)

---

**Last Updated:** April 11, 2026
