# Project Report: SuperStore Analysis Dashboard Portfolio

## 1. Executive Summary

This project analyzes the SuperStore retail dataset across Google Sheets, Looker Studio, and Tableau to produce a complete business intelligence portfolio. The work began with raw transaction data from Kaggle, continued through cleaning and feature engineering in Google Sheets, and concluded with executive and analytical dashboards published through Looker Studio and Tableau Public.

The final business dataset contains 9,993 rows and 37 business-facing columns after removal of one duplicated business row. Across the final cleaned dataset, the business generated $2,296,919.70 in sales and $286,409.85 in profit, with an overall profit margin of 12.47%. The core business issue is discount-driven profit leakage, especially within Furniture and the Central region.

## 2. Project Objective

The objective of the project was to move beyond simple sales reporting and answer four business questions:

1. Which categories, regions, and segments drive profitable growth?
2. Where is profit leaking despite strong revenue?
3. How strongly are discounts associated with loss-making transactions?
4. How can dashboard design support both executive review and deeper operational analysis?

## 3. Data Foundation

### Source and Scope

| Item | Value |
|---|---|
| Source | Kaggle SuperStore dataset |
| Raw rows | 9,994 |
| Final cleaned rows | 9,993 |
| Raw columns | 21 |
| Final columns | 37 |
| Time period | 2014 to 2017 |
| States covered | 49 |
| Unique orders | 5,009 |
| Unique customers | 793 |
| Unique products | 1,862 |

### Data Quality and Cleaning

- One duplicate business record was identified and removed: `Row ID = 3407`.
- The final schema preserved the original 21 fields and added 16 engineered analysis fields.
- Key engineered fields included `Shipping Delay`, `Shipping Speed`, `Customer Type`, `Order-Size`, `Sales Per Unit`, `Profit Margin`, `Loss Severity`, `Loss Flag`, customer-level totals, and order-level totals.
- Google Sheets served as the master business dataset for the project.
- Tableau received a reproducible export of the same 37-column structure through a Python pipeline.

## 4. Deliverables Across Three Platforms

| Platform | Purpose | Outcome |
|---|---|---|
| Google Sheets | Cleaning, engineered columns, pivot-table exploration, original dashboard layer | Created the master cleaned dataset and pivot-based business views |
| Looker Studio | Executive KPI dashboard | Delivered a polished, interactive summary for fast decision review |
| Tableau Public | Multi-page analytical storytelling dashboard | Delivered a six-page drill-down dashboard for deeper business analysis |

### Tableau Page Structure

1. `Overview`
2. `Sales Analysis`
3. `Profit and Margin`
4. `Loss and Discount Risk`
5. `Customer Analysis`
6. `Shipping and Ops`

This structure allowed the final dashboard portfolio to serve both summary-level and investigative use cases.

## 5. Validated KPI Baseline

The following KPI baseline is taken from the final Google Sheets cleaned dataset:

| KPI | Value |
|---|---|
| Total Sales | $2,296,919.70 |
| Total Profit | $286,409.85 |
| Profit Margin | 12.47% |
| Total Quantity | 37,871 |
| Loss Transactions | 1,870 |
| Loss Share | 18.71% |
| High-Discount Transactions (`> 20%`) | 1,392 |
| High-Discount Loss Transactions | 1,347 |
| Average Discount | 15.62% |

### Tableau Export Note

The Tableau-ready dataset rounds row-level `Sales` and `Profit` values to two decimals, so its totals are slightly different:

- Tableau Sales: $2,296,919.28
- Tableau Profit: $286,408.60

This is a cent-level export difference only and does not change the project conclusions.

## 6. Findings

### 6.1 Category Performance

| Category | Sales | Profit | Margin |
|---|---|---|---|
| TECHNOLOGY | $836,154.10 | $145,455.66 | 17.40% |
| OFFICE SUPPLIES | $719,046.99 | $122,490.88 | 17.04% |
| FURNITURE | $741,718.61 | $18,463.31 | 2.49% |

Interpretation:

- `TECHNOLOGY` is the strongest growth and profit category.
- `OFFICE SUPPLIES` is stable and efficient.
- `FURNITURE` underperforms badly on margin and is the primary category-level concern.

### 6.2 Sub-Category Profitability

Strongest profit contributors:

- `Copiers`
- `Phones`
- `Accessories`
- `Paper`

Weakest profit contributors:

- `Tables`
- `Bookcases`
- `Supplies`

Interpretation:

- `Tables` is the clearest structural loss-maker.
- `Bookcases` also underperform despite meaningful sales volume.
- These sub-categories explain much of the category-level weakness inside Furniture.

### 6.3 Regional Performance

| Region | Sales | Profit | Margin | Average Discount |
|---|---|---|---|---|
| West | $725,457.93 | $108,418.79 | 14.94% | 10.93% |
| East | $678,499.99 | $91,534.90 | 13.49% | 14.53% |
| South | $391,721.90 | $46,749.71 | 11.93% | 14.73% |
| Central | $501,239.88 | $39,706.45 | 7.92% | 24.04% |

Interpretation:

- `West` is the best-performing region.
- `Central` combines high discounting with weak profit conversion and is the most important regional risk area.

### 6.4 Time Trends

- `2017 Q4` is the strongest sales quarter.
- `2016 Q4` and `2017 Q4` are especially strong for profit.
- Sales accelerate late in the calendar year, especially in `November` and `December`.

Interpretation:

- The business has clear seasonality.
- End-of-year planning, inventory positioning, and discount control matter disproportionately.

### 6.5 Discount and Loss Risk

This is the most important business story in the project:

- 1,392 transactions have discounts above 20%.
- 1,347 of those transactions are loss-making.
- 96.77% of high-discount transactions are losses.
- 72.03% of all loss transactions happen above the 20% discount threshold.
- Deep-discount transactions are entirely loss-making in the Tableau risk view.

Interpretation:

- Discounting above 20% is not a marginal issue. It is a primary driver of lost profit.
- The risk is especially visible in weak sub-categories such as `Tables`, `Bookcases`, and selected Office Supplies lines.

### 6.6 Customer and Operations Findings

- `Consumer` is the largest sales segment, contributing 50.56% of revenue.
- `Home Office` has the highest profit margin at 14.05%.
- `Standard Class` accounts for 59.71% of transaction rows.
- `Normal` shipping speed accounts for 61.49% of transactions.

Interpretation:

- Segment and fulfillment views are useful because profitability is not identical to sales volume.
- Operational dashboards benefit from separating order mix, shipping speed, and loss transactions instead of treating them as a single logistics measure.

## 7. Dashboard Design Implications

The final dashboard portfolio reflects the project findings in three layers:

- Google Sheets keeps the analytical foundation transparent by preserving formulas, engineered fields, and pivot logic.
- Looker Studio provides the clean executive layer with KPI cards and essential trend comparisons.
- Tableau Public carries the deeper story through drill-down pages focused on sales, profit, risk, customers, and shipping.

This three-tool structure is appropriate for a cumulative capstone because it shows technical range, analytical rigor, and communication design across multiple BI environments.

## 8. Recommendations

1. Tighten discount policy above the 20% threshold, especially in low-margin categories and regions.
2. Review `Furniture`, with specific attention to `Tables` and `Bookcases`.
3. Audit `Central` region pricing and promotional behavior because high discounts are not converting into strong profit.
4. Preserve profitable growth levers in `Technology`, `West`, and high-profit sub-categories such as `Copiers`, `Phones`, and `Accessories`.
5. Use the Tableau risk pages and Looker executive page together: one for escalation, one for day-to-day monitoring.

## 9. Final Project Status

The project is complete from a dashboard-development perspective. The remaining work was documentation alignment, and that is now addressed through:

- a consolidated main README,
- a clearer Tableau workflow README,
- a cross-platform dashboard links file,
- an updated project report,
- and a synchronized data dictionary.

The repository now communicates the dataset, workflow, dashboard assets, links, and final business insights in a single professional narrative.
