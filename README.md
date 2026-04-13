# Financial Transaction Analysis System

A Flask-based web application for analyzing layered financial transactions, tracking money flow, and generating comprehensive reports.

## Features

### 1. Hierarchical Transaction View
- Multi-layer transaction tracking (Layer 1 through Layer 6+)
- Account-wise summary with credited/debited amounts
- Bank-wise grouping and analysis
- Interactive expandable/collapsible views

### 2. Flow Diagram Visualization
- Visual tree representation of money flow
- Color-coded nodes by account type:
  - 🔴 Red: Victim/Entry accounts
  - 🔵 Blue: Intermediate accounts
  - 🟠 Orange: Cash-out accounts
  - ⚫ Gray: Frozen accounts
- Status indicators:
  - 🔴 Red dot: PENDING
  - 🟠 Orange dot: PARTIAL
  - 🟢 Green dot: COMPLETE
- Clickable nodes with detailed transaction information
- Grouped display for multiple transactions
- Download as standalone HTML

### 3. Cash-Out Analysis
- ATM withdrawals with location tracking
- Cheque withdrawals
- POS transactions with merchant details
- Transaction holds/frozen accounts
- Others (transactions less than ₹500)
- Automatic grouping by account number
- Disputed amount tracking

### 4. Other Sheets Integration
- Horizontal summary bar showing totals from all sheets
- Clickable entries with detailed modal view
- Columns displayed:
  - Bank name
  - Account number
  - IFSC code
  - Transaction ID
  - Amount
  - Date
  - Extra information (location/merchant/remarks)

### 5. Reports
- Account Summary Report (Excel)
- Bank-wise Report
- Flow Diagram Report (HTML)
- Downloadable formats

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd LAYERED2
```

2. Install required packages:
```bash
pip install flask pandas openpyxl
```

3. Prepare your data:
   - Place your main transaction file (Excel) in the project directory
   - Ensure other sheets (ATM, Cheque, POS, Hold, Others) are in the same workbook

## Usage

1. Start the Flask application:
```bash
python app_account.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

3. Upload your Excel file or use the pre-configured file path

4. Navigate through different views:
   - Main page: Hierarchical transaction view
   - Flow Diagram: Visual money flow representation
   - Reports: Download various analysis reports

## File Structure

```
LAYERED2/
├── app_account.py          # Main Flask application
├── templates/
│   ├── index.html          # Main hierarchical view
│   └── flow_diagram.html   # Flow diagram visualization
├── static/                 # Static assets (if any)
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## Key Functions

### Transaction Processing
- `get_layer_transactions()`: Fetch transactions by layer
- `organize_tree_by_layers()`: Build hierarchical tree structure
- `get_cashout_data()`: Analyze cash-out channels

### API Endpoints
- `/api/transactions`: Get transactions by layer
- `/api/flow-diagram/<trans_id>`: Get flow diagram data
- `/api/other-sheets-total`: Get totals from other sheets
- `/api/sheet-details/<sheet_name>`: Get detailed sheet data

## Data Format

### Main Transaction Sheet
Expected columns:
- Column 0: Serial Number
- Column 1: Acknowledgement Number
- Column 2: Debited Account
- Column 3: Debited Transaction ID
- Column 4: Debited Amount
- Column 5: Layer
- Column 6: Credited Account
- Column 7: Credited Transaction ID
- Column 8: Credited Amount

### Other Sheets
- ATM Withdrawal: Disputed amount in column 6, location in column 8, bank in column 11
- Cheque Withdrawal: Standard format
- POS Withdrawal: Merchant name in column 8
- Transaction Hold: Frozen accounts
- Others Less Than 500: Fixed ₹500 per entry, remarks in column H

## Security Notes

- Excel files with sensitive data are excluded from git (.gitignore)
- Backup files are not tracked
- Test directories are excluded

## Browser Compatibility

- Chrome (recommended)
- Firefox
- Edge
- Safari

## License

[Add your license here]

## Contributors

[Add contributors here]
