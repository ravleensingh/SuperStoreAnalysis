# SuperStore Tableau Workflow

This folder contains the reproducible Python-to-Tableau workflow used to extend the main `SuperStore_Analysis` project with a published Tableau Public dashboard. It does not replace the original Google Sheets or Looker Studio work. Instead, it rebuilds the dataset from the same SuperStore source and prepares a Tableau-ready export with the approved 37-column schema.

## Related Project Assets

- Main project summary: [../README.md](../README.md)
- Tableau Public dashboard: [Open Tableau Public](https://public.tableau.com/app/profile/ravleen.singh4050/viz/Book1_17785071275660/Overview)
- Cross-platform dashboard links: [tableau/dashboard_links.md](./tableau/dashboard_links.md)
- Written report: [reports/project_report.md](./reports/project_report.md)
- Data dictionary: [docs/data_dictionary.md](./docs/data_dictionary.md)

## Workflow Scope

The Tableau workflow was designed around four rules:

1. Rebuild the analysis from the raw SuperStore source.
2. Keep the Tableau work isolated from the original Google Sheets and Looker Studio deliverables.
3. Export only the approved 37 business-facing columns.
4. Document the workflow well enough to support portfolio review, grading, and future reuse.

## Included Outputs

| Path | Purpose |
|---|---|
| [data/raw/superstore_raw_dataset.csv](./data/raw/superstore_raw_dataset.csv) | Raw snapshot copied into the Tableau workflow |
| [data/processed/superstore_cleaned_dataset.csv](./data/processed/superstore_cleaned_dataset.csv) | Cleaned dataset produced by the Python pipeline |
| [data/processed/superstore_tableau_ready_dataset.csv](./data/processed/superstore_tableau_ready_dataset.csv) | Final Tableau-ready source used in the workbook |
| [notebooks/01_extraction.ipynb](./notebooks/01_extraction.ipynb) to [notebooks/05_final_load_prep.ipynb](./notebooks/05_final_load_prep.ipynb) | End-to-end notebook workflow |
| [scripts/superstore_pipeline.py](./scripts/superstore_pipeline.py) | Reusable export pipeline |
| [tableau/workbook/Book1.twb](./tableau/workbook/Book1.twb) | Tableau workbook |
| [tableau/screenshots/](./tableau/screenshots/) | Saved dashboard page screenshots |

## Dashboard Pages

The published Tableau dashboard is organized into six pages:

| Page | Focus |
|---|---|
| `Overview` | KPI cards, quarterly trend, monthly sales, discount by region, regional sales and profit, state map |
| `Sales Analysis` | Region-category mix, quarterly regional sales, sales by segment, sales by order size, yearly sales pattern |
| `Profit and Margin` | Regional profit, sub-category profit, quarterly profit trend, segment profit, margin heatmap |
| `Loss and Discount Risk` | Loss severity, category-level loss composition, profit-vs-loss by region, sub-category loss concentration |
| `Customer Analysis` | Segment mix, sales and profit by segment, customer counts by region, discount-vs-margin correlation |
| `Shipping and Ops` | Ship-mode mix, shipping-speed distribution, loss by shipping pattern, average shipping delay |

## Validated Tableau Dataset Summary

| Item | Value |
|---|---|
| Raw source rows | 9,994 |
| Duplicate business rows removed | 1 (`Row ID = 3407`) |
| Final rows | 9,993 |
| Final columns | 37 |
| Total Sales | $2,296,919.28 |
| Total Profit | $286,408.60 |
| Overall Profit Margin | 12.47% |
| Loss transactions | 1,870 |
| Transactions with discount above 20% | 1,392 |
| Losses with discount above 20% | 1,347 |
| Total quantity | 37,871 |
| Unique orders | 5,009 |
| Unique customers | 793 |
| Unique products | 1,862 |

## Final Schema

The Tableau-ready export contains these columns only:

`Row ID`, `Transaction Id (PK)`, `Order ID`, `Order Date`, `Year`, `Month`, `Quarter`, `Ship Date`, `Shipping Delay`, `Shipping Speed`, `Ship Mode`, `Customer ID`, `Customer Name`, `Customer Type`, `Segment`, `Country`, `City`, `State`, `Postal Code`, `Region`, `Product ID`, `Category`, `Sub-Category`, `Product Name`, `Sales`, `Quantity`, `Order-Size`, `Sales Per Unit`, `Discount`, `Profit`, `Profit Margin`, `Loss Severity`, `Loss Flag`, `Order-Level Total Sales (Grouped by Order ID C)`, `Customer Purchase Frequency (Customer ID = L)`, `Total sales per customer`, `Discount Amount (Sales × Discount)`

## Tableau-Specific Data Note

The Tableau workflow preserves the same business structure used in the main project, but it rounds row-level `Sales` and `Profit` values to two decimals before export. That creates a small cent-level difference from the Google Sheets master cleaned dataset:

| Dataset | Total Sales | Total Profit |
|---|---|---|
| Google Sheets cleaned dataset | $2,296,919.70 | $286,409.85 |
| Tableau-ready export | $2,296,919.28 | $286,408.60 |

This difference does not affect the direction of the insights, the KPI percentages, or the dashboard conclusions.

## Business Highlights Supported by Tableau

- `TECHNOLOGY` is the strongest category for both sales and profit.
- `FURNITURE` is the weakest category by margin and the main source of structural leakage.
- `Tables` and `Bookcases` remain the most problematic sub-categories.
- `West` is the best-performing region, while `Central` remains the weakest on margin.
- High discounts, especially above 20%, are strongly associated with losses.
- `Consumer` is the largest sales segment, while `Home Office` has the strongest margin profile.

## Notebook Order

1. `01_extraction.ipynb`
2. `02_cleaning.ipynb`
3. `03_eda.ipynb`
4. `04_statistical_analysis.ipynb`
5. `05_final_load_prep.ipynb`

All notebooks have already been executed and saved with visible outputs.

## Rebuild Commands

Refresh the processed outputs:

```bash
python SuperStore_Analysis/tableau_analysis/scripts/superstore_pipeline.py
```

Re-run a notebook in place:

```bash
jupyter nbconvert --to notebook --inplace --execute SuperStore_Analysis/tableau_analysis/notebooks/03_eda.ipynb
```
