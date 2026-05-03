# Project Report: SuperStore Tableau Workflow

## 1. Executive Summary

This workflow rebuilds the SuperStore dashboard dataset directly from the raw source file and prepares a clean, professional, Tableau-ready export. The project preserves the existing Google Sheets and Looker Studio work while adding a separate Python-and-Jupyter pipeline for reproducible cleaning, exploratory analysis, statistical testing, and Tableau Public dashboard development.

The final Tableau dataset contains **9,993 rows** and **37 columns**, with no extra helper fields stored in the CSV. The business remains profitable overall, generating **$2,296,919.28** in sales and **$286,408.60** in profit, but the analysis confirms that discount-heavy transactions are the dominant driver of profit leakage.

## 2. Project Objectives

- Rebuild the dataset from the raw SuperStore source using Python notebooks.
- Keep the Tableau workflow isolated from the existing dashboard assets.
- Export a final CSV containing only the approved 37 columns.
- Produce notebook outputs, EDA, and statistical evidence that directly support a multi-page Tableau Public dashboard.

## 3. Data and Cleaning Summary

| Item | Value |
|---|---|
| Raw source rows | 9,994 |
| Final rows | 9,993 |
| Duplicate business rows removed | 1 |
| Raw columns | 21 |
| Final columns | 37 |
| Source time period | 2014 to 2017 |
| Unique orders | 5,009 |
| Unique customers | 793 |
| Unique products | 1,862 |

### Key Cleaning Decisions

1. Removed one duplicated business row after checking all fields except `Row ID`.
2. Standardized the final Tableau export to the exact approved 37-column schema.
3. Kept notebook-only helper calculations out of the saved CSV.
4. Derived customer, loss, order-size, and shipping classifications in a documented way so the process stays reproducible.

## 4. Core KPI Snapshot

| KPI | Value |
|---|---|
| Total Sales | `$2,296,919.28` |
| Total Profit | `$286,408.60` |
| Overall Profit Margin | `12.47%` |
| Total Quantity | `37,871` |
| Loss Transactions | `1,870` |
| Loss Transaction Share | `18.71%` |
| Average Discount | `15.62%` |
| Transactions with Discount > 20% | `1,392` |
| Loss Transactions with Discount > 20% | `1,347` |

## 5. Major Analytical Findings

### 5.1 Category Performance

| Category | Sales | Profit | Profit Margin |
|---|---|---|---|
| `TECHNOLOGY` | `$836,154.02` | `$145,455.44` | `17.40%` |
| `FURNITURE` | `$741,718.36` | `$18,463.16` | `2.49%` |
| `OFFICE SUPPLIES` | `$719,046.90` | `$122,490.00` | `17.04%` |

`FURNITURE` is the most important problem area. It contributes major revenue but delivers a weak margin compared with the other two categories.

### 5.2 Sub-Category Risk

The strongest profit sub-categories are:

- `Copiers`
- `Phones`
- `Accessories`
- `Paper`

The weakest sub-categories are:

- `Tables`
- `Bookcases`
- `Supplies`

`Tables` is the clearest structural loss-maker in the product mix.

### 5.3 Regional Performance

| Region | Sales | Profit | Profit Margin |
|---|---|---|---|
| `West` | `$725,457.76` | `$108,418.31` | `14.94%` |
| `East` | `$678,499.93` | `$91,534.56` | `13.49%` |
| `Central` | `$501,239.76` | `$39,706.24` | `7.92%` |
| `South` | `$391,721.83` | `$46,749.49` | `11.93%` |

`Central` deserves special attention because its margin trails every other region.

### 5.4 Time Trends

- The strongest sales quarter is `2017 Q4`.
- Late-year months drive the highest revenue, especially `November` and `December`.
- The quarterly trend supports a strong time-series section on the Tableau overview page.

### 5.5 Discount Risk

The discount story is the most important operational insight in the project:

- Overall average discount is `15.62%`
- `1,392` transactions have discounts above `20%`
- `1,347` of those high-discount transactions are loss-making
- Every `Deep Discount` transaction in the analysis is a loss
- `High Discount` transactions have a `90.20%` loss rate

## 6. Statistical Validation

The statistical notebook confirms that the visual patterns are meaningful:

| Test | Result |
|---|---|
| Pearson correlation: Discount Rate vs Profit Margin | `r = -0.8645`, `p < 0.001` |
| Welch t-test: Profit for Discount `> 20%` vs `<= 20%` | Strong significant difference, `p < 0.001` |
| ANOVA: Profit differences across categories | Significant, `p < 0.001` |
| Chi-square: Discount Band vs Loss Flag | Strong dependence, `p < 0.001` |

These results justify giving discount-risk analysis a dedicated Tableau page instead of treating it as a minor supporting chart.

## 7. Dashboard Implications

The Tableau dashboard should mirror the strengths of the existing Looker Studio dashboard while using Tableau for richer drill-downs and interactions. The analysis strongly supports a six-page structure:

1. Overview
2. Sales Analysis
3. Profit and Margin
4. Loss and Discount Risk
5. Customer Analysis
6. Shipping and Operations

## 8. Recommendations

1. Reduce deep discounting on structurally weak product areas, especially `Tables` and `Bookcases`.
2. Review pricing and sales strategy in the `Central` region, where margin performance is weakest.
3. Use discounting more selectively, because the `> 20%` threshold is strongly associated with losses.
4. Highlight profitable category and regional combinations in Tableau so the dashboard balances risk insight with growth opportunity.

## 9. Conclusion

The SuperStore Tableau workflow is now reproducible, streamlined, and aligned with the final dashboard requirement. The notebooks run end to end, the final Tableau dataset contains only the approved 37 columns, and the project documentation is synchronized with the cleaned data and dashboard design direction.
