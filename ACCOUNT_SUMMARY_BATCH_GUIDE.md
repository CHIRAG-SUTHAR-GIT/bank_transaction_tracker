# Overnight Account Summary Database

This project can now analyse every Excel workbook in
`C:\Users\admin\Desktop\bank_trails` one at a time through the existing
`app_account.py` account-summary code.

## Start everything

Double-click:

`START_OVERNIGHT_AND_DASHBOARD.bat`

It opens:

1. The resumable overnight worker.
2. The local dashboard at `http://127.0.0.1:5002`.

The worker prevents Windows system sleep while it is active. The monitor may
turn off normally. Keep the computer connected to power, and do not close a
laptop lid if Windows is configured to sleep when the lid closes. Do not shut
down or restart Windows during the run. If the worker is stopped, start the
launcher again and it will continue from the saved queue.

## What is saved

- SQLite database: `data\account_summaries.sqlite`
- Worker log: `data\account_summary_worker.log`

The database keeps:

- Account Wise Summary
- Bank Wise Summary
- Partial Bank Wise Summary
- Per-file status, duration, attempts, and error details

Completed files are skipped on later runs. New files are discovered
automatically. Changed files are recalculated and replaced in one database
transaction, so incomplete results are not shown.

## Dashboard

The dashboard opens with **All ACKs** selected. It supports:

- All ACKs or one acknowledgement number
- Account, bank, and partial-bank views
- Status and text filters
- Processing progress and failed-file details
- Excel download for all ACKs or the selected ACK

The dashboard binds only to `127.0.0.1`, so the financial data is not published
to the internet.

## Command-line options

Run one pass and stop:

```powershell
python batch_account_summaries.py --input "C:\Users\admin\Desktop\bank_trails"
```

Retry files that reached the failure limit:

```powershell
python batch_account_summaries.py --retry-failed
```

Recalculate every discovered file:

```powershell
python batch_account_summaries.py --reprocess-all
```

Run only the dashboard:

```powershell
python account_summary_dashboard.py
```
