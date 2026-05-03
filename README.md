# SuperStore Retail Performance and Profitability Analysis

This project analyzes the SuperStore retail dataset across Google Sheets, Looker Studio, and Tableau-focused Python notebooks. The original dashboard work in Google Sheets and Looker Studio is preserved as-is, and a separate Tableau workflow has been added inside `Tableau_Analysis/` so the raw-to-dashboard process can be reproduced cleanly in Python.

## Project Scope

- Preserve the existing Google Sheets dashboard, Looker Studio dashboard, and pivot-table work
- Rebuild the dataset from raw data for Tableau Public using notebooks
- Perform cleaning, EDA, and statistical analysis from scratch
- Export a professional Tableau-ready dataset with only the approved 37 columns

## Project Assets

| Area | Description |
|---|---|
| `DataSet/raw/` | Original raw SuperStore source files |
| `DataSet/cleaned/` | Existing Google Sheets cleaned benchmark files |
| `Pivot_Tables/` | Google Sheets pivot-table exports |
| `Dashboard/` | PDF exports of the Google Sheets and Looker Studio dashboards |
| `Tableau_Analysis/` | Isolated Python, notebook, and Tableau workflow |

## Tableau Workflow Summary

The Tableau workflow is fully contained inside `Tableau_Analysis/` and does not interfere with the existing dashboard files.

Published Tableau Public dashboard:
`https://public.tableau.com/app/profile/ravleen.singh4050/viz/Book1_17777857884460/Overview?publish=yes`

### Final Tableau Dataset

| Metric | Value |
|---|---|
| Final rows | `9,993` |
| Final columns | `37` |
| Total Sales | `$2,296,919.28` |
| Total Profit | `$286,408.60` |
| Overall Profit Margin | `12.47%` |
| Loss Transactions | `1,870` |
| High-Discount Transactions (`> 20%`) | `1,392` |
| Unique Orders | `5,009` |
| Unique Customers | `793` |
| Unique Products | `1,862` |

### Final Tableau Schema

The final dataset contains only these fields:

`Row ID`, `Transaction Id (PK)`, `Order ID`, `Order Date`, `Year`, `Month`, `Quarter`, `Ship Date`, `Shipping Delay`, `Shipping Speed`, `Ship Mode`, `Customer ID`, `Customer Name`, `Customer Type`, `Segment`, `Country`, `City`, `State`, `Postal Code`, `Region`, `Product ID`, `Category`, `Sub-Category`, `Product Name`, `Sales`, `Quantity`, `Order-Size`, `Sales Per Unit`, `Discount`, `Profit`, `Profit Margin`, `Loss Severity`, `Loss Flag`, `Order-Level Total Sales (Grouped by Order ID C)`, `Customer Purchase Frequency (Customer ID = L)`, `Total sales per customer`, `Discount Amount (Sales × Discount)`

## Key Insights

- `TECHNOLOGY` is the strongest category for both sales and profit.
- `FURNITURE` is the clearest margin leakage category.
- `Tables` and `Bookcases` are the most problematic sub-categories.
- `West` leads regional profit, while `Central` has the weakest profit margin.
- The discount threshold above `20%` is strongly linked to losses.

## Repository Structure

```text
SuperStore_Analysis/
|-- Dashboard/
|   |-- googlesheets_Dashboard.pdf
|   `-- lookerstudio_Dashboard.pdf
|-- DataSet/
|   |-- cleaned/
|   `-- raw/
|-- Pivot_Tables/
|   |-- exploring_PivotTables/
|   `-- major_PivotTables/
|-- Tableau_Analysis/
|   |-- data/
|   |-- docs/
|   |-- notebooks/
|   |-- reports/
|   |-- scripts/
|   `-- tableau/
`-- README.md
```

## Tableau Workflow Files

- `Tableau_Analysis/README.md`
- `Tableau_Analysis/notebooks/01_extraction.ipynb` to `05_final_load_prep.ipynb`
- `Tableau_Analysis/scripts/superstore_pipeline.py`
- `Tableau_Analysis/docs/data_dictionary.md`
- `Tableau_Analysis/reports/project_report.md`
- `Tableau_Analysis/tableau/dashboard_links.md`
- `Tableau_Analysis/tableau/screenshots/`
- `Tableau_Analysis/tableau/workbook/Book1.twb`

## Run Order

1. `01_extraction.ipynb`
2. `02_cleaning.ipynb`
3. `03_eda.ipynb`
4. `04_statistical_analysis.ipynb`
5. `05_final_load_prep.ipynb`

All five notebooks have already been executed and saved with visible outputs.
