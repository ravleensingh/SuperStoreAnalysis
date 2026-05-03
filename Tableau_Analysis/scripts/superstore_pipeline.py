"""Reusable cleaning and export pipeline for the SuperStore Tableau workflow."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import shutil

import numpy as np
import pandas as pd

LOYAL_CUSTOMER_MIN_PURCHASES = 10

FINAL_SCHEMA = [
    "Row ID",
    "Transaction Id (PK)",
    "Order ID",
    "Order Date",
    "Year",
    "Month",
    "Quarter",
    "Ship Date",
    "Shipping Delay",
    "Shipping Speed",
    "Ship Mode",
    "Customer ID",
    "Customer Name",
    "Customer Type",
    "Segment",
    "Country",
    "City",
    "State",
    "Postal Code",
    "Region",
    "Product ID",
    "Category",
    "Sub-Category",
    "Product Name",
    "Sales",
    "Quantity",
    "Order-Size",
    "Sales Per Unit",
    "Discount",
    "Profit",
    "Profit Margin",
    "Loss Severity",
    "Loss Flag",
    "Order-Level Total Sales (Grouped by Order ID C)",
    "Customer Purchase Frequency (Customer ID = L)",
    "Total sales per customer",
    "Discount Amount (Sales × Discount)",
]


@dataclass(frozen=True)
class ProjectPaths:
    """Resolved paths used across the SuperStore Tableau workflow."""

    project_root: Path
    source_raw_csv_path: Path
    source_raw_excel_path: Path
    source_cleaned_path: Path
    raw_snapshot_path: Path
    cleaned_output_path: Path
    tableau_output_path: Path


def resolve_project_paths(project_root: Path | None = None) -> ProjectPaths:
    """Resolve all paths used by the Tableau workflow."""

    root = (
        project_root.resolve()
        if project_root is not None
        else Path(__file__).resolve().parents[1]
    )
    superstore_root = root.parent

    return ProjectPaths(
        project_root=root,
        source_raw_csv_path=superstore_root / "DataSet" / "raw" / "raw.csv",
        source_raw_excel_path=superstore_root / "DataSet" / "raw" / "raw.xlsx",
        source_cleaned_path=superstore_root / "DataSet" / "cleaned" / "cleaned.csv",
        raw_snapshot_path=root / "data" / "raw" / "superstore_raw_dataset.csv",
        cleaned_output_path=root / "data" / "processed" / "superstore_cleaned_dataset.csv",
        tableau_output_path=root
        / "data"
        / "processed"
        / "superstore_tableau_ready_dataset.csv",
    )


def ensure_project_directories(paths: ProjectPaths) -> None:
    """Create local workflow directories when they do not already exist."""

    for directory in (
        paths.raw_snapshot_path.parent,
        paths.cleaned_output_path.parent,
        paths.project_root / "docs",
        paths.project_root / "notebooks",
        paths.project_root / "reports",
        paths.project_root / "scripts",
        paths.project_root / "tableau" / "screenshots",
    ):
        directory.mkdir(parents=True, exist_ok=True)


def _normalise_whitespace(value: object) -> object:
    """Collapse repeated whitespace while preserving missing values."""

    if pd.isna(value):
        return np.nan
    return " ".join(str(value).strip().split())


def _format_date(series: pd.Series) -> pd.Series:
    """Format datetimes like `11/8/2016` for parity with the existing project."""

    return (
        series.dt.month.astype("Int64").astype(str)
        + "/"
        + series.dt.day.astype("Int64").astype(str)
        + "/"
        + series.dt.year.astype("Int64").astype(str)
    )


def _format_percent_label(rate: float) -> str:
    """Convert a discount rate into a readable percent label without noise."""

    percent_value = round(float(rate) * 100, 2)
    label = f"{percent_value:.2f}".rstrip("0").rstrip(".")
    return f"{label}%"


def _categorise_shipping_speed(days: int) -> str:
    """Bucket shipping delay into a business-friendly speed label."""

    if days <= 3:
        return "Fast"
    if days <= 6:
        return "Normal"
    return "Slow"


def _categorise_order_size(sales: float) -> str:
    """Bucket order lines into Small, Medium, and Large sales tiers."""

    if sales < 100:
        return "Small"
    if sales < 500:
        return "Medium"
    return "Large"


def _categorise_customer_type(purchase_frequency: int) -> str:
    """Classify customers using transaction frequency."""

    return (
        "Loyal"
        if purchase_frequency >= LOYAL_CUSTOMER_MIN_PURCHASES
        else "Occasional"
    )


def _categorise_loss_severity(profit: float) -> str:
    """Assign loss severity labels using the project thresholds."""

    if profit >= 0:
        return "Profit"
    if profit <= -200:
        return "High Loss"
    return "Low Loss"


def copy_raw_snapshot(paths: ProjectPaths | None = None) -> Path:
    """Create an isolated raw CSV snapshot inside the Tableau workflow."""

    resolved_paths = resolve_project_paths() if paths is None else paths
    ensure_project_directories(resolved_paths)

    if resolved_paths.source_raw_excel_path.exists():
        df_raw = pd.read_excel(resolved_paths.source_raw_excel_path)
        df_raw.to_csv(resolved_paths.raw_snapshot_path, index=False)
    else:
        shutil.copy2(resolved_paths.source_raw_csv_path, resolved_paths.raw_snapshot_path)

    return resolved_paths.raw_snapshot_path


def load_raw_dataset(paths: ProjectPaths | None = None) -> pd.DataFrame:
    """Load the raw dataset, preferring the Excel file when available."""

    resolved_paths = resolve_project_paths() if paths is None else paths
    if resolved_paths.source_raw_excel_path.exists():
        return pd.read_excel(resolved_paths.source_raw_excel_path)
    return pd.read_csv(resolved_paths.source_raw_csv_path)


def load_existing_cleaned_dataset(paths: ProjectPaths | None = None) -> pd.DataFrame:
    """Load the existing Google Sheets cleaned dataset for reference checks."""

    resolved_paths = resolve_project_paths() if paths is None else paths
    return pd.read_csv(resolved_paths.source_cleaned_path)


def build_clean_dataset(
    df_raw: pd.DataFrame | None = None,
    paths: ProjectPaths | None = None,
) -> tuple[pd.DataFrame, list[int]]:
    """Clean the raw dataset and build the exact 37-column final schema."""

    resolved_paths = resolve_project_paths() if paths is None else paths
    df = load_raw_dataset(resolved_paths) if df_raw is None else df_raw.copy()

    text_columns = [
        "Order ID",
        "Ship Mode",
        "Customer ID",
        "Customer Name",
        "Segment",
        "Country",
        "City",
        "State",
        "Region",
        "Product ID",
        "Category",
        "Sub-Category",
        "Product Name",
    ]
    for column in text_columns:
        df[column] = df[column].map(_normalise_whitespace)

    dedupe_subset = [column for column in df.columns if column != "Row ID"]
    duplicate_mask = df.duplicated(subset=dedupe_subset, keep="first")
    dropped_row_ids = df.loc[duplicate_mask, "Row ID"].astype(int).tolist()
    df = df.loc[~duplicate_mask].copy()

    df["Order Date"] = pd.to_datetime(df["Order Date"])
    df["Ship Date"] = pd.to_datetime(df["Ship Date"])
    df["Row ID"] = df["Row ID"].astype(int)
    df["Postal Code"] = df["Postal Code"].astype(int)
    df["Quantity"] = df["Quantity"].astype(int)

    df["Country"] = df["Country"].fillna("United States")
    df["Ship Mode"] = df["Ship Mode"].str.title()
    df["Segment"] = df["Segment"].str.title()
    df["Region"] = df["Region"].str.title()
    df["City"] = df["City"].str.title()
    df["State"] = df["State"].str.title()
    df["Sub-Category"] = df["Sub-Category"].str.title()
    df["Category"] = df["Category"].str.upper()

    df = df.sort_values(["Row ID", "Order ID", "Product ID"]).reset_index(drop=True)

    df["Sales"] = df["Sales"].astype(float).round(2)
    df["Profit"] = df["Profit"].astype(float).round(2)
    df["Discount Rate Raw"] = df["Discount"].astype(float)
    df["Discount"] = df["Discount Rate Raw"].map(_format_percent_label)

    df["Transaction Id (PK)"] = [
        f"TXN-{index:06d}" for index in range(1, len(df) + 1)
    ]
    df["Year"] = df["Order Date"].dt.year.astype(int)
    df["Month"] = df["Order Date"].dt.month_name()
    df["Quarter"] = "Q" + df["Order Date"].dt.quarter.astype(str)
    df["Shipping Delay"] = (df["Ship Date"] - df["Order Date"]).dt.days.astype(int)
    df["Shipping Speed"] = df["Shipping Delay"].map(_categorise_shipping_speed)

    customer_frequency = df.groupby("Customer ID")["Customer ID"].transform("size")
    df["Customer Purchase Frequency (Customer ID = L)"] = customer_frequency.astype(int)
    df["Customer Type"] = customer_frequency.map(_categorise_customer_type)

    df["Order-Size"] = df["Sales"].map(_categorise_order_size)
    df["Sales Per Unit"] = (df["Sales"] / df["Quantity"]).round(2)
    df["Profit Margin"] = np.where(
        df["Sales"].ne(0),
        (df["Profit"] / df["Sales"]).round(2),
        np.nan,
    )
    df["Loss Severity"] = df["Profit"].map(_categorise_loss_severity)
    df["Loss Flag"] = np.where(df["Profit"] < 0, "Loss", "Profit")
    df["Discount Amount (Sales × Discount)"] = (
        df["Sales"] * df["Discount Rate Raw"]
    ).round(2)

    order_total_sales = df.groupby("Order ID")["Sales"].transform("sum").round(2)
    customer_total_sales = (
        df.groupby("Customer ID")["Sales"].transform("sum").round(2)
    )
    df["Order-Level Total Sales (Grouped by Order ID C)"] = order_total_sales
    df["Total sales per customer"] = customer_total_sales

    df["Order Date"] = _format_date(df["Order Date"])
    df["Ship Date"] = _format_date(df["Ship Date"])

    final_df = df[FINAL_SCHEMA].copy()
    return final_df, dropped_row_ids


def build_tableau_ready_dataset(df_clean: pd.DataFrame) -> pd.DataFrame:
    """Return the final Tableau-ready dataset in the approved schema."""

    return df_clean[FINAL_SCHEMA].copy()


def prepare_analysis_frame(df: pd.DataFrame) -> pd.DataFrame:
    """Add temporary helper columns used inside notebooks only."""

    analysis_df = df.copy()
    analysis_df["Order Date Parsed"] = pd.to_datetime(analysis_df["Order Date"])
    analysis_df["Ship Date Parsed"] = pd.to_datetime(analysis_df["Ship Date"])
    analysis_df["Month Number"] = analysis_df["Order Date Parsed"].dt.month
    analysis_df["Quarter Number"] = analysis_df["Order Date Parsed"].dt.quarter
    analysis_df["Year Quarter"] = (
        analysis_df["Year"].astype(str) + " " + analysis_df["Quarter"]
    )
    analysis_df["Year Quarter Sort"] = (
        analysis_df["Year"] * 10 + analysis_df["Quarter Number"]
    )
    analysis_df["Discount Rate"] = (
        analysis_df["Discount"].str.replace("%", "", regex=False).astype(float) / 100
    )
    analysis_df["Profit Margin %"] = analysis_df["Profit Margin"] * 100
    analysis_df["Loss Indicator"] = (analysis_df["Loss Flag"] == "Loss").astype(int)
    analysis_df["High Discount Indicator"] = (
        analysis_df["Discount Rate"] > 0.20
    ).astype(int)
    analysis_df["Profit Only"] = analysis_df["Profit"].clip(lower=0)
    analysis_df["Loss Only"] = analysis_df["Profit"].where(
        analysis_df["Profit"] < 0,
        0,
    )
    analysis_df["Absolute Loss"] = analysis_df["Loss Only"].abs()
    analysis_df["Discount Band"] = pd.cut(
        analysis_df["Discount Rate"],
        bins=[-0.001, 0, 0.10, 0.20, 0.40, 1.0],
        labels=[
            "No Discount",
            "Low Discount",
            "Moderate Discount",
            "High Discount",
            "Deep Discount",
        ],
    ).astype(str)
    return analysis_df


def validate_final_schema(df: pd.DataFrame) -> dict[str, object]:
    """Validate schema order and surface any mismatch cleanly."""

    actual_columns = list(df.columns)
    return {
        "matches_expected_schema": actual_columns == FINAL_SCHEMA,
        "missing_columns": [column for column in FINAL_SCHEMA if column not in actual_columns],
        "unexpected_columns": [
            column for column in actual_columns if column not in FINAL_SCHEMA
        ],
    }


def compute_project_metrics(df: pd.DataFrame) -> dict[str, float]:
    """Return headline QA metrics from the cleaned final dataset."""

    analysis_df = prepare_analysis_frame(df)
    sales_total = float(analysis_df["Sales"].sum())
    profit_total = float(analysis_df["Profit"].sum())
    loss_transactions = int((analysis_df["Loss Flag"] == "Loss").sum())
    high_discount_transactions = int((analysis_df["Discount Rate"] > 0.20).sum())
    high_discount_loss_transactions = int(
        (
            (analysis_df["Loss Flag"] == "Loss")
            & (analysis_df["Discount Rate"] > 0.20)
        ).sum()
    )

    return {
        "rows": int(len(analysis_df)),
        "sales_total": round(sales_total, 2),
        "profit_total": round(profit_total, 2),
        "profit_margin": round(profit_total / sales_total, 4),
        "loss_transactions": loss_transactions,
        "loss_transaction_pct": round(loss_transactions / len(analysis_df), 4),
        "high_discount_transactions": high_discount_transactions,
        "high_discount_loss_transactions": high_discount_loss_transactions,
        "unique_orders": int(analysis_df["Order ID"].nunique()),
        "unique_customers": int(analysis_df["Customer ID"].nunique()),
        "unique_products": int(analysis_df["Product ID"].nunique()),
        "total_quantity": int(analysis_df["Quantity"].sum()),
    }


def export_pipeline_outputs(
    paths: ProjectPaths | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame, list[int]]:
    """Run the pipeline and save the raw snapshot, cleaned CSV, and Tableau CSV."""

    resolved_paths = resolve_project_paths() if paths is None else paths
    ensure_project_directories(resolved_paths)
    copy_raw_snapshot(resolved_paths)

    df_clean, dropped_row_ids = build_clean_dataset(paths=resolved_paths)
    df_tableau = build_tableau_ready_dataset(df_clean)

    df_clean.to_csv(resolved_paths.cleaned_output_path, index=False)
    df_tableau.to_csv(resolved_paths.tableau_output_path, index=False)

    return df_clean, df_tableau, dropped_row_ids


def main() -> None:
    """CLI entrypoint used for local verification."""

    paths = resolve_project_paths()
    df_clean, df_tableau, dropped_row_ids = export_pipeline_outputs(paths=paths)
    metrics = compute_project_metrics(df_clean)
    schema_check = validate_final_schema(df_tableau)

    print("SuperStore Tableau workflow exported successfully.")
    print(f"Raw snapshot     : {paths.raw_snapshot_path}")
    print(f"Cleaned dataset  : {paths.cleaned_output_path}")
    print(f"Tableau dataset  : {paths.tableau_output_path}")
    print(f"Dropped row IDs  : {dropped_row_ids or 'None'}")
    print("Headline metrics :")
    for key, value in metrics.items():
        print(f"  - {key}: {value}")
    print("Schema check     :")
    for key, value in schema_check.items():
        print(f"  - {key}: {value}")


if __name__ == "__main__":
    main()
