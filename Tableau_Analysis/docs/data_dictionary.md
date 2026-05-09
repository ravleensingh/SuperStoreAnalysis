# SuperStore Final Dataset Data Dictionary

This document describes the 37-column Tableau-ready dataset used inside `tableau_analysis/`.

It is a Tableau workflow document, not the main whole-project documentation file for `SuperStore_Analysis`. For full-project documentation, use:

- [../../docs/final_project_documentation.md](../../docs/final_project_documentation.md)

## Dataset Lineage

| Layer | File | Role |
|---|---|---|
| Raw source | `SuperStore_Analysis/data/raw/raw.csv` | Original Kaggle dataset |
| Master cleaned dataset | `SuperStore_Analysis/data/processed/cleaned.csv` | Final Google Sheets dataset used for project-level business metrics |
| Tableau-ready dataset | `SuperStore_Analysis/tableau_analysis/data/processed/superstore_tableau_ready_dataset.csv` | Reproducible export used by the Tableau workbook |

## Dataset Summary

| Item | Details |
|---|---|
| Raw rows | 9,994 |
| Duplicate rows removed | 1 (`Row ID = 3407`) |
| Final rows | 9,993 |
| Raw columns | 21 |
| Final columns | 37 |
| Granularity | One row per transaction line item |

## Metric Reconciliation Note

The Google Sheets cleaned dataset and Tableau-ready export share the same 9,993-row structure and the same 37 columns. Their totals differ slightly because the Tableau pipeline rounds row-level `Sales` and `Profit` values during export.

| Dataset | Total Sales | Total Profit |
|---|---|---|
| Google Sheets cleaned dataset | $2,296,919.70 | $286,409.85 |
| Tableau-ready export | $2,296,919.28 | $286,408.60 |

This difference is expected and does not affect the analytical conclusions.

## Raw Source Columns

These 21 fields come directly from the source dataset:

`Row ID`, `Order ID`, `Order Date`, `Ship Date`, `Ship Mode`, `Customer ID`, `Customer Name`, `Segment`, `Country`, `City`, `State`, `Postal Code`, `Region`, `Product ID`, `Category`, `Sub-Category`, `Product Name`, `Sales`, `Quantity`, `Discount`, `Profit`

## Engineered Columns

The final dataset adds 16 business-facing fields.

| Column Name | Type | Logic | Purpose |
|---|---|---|---|
| `Transaction Id (PK)` | string | Sequential key such as `TXN-000001` | Stable transaction identifier |
| `Year` | integer | Extracted from `Order Date` | Year-level filtering and trend analysis |
| `Month` | string | Full month name from `Order Date` | Monthly analysis |
| `Quarter` | string | `Q1` to `Q4` from `Order Date` | Quarterly analysis |
| `Shipping Delay` | integer | Days between `Ship Date` and `Order Date` | Fulfillment performance analysis |
| `Shipping Speed` | string | `Fast` if `<= 3` days, `Normal` if `4 to 6`, `Slow` if `>= 7` | Simplified shipping classification |
| `Customer Type` | string | `Loyal` if customer purchase frequency `>= 10`, otherwise `Occasional` | Customer loyalty grouping |
| `Order-Size` | string | `Small` if `Sales < 100`, `Medium` if `100 to 499.99`, `Large` if `>= 500` | Basket-size grouping |
| `Sales Per Unit` | float | `Sales / Quantity`, rounded to 2 decimals | Unit economics |
| `Profit Margin` | float | `Profit / Sales`, rounded to 2 decimals | Margin analysis |
| `Loss Severity` | string | `Profit`, `Low Loss`, or `High Loss` based on profit thresholds | Loss-risk classification |
| `Loss Flag` | string | `Loss` if `Profit < 0`, otherwise `Profit` | Binary outcome grouping |
| `Order-Level Total Sales (Grouped by Order ID C)` | float | Sum of `Sales` within each `Order ID` | Order-level context |
| `Customer Purchase Frequency (Customer ID = L)` | integer | Count of transaction rows per `Customer ID` | Repeat-purchase context |
| `Total sales per customer` | float | Sum of `Sales` per `Customer ID` | Customer value context |
| `Discount Amount (Sales × Discount)` | float | `Sales * Discount Rate`, rounded to 2 decimals | Discount value in currency terms |

## Final 37-Column Schema

| # | Column Name | Type | Description |
|---|---|---|---|
| 1 | `Row ID` | integer | Original source row identifier |
| 2 | `Transaction Id (PK)` | string | Sequential transaction key |
| 3 | `Order ID` | string | Business order identifier |
| 4 | `Order Date` | string/date | Order date in `M/D/YYYY` format |
| 5 | `Year` | integer | Order year |
| 6 | `Month` | string | Full month name |
| 7 | `Quarter` | string | Quarter label |
| 8 | `Ship Date` | string/date | Ship date in `M/D/YYYY` format |
| 9 | `Shipping Delay` | integer | Days between order and ship dates |
| 10 | `Shipping Speed` | string | Shipping-speed bucket |
| 11 | `Ship Mode` | string | Source delivery mode |
| 12 | `Customer ID` | string | Customer identifier |
| 13 | `Customer Name` | string | Customer name |
| 14 | `Customer Type` | string | Loyalty-style customer grouping |
| 15 | `Segment` | string | Consumer, Corporate, or Home Office |
| 16 | `Country` | string | Country name |
| 17 | `City` | string | Customer city |
| 18 | `State` | string | Customer state |
| 19 | `Postal Code` | integer | Postal code |
| 20 | `Region` | string | Region grouping |
| 21 | `Product ID` | string | Product identifier |
| 22 | `Category` | string | Product category, standardized to uppercase |
| 23 | `Sub-Category` | string | Product sub-category |
| 24 | `Product Name` | string | Product description |
| 25 | `Sales` | float | Sales amount |
| 26 | `Quantity` | integer | Quantity ordered |
| 27 | `Order-Size` | string | Sales-size bucket |
| 28 | `Sales Per Unit` | float | Sales divided by quantity |
| 29 | `Discount` | string | Percent label such as `20%` |
| 30 | `Profit` | float | Profit amount |
| 31 | `Profit Margin` | float | Profit-to-sales ratio |
| 32 | `Loss Severity` | string | Profit, low loss, or high loss |
| 33 | `Loss Flag` | string | Profit or loss outcome |
| 34 | `Order-Level Total Sales (Grouped by Order ID C)` | float | Total sales for the same order |
| 35 | `Customer Purchase Frequency (Customer ID = L)` | integer | Number of transaction rows for the same customer |
| 36 | `Total sales per customer` | float | Total sales accumulated by customer |
| 37 | `Discount Amount (Sales × Discount)` | float | Currency value of discount |

## Temporary Analysis-Only Fields

The notebooks create helper columns for EDA and statistical testing, but these are not exported into the final Tableau CSV:

- `Order Date Parsed`
- `Ship Date Parsed`
- `Month Number`
- `Quarter Number`
- `Year Quarter`
- `Year Quarter Sort`
- `Discount Rate`
- `Profit Margin %`
- `Loss Indicator`
- `High Discount Indicator`
- `Profit Only`
- `Loss Only`
- `Absolute Loss`
- `Discount Band`

## Data Quality Notes

- Duplicate checking was performed on all raw fields except `Row ID`.
- The duplicated business row removed from the source was `Row ID = 3407`.
- `Category` values were standardized to uppercase for dashboard consistency.
- `Discount` is stored as a percent label in the final export to stay presentation-friendly across dashboard tools.
- Existing Google Sheets and Looker Studio deliverables remain preserved outside the Tableau workflow.
