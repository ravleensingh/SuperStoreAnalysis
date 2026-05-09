# Tableau Workflow Notes

## 1. Purpose

The `tableau_analysis/` folder exists to create a reproducible Tableau layer for the `SuperStore_Analysis` project without changing the original Google Sheets and Looker Studio deliverables.

This workflow is intentionally narrower than the full capstone. It focuses only on:

- rebuilding the dataset from raw source files
- exporting the approved 37-column schema
- supporting the Tableau workbook and Tableau Public dashboard

## 2. Inputs and Outputs

### Inputs

- `../../data/raw/raw.csv`
- `../../data/raw/raw.xlsx`

### Outputs

- `../data/raw/superstore_raw_dataset.csv`
- `../data/processed/superstore_cleaned_dataset.csv`
- `../data/processed/superstore_tableau_ready_dataset.csv`
- `../tableau/workbook/Book1.twb`

## 3. Workflow Steps

1. Extract the raw SuperStore data.
2. Check duplicates excluding `Row ID`.
3. Remove the duplicated business row `Row ID = 3407`.
4. Standardize text fields and business labels.
5. Derive the approved engineered columns.
6. Export the cleaned Tableau-ready dataset.
7. Use the exported file as the source for the Tableau workbook.

## 4. Notebook Order

1. `01_extraction.ipynb`
2. `02_cleaning.ipynb`
3. `03_eda.ipynb`
4. `04_statistical_analysis.ipynb`
5. `05_final_load_prep.ipynb`

## 5. Tableau Dataset Scope

The Tableau-ready dataset contains only the approved 37 business-facing columns.

It excludes temporary notebook helper fields such as:

- parsed date helpers
- quarter sort helpers
- discount-band helper fields
- analysis-only indicator fields

Those helpers may be created during analysis but are not stored in the final Tableau export.

## 6. Tableau Dashboard Coverage

The Tableau Public dashboard contains six pages:

1. `Overview`
2. `Sales Analysis`
3. `Profit and Margin`
4. `Loss and Discount Risk`
5. `Customer Analysis`
6. `Shipping and Ops`

## 7. Metric Note

The Tableau export rounds row-level `Sales` and `Profit` values during export, which creates a small cent-level difference versus the main cleaned project dataset.

| Dataset | Total Sales | Total Profit |
|---|---|---|
| Main cleaned dataset | $2,296,919.70 | $286,409.85 |
| Tableau-ready dataset | $2,296,919.28 | $286,408.60 |

This difference is expected and does not change the project conclusions.

## 8. Scope Separation Note

This file documents only the Tableau subproject.

For full-capstone documentation across Google Sheets, Looker Studio, Tableau, pivot tables, and final business insights, use:

- [../../docs/final_project_documentation.md](../../docs/final_project_documentation.md)
