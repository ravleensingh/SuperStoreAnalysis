# SuperStore Retail Performance & Profitability Analysis

## Project Overview

This project conducts a comprehensive data visualization and analysis of **9,993 transactions** from a U.S. retail chain spanning **2014 to 2017**. The objective is to identify hidden drivers of profit leakage, quantify the impact of discount strategies, and surface actionable insights across product categories, customer segments, and geographic regions.

The business records an overall profit margin of **12.47%** on total revenue of **$2,296,919.70**, yet **18.71% of all transactions (1,870 records)** are loss-making — the majority of which are directly attributable to aggressive discounting above 20%.

> **Live Resources**
> - Kaggle Dataset: [Superstore Dataset — Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
> - Google Sheets (Pivot Tables & Analysis): [Google Sheets — Analysis & Dashboard](https://docs.google.com/spreadsheets/d/1uYMA31gywDBovLxOGKkN01vJsgJn0UiOrBL0BGHEHfw/edit?usp=sharing)
> - Looker Studio Dashboard (Live): [Looker Studio — Interactive Dashboard](https://datastudio.google.com/reporting/a8f98465-e7fb-4850-a190-e4742323a383)
> - Tableau Public Dashboard (Live): [Tableau Public — Interactive Dashboard](https://public.tableau.com/app/profile/ravleen.singh4050/viz/Book1_17777857884460/Overview?publish=yes)

---

## Repository Structure

```text
SuperStore_Analysis/
│
├── DataSet/
│   ├── raw/
│   │   ├── raw.csv                        # Original Kaggle dataset (9,994 records, 21 columns)
│   │   └── raw.xlsx
│   └── cleaned/
│       ├── cleaned.csv                    # Engineered dataset (9,993 records, 37 columns)
│       └── cleaned.xlsx
│
├── Pivot_Tables/
│   ├── exploring_PivotTables/
│   │   ├── explored_PivotTables.csv       # Exploratory pivot analysis
│   │   └── explored_PivotTables.xlsx
│   └── major_PivotTables/
│       ├── Major_PivotTables.csv          # Core analytical pivot tables
│       └── Major_PivotTables.xlsx
│
├── Dashboard/
│   ├── googlesheets_Dashboard.pdf         # Google Sheets dashboard export
│   └── lookerstudio_Dashboard.pdf         # Looker Studio dashboard export
│
├── Tableau_Analysis/
│   ├── data/                              # Raw and processed datasets for Tableau
│   ├── docs/                              # Data dictionary and workflow documentation
│   ├── notebooks/                         # Extraction, cleaning, EDA, and statistical analysis notebooks
│   ├── reports/                           # Tableau workflow project report
│   ├── scripts/                           # Reusable Tableau workflow pipeline
│   └── tableau/
│       ├── dashboard_links.md             # Tableau Public dashboard link
│       ├── screenshots/                   # Tableau dashboard screenshots
│       └── workbook/                      # Tableau workbook file
│
└── README.md
```

---

## Dataset Details

### Raw Dataset
| Attribute | Value |
|---|---|
| Source | Kaggle — Superstore Retail Sales Dataset |
| Records | 9,994 transactions |
| Columns | 21 |
| Time Period | 2014 – 2017 |
| Geography | 49 U.S. States |

**Original Columns:** `Row ID`, `Order ID`, `Order Date`, `Ship Date`, `Ship Mode`, `Customer ID`, `Customer Name`, `Segment`, `Country`, `City`, `State`, `Postal Code`, `Region`, `Product ID`, `Category`, `Sub-Category`, `Product Name`, `Sales`, `Quantity`, `Discount`, `Profit`

### Cleaned Dataset
| Attribute | Value |
|---|---|
| Records | 9,993 transactions |
| Columns | 37 (21 original + 16 engineered) |

**16 Engineered Columns Added:**

| Engineered Column | Description |
|---|---|
| `Transaction Id (PK)` | Unique primary key per transaction |
| `Year` | Extracted order year |
| `Month` | Extracted order month |
| `Quarter` | Fiscal quarter (Q1–Q4) |
| `Shipping Delay` | Days between order date and ship date |
| `Shipping Speed` | Categorical speed classification |
| `Customer Type` | Customer loyalty classification |
| `Order-Size` | Order size tier (Small / Medium / Large) |
| `Sales Per Unit` | Sales ÷ Quantity |
| `Profit Margin` | Profit ÷ Sales |
| `Loss Severity` | Severity classification of loss transactions |
| `Loss Flag` | Binary flag: Profit / Loss |
| `Order-Level Total Sales` | Aggregated sales grouped by Order ID |
| `Customer Purchase Frequency` | Transaction count per Customer ID |
| `Total Sales per Customer` | Cumulative sales per customer |
| `Discount Amount` | Absolute discount value (Sales × Discount Rate) |

---

## Key Metrics

| Metric | Value |
|---|---|
| Total Revenue | $2,296,919.70 |
| Total Profit | $286,409.85 |
| Overall Profit Margin | 12.47% |
| Loss-Making Transactions | 1,870 (18.71%) |
| Transactions with Discount > 20% | 1,392 |
| Loss Transactions with Discount > 20% | 1,347 (96.8% of all losses) |
| Unique Customers | 793 |
| Unique Products | 1,862 |
| Unique Orders | 5,009 |

---

## Category Performance

| Category | Total Sales | Total Profit | Profit Margin |
|---|---|---|---|
| Technology | $836,154.10 | $145,455.66 | 17.40% |
| Office Supplies | $719,046.99 | $122,490.88 | 17.04% |
| Furniture | $741,718.61 | $18,463.31 | 2.49% |

> Furniture is the primary profit leakage category, generating only a **2.49% margin** despite being the second-highest revenue contributor.

---

## Regional Performance

| Region | Total Sales | Total Profit |
|---|---|---|
| West | $725,457.93 | $108,418.79 |
| East | $678,499.99 | $91,534.90 |
| South | $391,721.90 | $46,749.71 |
| Central | $501,239.88 | $39,706.45 |

---

## Data Dimensions

| Dimension | Values |
|---|---|
| Categories | Furniture, Office Supplies, Technology |
| Sub-Categories | Accessories, Appliances, Art, Binders, Bookcases, Chairs, Copiers, Envelopes, Fasteners, Furnishings, Labels, Machines, Paper, Phones, Storage, Supplies, Tables |
| Customer Segments | Consumer, Corporate, Home Office |
| Shipping Modes | Standard Class, Second Class, First Class, Same Day |
| Regions | Central, East, South, West |
| States Covered | 49 |

---

## Pivot Table Analysis

### Exploring Pivot Tables
Initial exploratory analysis covering sales distribution by shipping speed, category-level margin trends, and discount-to-loss correlation patterns.

### Major Pivot Tables
Core decision-support analysis structured across three dimensions:

1. **Time × Region** — Year, Quarter, Month, and Region breakdown of Sales, Profit, Average Profit, Order Count, Quantity, and Average Discount
2. **Category × Sub-Category × Segment × Ship Mode** — Profitability and discount analysis across product hierarchy and fulfillment channels
3. **Loss Severity × Category × Sub-Category** — Isolation of high-loss and moderate-loss transactions with associated discount rates and sales volumes

---

## Dashboard

Dashboard assets are available across Google Sheets, Looker Studio, and Tableau:

| Asset | Description |
|---|---|
| `Dashboard/googlesheets_Dashboard.pdf` | Static export of the Google Sheets interactive dashboard |
| `Dashboard/lookerstudio_Dashboard.pdf` | Static export of the Looker Studio live dashboard |
| `Tableau_Analysis/tableau/screenshots/` | Tableau dashboard page screenshots |
| `Tableau_Analysis/tableau/workbook/Book1.twb` | Tableau workbook file |
| `Tableau_Analysis/tableau/dashboard_links.md` | Published Tableau Public dashboard link |

Live interactive versions are accessible via the links at the top of this document.

---

## Tableau Workflow

The Tableau workflow was added as a separate, isolated layer so the original Google Sheets and Looker Studio work remains unchanged.

### Tableau Workflow Highlights

- Rebuilds the dataset from raw data using Python and Jupyter
- Keeps the final Tableau-ready dataset limited to the approved 37 columns
- Includes extraction, cleaning, EDA, and statistical analysis notebooks
- Stores workbook and screenshots for dashboard documentation and portfolio use

### Tableau Workflow Files

- `Tableau_Analysis/README.md`
- `Tableau_Analysis/notebooks/01_extraction.ipynb` to `05_final_load_prep.ipynb`
- `Tableau_Analysis/scripts/superstore_pipeline.py`
- `Tableau_Analysis/docs/data_dictionary.md`
- `Tableau_Analysis/reports/project_report.md`
- `Tableau_Analysis/tableau/dashboard_links.md`
- `Tableau_Analysis/tableau/screenshots/`
- `Tableau_Analysis/tableau/workbook/Book1.twb`

---

## Tools & Technologies

| Tool | Purpose |
|---|---|
| Google Sheets | Data cleaning, feature engineering, pivot table analysis, dashboard |
| Looker Studio | Interactive live dashboard and data visualization |
| Python (Jupyter, Pandas, NumPy, Matplotlib, Seaborn, SciPy) | Extraction, cleaning, EDA, and Tableau workflow |
| Tableau Public | Interactive multi-page dashboard and storytelling |
| CSV / XLSX | Data storage and cross-tool compatibility |
