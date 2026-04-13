# 🔄 Transaction Flow Diagram - User Guide

## Overview
The Transaction Flow Diagram is a visual representation of money flow from victim accounts through multiple layers to cash-out channels. It provides an intuitive way to understand complex transaction hierarchies.

## Features

### 1. Visual Hierarchy
- **Layer 1 (Seed)**: Victim/Entry account shown at the top
- **Intermediate Layers**: Money transfer through multiple accounts
- **Cash-out Section**: Final destinations grouped by type

### 2. Color Coding
- 🔴 **Light Pink/Salmon**: Victim/Entry accounts
- 🟡 **Beige/Tan**: Intermediate transfer accounts
- 🔴 **Pink**: Cash-out channels (ATM/Cheque/POS)
- 🟢 **Light Green**: Frozen/Hold transactions
- 🟣 **Purple**: Others Less Than 500

### 3. Interactive Features
- **Clickable Nodes**: Click any box to see detailed transaction information
- **Expandable Groups**: Click "+X more accounts" to expand collapsed groups
- **Modal Popups**: Transaction details appear in a clean modal window

### 4. Cash-out Channels
The bottom section groups all cash-out activities:
- **ATM Withdrawals**: From "Withdrawal through ATM" sheet
- **Cheque Withdrawals**: From "Cash withdrawal through cheque" sheet
- **POS Withdrawals**: From "Withdrawal through POS" sheet
- **Frozen/Hold**: From "Transaction put on hold" sheet
- **Others**: From "Others Less Than 500" sheet

## How to Use

### Accessing the Flow Diagram

#### Method 1: Web View
1. Upload your Excel files in the main application
2. Click the **"🔄 View Flow Diagram"** button
3. Select a Layer 1 transaction from the dropdown
4. Click **"Load Diagram"** to visualize

#### Method 2: Download Report
1. In the Flow Diagram page, select a transaction
2. Click **"Load Diagram"** to preview
3. Click **"Download Report"** to save as standalone HTML file
4. Open the downloaded HTML file in any browser (works offline)

### Understanding the Diagram

#### Layer Information
Each layer shows:
- Layer number and description
- Total transaction count
- Total disputed amount
- Individual account boxes with bank name, account number, and amount

#### Account Boxes
Each box displays:
- **Bank Name**: Primary identifier
- **Account Number**: Partial display (first 4 + last 4 digits)
- **Amount**: Transaction amount in ₹
- **Extra Info**: Location (ATM), Merchant (POS), etc.

#### Cash-out Summary
Shows aggregated information:
- Total transactions per type
- Total amount per type
- Additional details (ATM count, merchant count, etc.)

### Interacting with the Diagram

#### Viewing Details
1. Click any account box
2. Modal popup shows:
   - Full transaction ID
   - Complete account numbers
   - Transaction amount
   - Layer information
   - Status (COMPLETE/PARTIAL/PENDING)
   - Breakdown from other sheets
   - Updated and pending amounts

#### Expanding Collapsed Groups
1. Look for boxes with "+X more accounts"
2. Click to expand and see all accounts
3. Click again to collapse

#### Closing Modal
- Click the **X** button in top-right
- Click outside the modal window
- Press **ESC** key

## Technical Details

### Data Sources
- **Main Sheet**: "Money Transfer to" - Hierarchical transaction data
- **ATM Sheet**: "Withdrawal through ATM" - Column F (Withdrawal Amount)
- **Cheque Sheet**: "Cash withdrawal through cheque" - Column J
- **POS Sheet**: "Withdrawal through POS" - Column G
- **Hold Sheet**: "Transaction put on hold" - Various columns
- **Others Sheet**: "Others Less Than 500" - Fixed ₹500 per transaction

### Deduplication Logic
- ATM withdrawals: One entry per transaction ID
- Others Less Than 500: One ₹500 entry per transaction ID
- Other sheets: All unique entries included

### Collapse Threshold
- Layers with >5 accounts: Show 3 + collapse rest
- Cash-out groups with >3 items: Show 2 + collapse rest

## Best Practices

### For Investigation
1. Start with Layer 1 to identify victim account
2. Follow the flow through intermediate layers
3. Focus on cash-out section for recovery opportunities
4. Use modal details for complete information

### For Reporting
1. Download standalone HTML for offline viewing
2. Share with team members (no server required)
3. Take screenshots of specific sections
4. Use browser print function for PDF export

### For Analysis
1. Compare multiple Layer 1 transactions
2. Identify common intermediate accounts
3. Track cash-out patterns
4. Monitor frozen/hold amounts

## Troubleshooting

### Diagram Not Loading
- Ensure Excel files are uploaded first
- Check that Layer 1 transactions exist
- Verify "Money Transfer to" sheet is present

### Missing Cash-out Data
- Confirm other sheets are in the Excel file
- Check sheet names match expected patterns
- Verify amount columns have valid data

### Modal Not Showing Details
- Check browser console for errors
- Ensure transaction ID is valid
- Verify account number exists in data

## Browser Compatibility
- ✅ Chrome/Edge (Recommended)
- ✅ Firefox
- ✅ Safari
- ✅ Opera

## Performance Notes
- Large datasets (>1000 transactions) may take a few seconds to render
- Expanding many collapsed groups simultaneously may slow down the page
- Standalone HTML files work offline and load faster

## Future Enhancements
- Export as PDF
- Print-optimized layout
- Search/filter within diagram
- Zoom and pan controls
- Timeline view
- Network graph view

---

**Version**: 1.0  
**Last Updated**: April 11, 2026  
**Contact**: Gujarat Cyber Police
