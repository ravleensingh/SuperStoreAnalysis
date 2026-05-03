# SuperStore Tableau Analysis Workflow

This folder contains the isolated Python-to-Tableau workflow for `SuperStore_Analysis`. It rebuilds the dataset from the raw SuperStore source, performs notebook-based cleaning and analysis, and exports a Tableau-ready CSV without changing the existing Google Sheets, pivot-table, or Looker Studio assets.

Published Tableau Public dashboard:
`https://public.tableau.com/app/profile/ravleen.singh4050/viz/Book1_17777857884460/Overview?publish=yes`

## Workflow Goal

The Tableau workflow was rebuilt around one rule:

> The final Tableau dataset must contain only the approved 37 business-facing columns.

No extra helper columns, uppercase duplicates, sort keys, or notebook-only analytical fields are stored in the exported CSV. Those helpers are created only inside notebooks or inside Tableau as calculated fields.

## Included Outputs

- `data/raw/superstore_raw_dataset.csv`
  Local raw snapshot copied into the Tableau workflow
- `data/processed/superstore_cleaned_dataset.csv`
  Cleaned dataset built from raw data with the final 37-column schema
- `data/processed/superstore_tableau_ready_dataset.csv`
  Final Tableau Public source file
- `notebooks/01_extraction.ipynb` to `05_final_load_prep.ipynb`
  End-to-end workflow with saved outputs visible inside each notebook
- `scripts/superstore_pipeline.py`
  Reusable cleaning and export logic
- `docs/data_dictionary.md`
  Data dictionary for the 37-column final dataset
- `reports/project_report.md`
  Business summary, findings, and recommendations
- `tableau/dashboard_links.md`
  Published Tableau Public dashboard link
- `tableau/screenshots/`
  Dashboard page screenshots for portfolio and review
- `tableau/workbook/Book1.twb`
  Tableau workbook file used to build the published dashboard

## Final Dataset Summary

| Item | Value |
|---|---|
| Raw source rows | 9,994 |
| Duplicate business rows removed | 1 (`Row ID = 3407`) |
| Final rows | 9,993 |
| Final columns | 37 |
| Total Sales | `$2,296,919.28` |
| Total Profit | `$286,408.60` |
| Overall Profit Margin | `12.47%` |
| Loss Transactions | `1,870` |
| High-Discount Transactions (`> 20%`) | `1,392` |
| High-Discount Loss Transactions | `1,347` |
| Unique Orders | `5,009` |
| Unique Customers | `793` |
| Unique Products | `1,862` |

## Final Schema

The Tableau-ready export contains these columns only:

`Row ID`, `Transaction Id (PK)`, `Order ID`, `Order Date`, `Year`, `Month`, `Quarter`, `Ship Date`, `Shipping Delay`, `Shipping Speed`, `Ship Mode`, `Customer ID`, `Customer Name`, `Customer Type`, `Segment`, `Country`, `City`, `State`, `Postal Code`, `Region`, `Product ID`, `Category`, `Sub-Category`, `Product Name`, `Sales`, `Quantity`, `Order-Size`, `Sales Per Unit`, `Discount`, `Profit`, `Profit Margin`, `Loss Severity`, `Loss Flag`, `Order-Level Total Sales (Grouped by Order ID C)`, `Customer Purchase Frequency (Customer ID = L)`, `Total sales per customer`, `Discount Amount (Sales × Discount)`

## Notebook Order

Run the notebooks in this order:

1. `01_extraction.ipynb`
2. `02_cleaning.ipynb`
3. `03_eda.ipynb`
4. `04_statistical_analysis.ipynb`
5. `05_final_load_prep.ipynb`

All notebooks have already been executed and saved with visible outputs.

## Key Cleaning Rules

- Exact duplicate business rows are checked after excluding `Row ID`
- `Category` is standardized to uppercase to match dashboard labeling
- `Shipping Speed` is derived from shipping delay:
  - `Fast` for `<= 3` days
  - `Normal` for `4 to 6` days
  - `Slow` for `>= 7` days
- `Customer Type` is standardized using purchase frequency:
  - `Loyal` for `>= 10` line-item purchases
  - `Occasional` otherwise
- `Order-Size` is derived from `Sales`:
  - `Small` for `< 100`
  - `Medium` for `100 to 499.99`
  - `Large` for `>= 500`
- `Loss Severity` is derived from `Profit`:
  - `Profit` for `>= 0`
  - `Low Loss` for `-200 < Profit < 0`
  - `High Loss` for `<= -200`

## Business Highlights

- `TECHNOLOGY` is the highest-revenue and highest-profit category.
- `FURNITURE` is the weakest category by margin at `2.49%`.
- `Tables` and `Bookcases` are the largest sub-category profit leakage points.
- `West` leads regional profit, while `Central` has the weakest regional margin.
- The discount threshold above `20%` remains the clearest operational risk zone.

## How to Rebuild

Run the reusable pipeline directly if you want to refresh the processed files:

```bash
python SuperStore_Analysis/Tableau_Analysis/scripts/superstore_pipeline.py
```

To re-execute a notebook and save its outputs:

```bash
jupyter nbconvert --to notebook --inplace --execute SuperStore_Analysis/Tableau_Analysis/notebooks/03_eda.ipynb
```
