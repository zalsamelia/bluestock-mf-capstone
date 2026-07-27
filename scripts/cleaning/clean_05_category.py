# ==========================================================
# Day 2 - Data Cleaning
# Dataset : 05_category_inflows.csv
# ==========================================================

import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_PATH = PROJECT_ROOT / "data" / "processed"

CATEGORY_FILE = RAW_DATA_PATH / "05_category_inflows.csv"

category_df = pd.read_csv(CATEGORY_FILE)

print("\n" + "=" * 60)
print("Category Inflows Dataset")
print("=" * 60)

print(f"Rows    : {category_df.shape[0]}")
print(f"Columns : {category_df.shape[1]}")

print("\nColumn Names")
for column in category_df.columns:
    print(f"- {column}")

print("\nData Types")
print(category_df.dtypes)

print("\nFirst Five Rows")
print(category_df.head())

print("\nDataset Information")
category_df.info()

print("\nStatistical Summary")
print(category_df.describe(include="all"))

# ==========================================================
# Data Quality Assessment
# ==========================================================

print("\n" + "=" * 60)
print("Missing Values")
print("=" * 60)
print(category_df.isnull().sum())

print("\n" + "=" * 60)
print("Duplicate Records")
print("=" * 60)
print(f"Duplicate Rows : {category_df.duplicated().sum()}")

print("\n" + "=" * 60)
print("Categories")
print("=" * 60)
print(category_df["category"].value_counts())

print("\n" + "=" * 60)
print("Net Inflow Validation")
print("=" * 60)
print(f"Minimum Net Inflow : {category_df['net_inflow_crore'].min()}")
print(f"Maximum Net Inflow : {category_df['net_inflow_crore'].max()}")

# ==========================================================
# Data Cleaning
# ==========================================================

category_df["month"] = pd.to_datetime(category_df["month"])

category_df["category"] = category_df["category"].str.strip()

category_df["net_inflow_crore"] = pd.to_numeric(
    category_df["net_inflow_crore"],
    errors="coerce"
)

print("\n" + "=" * 60)
print("Data Cleaning Summary")
print("=" * 60)

print("Month converted to datetime.")
print("Category names standardized.")
print("Numeric values validated.")
print("Dataset cleaned successfully.")

# ==========================================================
# Save Dataset
# ==========================================================

output_file = PROCESSED_DATA_PATH / "clean_category_inflows.csv"

category_df.to_csv(output_file, index=False)

print(f"\nDataset saved to:\n{output_file}")