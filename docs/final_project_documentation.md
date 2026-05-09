# Final Project Documentation

## 1. Project Overview

`SuperStore_Analysis` is a complete retail analytics capstone built around the U.S. SuperStore dataset. The project combines data cleaning, feature engineering, pivot-table analysis, dashboard design, and business storytelling across three platforms:

- Google Sheets
- Looker Studio
- Tableau Public

The aim of the project is to identify revenue drivers, profit leakage, discount risk, customer patterns, and operational insights in a way that is both technically sound and presentation-ready.

## 2. Project Objectives

The project was designed to answer the following business questions:

1. Which categories, regions, and segments generate the strongest profitable growth?
2. Where is revenue high but profitability weak?
3. How strongly are discount levels linked to loss-making transactions?
4. What insights should be highlighted in executive dashboards versus deeper analytical dashboards?

## 3. Dataset Summary

| Item | Value |
|---|---|
| Source | Kaggle SuperStore dataset |
| Raw rows | 9,994 |
| Duplicate business rows removed | 1 (`Row ID = 3407`) |
| Final cleaned rows | 9,993 |
| Raw columns | 21 |
| Final columns | 37 |
| Time period | 2014 to 2017 |
| Geography | 49 U.S. states |
| Unique orders | 5,009 |
| Unique customers | 793 |
| Unique products | 1,862 |

## 4. Data Workflow

### Google Sheets Layer

Google Sheets was used as the original working environment for:

- cleaning the dataset
- deriving business-facing columns
- building exploratory pivot tables
- building major pivot tables
- designing the original dashboard view

This cleaned dataset is the master business dataset for the project.

### Looker Studio Layer

Looker Studio was used to convert the summary findings into an executive interactive dashboard focused on:

- KPI cards
- quarterly sales and profit trend
- sales and profit by region
- monthly sales pattern
- discount by region

### Tableau Layer

Tableau Public was used for the final multi-page storytelling dashboard. It adds richer filtering, better drill-down structure, and dedicated views for:

- profitability
- discount and loss risk
- customer analysis
- shipping and operations

## 5. Validated KPI Baseline

The following baseline uses the final cleaned Google Sheets dataset in `data/processed/cleaned.csv`.

| KPI | Value |
|---|---|
| Total Sales | $2,296,919.70 |
| Total Profit | $286,409.85 |
| Overall Profit Margin | 12.47% |
| Total Quantity | 37,871 |
| Loss Transactions | 1,870 |
| Loss Transaction Share | 18.71% |
| Transactions with Discount Above 20% | 1,392 |
| High-Discount Loss Transactions | 1,347 |
| Share of High-Discount Transactions That Are Losses | 96.77% |
| Share of All Loss Transactions Above 20% Discount | 72.03% |
| Average Discount | 15.62% |

## 6. Business Findings

### Category Performance

| Category | Sales | Profit | Margin |
|---|---|---|---|
| TECHNOLOGY | $836,154.10 | $145,455.66 | 17.40% |
| OFFICE SUPPLIES | $719,046.99 | $122,490.88 | 17.04% |
| FURNITURE | $741,718.61 | $18,463.31 | 2.49% |

Key conclusion:

`FURNITURE` is the clearest profit-leakage category because its revenue is high but its margin is far below the other two categories.

### Regional Performance

| Region | Sales | Profit | Margin | Avg Discount |
|---|---|---|---|---|
| West | $725,457.93 | $108,418.79 | 14.94% | 10.93% |
| East | $678,499.99 | $91,534.90 | 13.49% | 14.53% |
| South | $391,721.90 | $46,749.71 | 11.93% | 14.73% |
| Central | $501,239.88 | $39,706.45 | 7.92% | 24.04% |

Key conclusion:

`Central` is the most important regional risk area because it combines relatively high revenue with the highest average discount and the weakest margin.

### Sub-Category Risk

Strongest profit contributors:

- `Copiers`
- `Phones`
- `Accessories`
- `Paper`

Weakest sub-categories:

- `Tables`
- `Bookcases`
- `Supplies`

Key conclusion:

`Tables` is the most structurally loss-making sub-category in the project.

### Discount Risk

The discount-risk pattern is the most important business result in the project:

- 1,392 transactions have discounts above 20%
- 1,347 of them are loss-making
- 96.77% of high-discount transactions are losses
- 72.03% of all loss-making transactions occur above the 20% discount threshold

Key conclusion:

Discounting above 20% is strongly associated with unprofitable transactions and should be treated as a business control threshold.

### Customer and Operations Findings

- `Consumer` contributes 50.56% of total sales and is the largest segment.
- `Home Office` has the highest margin at 14.05%.
- `Standard Class` accounts for 59.71% of transaction rows.
- `Normal` shipping speed accounts for 61.49% of transactions.

## 7. Dashboard Deliverables

| Platform | Deliverable |
|---|---|
| Google Sheets | Cleaning workbook, pivot tables, and summary dashboard |
| Looker Studio | Executive dashboard |
| Tableau Public | Six-page analytical dashboard |

The Tableau dashboard pages are:

1. `Overview`
2. `Sales Analysis`
3. `Profit and Margin`
4. `Loss and Discount Risk`
5. `Customer Analysis`
6. `Shipping and Ops`

## 8. Dataset Reconciliation Note

The Tableau-ready dataset inside `tableau_analysis/` follows the same 37-column structure but rounds row-level `Sales` and `Profit` values during export.

| Dataset | Total Sales | Total Profit |
|---|---|---|
| Main cleaned dataset | $2,296,919.70 | $286,409.85 |
| Tableau-ready dataset | $2,296,919.28 | $286,408.60 |

This difference is small and does not affect the dashboard conclusions or final recommendations.

## 9. Final Recommendations

1. Tighten discounting policy above the 20% threshold.
2. Investigate `Tables` and `Bookcases` as priority sub-category problem areas.
3. Review `Central` region pricing and promotional strategy.
4. Preserve growth investment in high-performing areas such as `Technology`, `West`, and strong-margin sub-categories.
5. Use Google Sheets and Looker Studio for summary review, and use Tableau for detailed drill-down analysis.

## 10. Documentation Scope Note

This document is for the whole `SuperStore_Analysis` project.

It is intentionally broader than the documentation inside:

- [../tableau_analysis/docs/workflow_notes.md](../tableau_analysis/docs/workflow_notes.md)

The inner Tableau docs folder is limited to the Tableau workflow, export logic, and Tableau-specific dataset documentation.
