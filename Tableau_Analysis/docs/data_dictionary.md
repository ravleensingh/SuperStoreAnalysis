# SuperStore Tableau Workflow Data Dictionary

This dictionary documents the final 37-column dataset exported by the Tableau workflow in `SuperStore_Analysis/Tableau_Analysis`.

## Dataset Summary

| Item | Details |
|---|---|
| Source | `SuperStore_Analysis/DataSet/raw/raw.xlsx` |
| Raw rows | 9,994 |
| Final rows | 9,993 |
| Raw columns | 21 |
| Final columns | 37 |
| Final file | `data/processed/superstore_tableau_ready_dataset.csv` |
| Granularity | One row per transaction line item |

## Raw Source Columns

These 21 fields come directly from the source dataset:

`Row ID`, `Order ID`, `Order Date`, `Ship Date`, `Ship Mode`, `Customer ID`, `Customer Name`, `Segment`, `Country`, `City`, `State`, `Postal Code`, `Region`, `Product ID`, `Category`, `Sub-Category`, `Product Name`, `Sales`, `Quantity`, `Discount`, `Profit`

## Engineered Final Columns

The Tableau workflow adds 16 fields to reach the final 37-column schema.

| Column Name | Type | Logic | Purpose |
|---|---|---|---|
| `Transaction Id (PK)` | string | Sequential key: `TXN-000001`, `TXN-000002`, ... | Stable transaction identifier for Tableau |
| `Year` | integer | Year extracted from `Order Date` | Time filtering and trend analysis |
| `Month` | string | Full month name from `Order Date` | Month-level trend analysis |
| `Quarter` | string | Quarter label from `Order Date` (`Q1` to `Q4`) | Quarterly trend analysis |
| `Shipping Delay` | integer | `Ship Date - Order Date` in days | Shipping performance analysis |
| `Shipping Speed` | string | `Fast` if delay `<= 3`, `Normal` if `4 to 6`, `Slow` if `>= 7` | Simplified fulfillment classification |
| `Customer Type` | string | `Loyal` if customer purchase frequency `>= 10`, otherwise `Occasional` | Loyalty-style customer segmentation |
| `Order-Size` | string | `Small` if `Sales < 100`, `Medium` if `100 to 499.99`, `Large` if `>= 500` | Basket-size grouping |
| `Sales Per Unit` | float | `Sales / Quantity`, rounded to 2 decimals | Unit economics |
| `Profit Margin` | float | `Profit / Sales`, rounded to 2 decimals | Margin analysis |
| `Loss Severity` | string | `Profit`, `Low Loss`, `High Loss` based on profit thresholds | Loss-risk analysis |
| `Loss Flag` | string | `Loss` if `Profit < 0`, otherwise `Profit` | Quick profit/loss split |
| `Order-Level Total Sales (Grouped by Order ID C)` | float | Sum of `Sales` for each `Order ID` | Order-level revenue context |
| `Customer Purchase Frequency (Customer ID = L)` | integer | Count of rows per `Customer ID` | Repeat-purchase context |
| `Total sales per customer` | float | Sum of `Sales` for each `Customer ID` | Customer value context |
| `Discount Amount (Sales × Discount)` | float | `Sales * Discount Rate`, rounded to 2 decimals | Discount value in currency terms |

## Final 37-Column Schema

| # | Column Name | Type | Description |
|---|---|---|---|
| 1 | `Row ID` | integer | Original row identifier from source dataset |
| 2 | `Transaction Id (PK)` | string | Sequential transaction key created in the notebook workflow |
| 3 | `Order ID` | string | Business order identifier |
| 4 | `Order Date` | string/date | Order date stored in dashboard-friendly `M/D/YYYY` format |
| 5 | `Year` | integer | Order year |
| 6 | `Month` | string | Full month name |
| 7 | `Quarter` | string | Quarter label |
| 8 | `Ship Date` | string/date | Shipping date stored in dashboard-friendly `M/D/YYYY` format |
| 9 | `Shipping Delay` | integer | Days between order and ship date |
| 10 | `Shipping Speed` | string | Fulfillment speed bucket |
| 11 | `Ship Mode` | string | Delivery mode from source dataset |
| 12 | `Customer ID` | string | Customer identifier |
| 13 | `Customer Name` | string | Customer name |
| 14 | `Customer Type` | string | Loyalty-style customer segment |
| 15 | `Segment` | string | Consumer, Corporate, or Home Office |
| 16 | `Country` | string | Country name |
| 17 | `City` | string | Customer city |
| 18 | `State` | string | Customer state |
| 19 | `Postal Code` | integer | Postal code |
| 20 | `Region` | string | Regional grouping |
| 21 | `Product ID` | string | Product identifier |
| 22 | `Category` | string | Product category, standardized to uppercase |
| 23 | `Sub-Category` | string | Product sub-category |
| 24 | `Product Name` | string | Product name |
| 25 | `Sales` | float | Sales amount rounded to 2 decimals |
| 26 | `Quantity` | integer | Quantity ordered |
| 27 | `Order-Size` | string | Sales-size bucket |
| 28 | `Sales Per Unit` | float | Sales per unit |
| 29 | `Discount` | string | Discount label such as `20%` |
| 30 | `Profit` | float | Profit amount rounded to 2 decimals |
| 31 | `Profit Margin` | float | Profit margin ratio rounded to 2 decimals |
| 32 | `Loss Severity` | string | Profit/loss severity label |
| 33 | `Loss Flag` | string | `Profit` or `Loss` |
| 34 | `Order-Level Total Sales (Grouped by Order ID C)` | float | Order-level total sales |
| 35 | `Customer Purchase Frequency (Customer ID = L)` | integer | Number of transaction rows per customer |
| 36 | `Total sales per customer` | float | Total customer sales |
| 37 | `Discount Amount (Sales × Discount)` | float | Discount amount in currency terms |

## Temporary Analysis-Only Fields

The notebooks create a few helper fields for EDA and statistical analysis, but these are **not** exported into the final CSV:

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

- One duplicated business row was found in raw data and removed:
  - `Row ID = 3407`
- The Tableau-ready workflow keeps the final schema intentionally narrow and does not store dashboard helper columns in the exported file.
- Existing Google Sheets and Looker Studio assets remain preserved outside this workflow.
