# SuperStore Retail Performance and Profitability Analysis

This project analyzes the U.S. SuperStore retail dataset across Google Sheets, Looker Studio, and Tableau to explain where revenue is growing, where profit is leaking, and which operational patterns deserve business attention. The final deliverable is a complete dashboard portfolio backed by cleaned data, pivot-table analysis, reproducible Tableau preparation, and documented business findings.

## Live Project Links

- Kaggle Dataset: [Superstore Dataset - Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- Google Sheets Workbook: [Google Sheets - Cleaning, Pivot Tables, and Dashboard](https://docs.google.com/spreadsheets/d/1uYMA31gywDBovLxOGKkN01vJsgJn0UiOrBL0BGHEHfw/edit?usp=sharing)
- Looker Studio Dashboard: [Looker Studio - Interactive Dashboard](https://datastudio.google.com/reporting/a8f98465-e7fb-4850-a190-e4742323a383)
- Tableau Public Dashboard: [Tableau Public - Interactive Dashboard](https://public.tableau.com/app/profile/ravleen.singh4050/viz/Book1_17777857884460/Overview?publish=yes)

## Project Snapshot

| Item | Value |
|---|---|
| Raw source rows | 9,994 |
| Duplicate business rows removed | 1 (`Row ID = 3407`) |
| Final cleaned rows | 9,993 |
| Raw columns | 21 |
| Final business-facing columns | 37 |
| Time period | 2014 to 2017 |
| Geography | 49 U.S. states |
| Unique orders | 5,009 |
| Unique customers | 793 |
| Unique products | 1,862 |

## Dashboard Deliverables

| Platform | Role in the project | Live link | Local asset |
|---|---|---|---|
| Google Sheets | Cleaning, feature engineering, pivot tables, and summary dashboard | [Open workbook](https://docs.google.com/spreadsheets/d/1uYMA31gywDBovLxOGKkN01vJsgJn0UiOrBL0BGHEHfw/edit?usp=sharing) | [dashboard/googlesheets_Dashboard.pdf](./dashboard/googlesheets_Dashboard.pdf) |
| Looker Studio | Executive interactive dashboard for high-level KPI monitoring | [Open dashboard](https://datastudio.google.com/reporting/a8f98465-e7fb-4850-a190-e4742323a383) | [dashboard/lookerstudio_Dashboard.pdf](./dashboard/lookerstudio_Dashboard.pdf) |
| Tableau Public | Six-page analytical story with drill-down views and risk analysis | [Open dashboard](https://public.tableau.com/app/profile/ravleen.singh4050/viz/Book1_17777857884460/Overview?publish=yes) | [tableau_analysis/tableau/dashboard_links.md](./tableau_analysis/tableau/dashboard_links.md) |

## Validated KPI Baseline

The Google Sheets cleaned dataset is the master business dataset for the project.

| KPI | Value |
|---|---|
| Total Sales | $2,296,919.70 |
| Total Profit | $286,409.85 |
| Overall Profit Margin | 12.47% |
| Total Quantity | 37,871 |
| Loss-making transactions | 1,870 |
| Loss transaction share | 18.71% |
| Transactions with discount above 20% | 1,392 |
| Losses with discount above 20% | 1,347 |
| Share of high-discount transactions that are losses | 96.77% |
| Share of all loss transactions occurring above 20% discount | 72.03% |
| Average discount | 15.62% |

## Business Insights

### Sales and Growth

- `TECHNOLOGY` is the top revenue category with $836,154.10 in sales and the strongest absolute profit at $145,455.66.
- `FURNITURE` is the second-largest category by revenue at $741,718.61, but it contributes only $18,463.31 in profit and a 2.49% margin.
- `West` leads all regions in both sales ($725,457.93) and profit ($108,418.79), followed by `East`.
- `Central` generates meaningful revenue ($501,239.88) but underperforms on profit with only a 7.92% margin.
- The strongest sales quarter is `2017 Q4`, and late-year demand peaks in `November` and `December`.

### Profitability and Risk

- `Tables` is the largest structural loss-maker with -$17,725.59 in profit.
- `Bookcases` and `Supplies` also remain negative-profit sub-categories.
- `Copiers`, `Phones`, `Accessories`, and `Paper` are the strongest profit contributors.
- Discounts above 20% are the clearest risk zone: 1,347 of 1,392 high-discount transactions are loss-making.
- `Deep Discount` transactions are entirely loss-making in the Tableau risk analysis.
- `Central` has the highest average discount level at 24.04%, while `West` has the lowest at 10.93%.

### Customers and Operations

- `Consumer` is the largest segment, contributing 50.56% of total sales.
- `Home Office` is the smallest segment by revenue but has the highest profit margin at 14.05%.
- `Standard Class` handles 59.71% of transaction rows and dominates the shipping mix.
- `Normal` shipping speed accounts for 61.49% of transactions, with `Fast` at 32.29%.
- Shipping analysis shows that slow shipments are concentrated inside `Standard Class`, while fast delivery is driven by `First Class`, `Second Class`, and `Same Day`.

## Category and Region Summary

### Category Performance

| Category | Sales | Profit | Profit Margin |
|---|---|---|---|
| TECHNOLOGY | $836,154.10 | $145,455.66 | 17.40% |
| OFFICE SUPPLIES | $719,046.99 | $122,490.88 | 17.04% |
| FURNITURE | $741,718.61 | $18,463.31 | 2.49% |

### Regional Performance

| Region | Sales | Profit | Profit Margin | Average Discount |
|---|---|---|---|---|
| West | $725,457.93 | $108,418.79 | 14.94% | 10.93% |
| East | $678,499.99 | $91,534.90 | 13.49% | 14.53% |
| South | $391,721.90 | $46,749.71 | 11.93% | 14.73% |
| Central | $501,239.88 | $39,706.45 | 7.92% | 24.04% |

## Dashboard Storyline

### Google Sheets Dashboard

The Google Sheets dashboard is the original business summary layer. It combines cleaned data, pivot-table outputs, and executive KPI cards with charts for trend, discount, sub-category profitability, category comparison, ship-mode mix, quantity mix, and loss severity.

### Looker Studio Dashboard

The Looker Studio dashboard is the polished executive view. It focuses on top-level KPIs, sales and profit trend by quarter, regional comparisons, monthly sales patterns, and discount behavior by region through an interactive filter layer.

### Tableau Dashboard

The Tableau Public dashboard is the most detailed storytelling layer and is organized into six pages:

1. `Overview` for KPI cards, sales and profit trend, regional summary, discount by region, and the state-level map.
2. `Sales Analysis` for region-category mix, quarterly sales by region, segment-region sales, order-size contribution, and yearly sales progression.
3. `Profit and Margin` for region profit, sub-category profit, quarterly profit trend, profit-by-segment comparison, and the category-versus-ship-mode margin heatmap.
4. `Loss and Discount Risk` for loss severity split, category risk, regional profit-vs-loss comparison, and sub-category loss concentration.
5. `Customer Analysis` for segment mix, sales and profit by segment, segment-region customer counts, and the discount-versus-profit-margin relationship.
6. `Shipping and Ops` for shipping speed by category, ship-mode distribution, loss transactions by shipping speed and mode, and average shipping delay.

## Data Foundation

The project uses three closely related datasets:

| File | Purpose |
|---|---|
| [data/raw/raw.csv](./data/raw/raw.csv) | Original Kaggle extract |
| [data/processed/cleaned.csv](./data/processed/cleaned.csv) | Final Google Sheets master dataset used for business metrics |
| [tableau_analysis/data/processed/superstore_tableau_ready_dataset.csv](./tableau_analysis/data/processed/superstore_tableau_ready_dataset.csv) | Tableau-ready export with the same 37-column schema |

The 37-column final schema contains the original 21 source fields plus 16 engineered business fields, including:

- `Transaction Id (PK)`
- `Year`, `Month`, `Quarter`
- `Shipping Delay`, `Shipping Speed`
- `Customer Type`
- `Order-Size`
- `Sales Per Unit`
- `Profit Margin`
- `Loss Severity`, `Loss Flag`
- `Order-Level Total Sales (Grouped by Order ID C)`
- `Customer Purchase Frequency (Customer ID = L)`
- `Total sales per customer`
- `Discount Amount (Sales × Discount)`

## Metric Reconciliation Note

The Google Sheets cleaned dataset and Tableau-ready export share the same deduplicated 9,993-row structure, but they do not match to the cent because the Tableau pipeline rounds row-level `Sales` and `Profit` values during export.

| Dataset | Total Sales | Total Profit |
|---|---|---|
| Google Sheets master cleaned dataset | $2,296,919.70 | $286,409.85 |
| Tableau-ready export | $2,296,919.28 | $286,408.60 |

This difference is small, expected, and does not change the business conclusions or dashboard story. All public dashboards display rounded headline values, which is why the visible KPI cards remain aligned.

## Workflow Summary

1. Raw data was collected from Kaggle and stored in `data/raw/`.
2. Google Sheets was used to clean the dataset, engineer the 16 business-facing fields, and create exploratory plus major pivot tables.
3. Looker Studio was used to convert the summary layer into an executive dashboard.
4. A separate Python and Jupyter workflow was created in `tableau_analysis/` to reproduce the data preparation and publish a Tableau Public dashboard without changing the original Sheets and Looker deliverables.

## Repository Structure

```text
SuperStore_Analysis/
├── dashboard/
├── data/
│   ├── raw/
│   └── processed/
├── docs/
├── pivot_tables/
│   ├── exploring_PivotTables/
│   └── major_PivotTables/
├── tableau_analysis/
│   ├── data/
│   ├── docs/
│   ├── notebooks/
│   ├── reports/
│   ├── scripts/
│   └── tableau/
└── README.md
```

## Recommended Review Order

1. Read this `README.md` for the project summary and direct links.
2. Open the Google Sheets workbook to inspect cleaning logic, pivot tables, and the original dashboard layer.
3. Review the Looker Studio dashboard for the executive summary experience.
4. Open the Tableau Public dashboard for the complete six-page analytical story.
5. Use the Tableau workflow documentation in `tableau_analysis/` for reproducibility, data dictionary details, and the written report.

## Tools and Technologies

| Tool | Role |
|---|---|
| Google Sheets | Cleaning, feature engineering, pivot tables, dashboard |
| Looker Studio | Executive dashboarding |
| Tableau Public | Interactive multi-page storytelling dashboard |
| Python, Pandas, NumPy, SciPy, Jupyter | Reproducible Tableau workflow and validation |
| CSV and XLSX | Cross-tool data storage |
