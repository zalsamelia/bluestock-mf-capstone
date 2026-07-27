# ==========================================================
# Day 2 - Data Cleaning
# Dataset : 01_fund_master.csv
# ==========================================================

# ==========================================================
# Import Libraries
# ==========================================================
import pandas as pd
from pathlib import Path

# ==========================================================
# Project Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"

PROCESSED_DATA_PATH = PROJECT_ROOT / "data" / "processed"

# ==========================================================
# Dataset File
# ==========================================================

FUND_MASTER_FILE = RAW_DATA_PATH / "01_fund_master.csv"

# ==========================================================
# Load Dataset
# ==========================================================

fund_df = pd.read_csv(
    FUND_MASTER_FILE,
    dtype={
        "fund_house": "str",
        "scheme_name": "str",
        "category": "str",
        "sub_category": "str",
        "plan": "str",
        "benchmark": "str",
        "fund_manager": "str",
        "risk_category": "str",
        "sebi_category_code": "str"
    }
)

# ==========================================================
# Dataset Inspection
# ==========================================================

print("\n" + "=" * 60)
print("Fund Master Dataset")
print("=" * 60)

print(f"Rows    : {fund_df.shape[0]}")
print(f"Columns : {fund_df.shape[1]}")

print("\nColumn Names")
for column in fund_df.columns:
    print(f"- {column}")

print("\nData Types")
print(fund_df.dtypes)

print("\nFirst Five Rows")
print(fund_df.head())

print("\nDataset Information")
fund_df.info()

print("\nStatistical Summary")
print(fund_df.describe(include="all"))

# ==========================================================
# Data Quality Assessment
# ==========================================================

print("\n" + "=" * 60)
print("Missing Values")
print("=" * 60)
print(fund_df.isnull().sum())

print("\n" + "=" * 60)
print("Duplicate Records")
print("=" * 60)
print(f"Duplicate Rows : {fund_df.duplicated().sum()}")

print("\n" + "=" * 60)
print("Fund Houses")
print("=" * 60)
print(fund_df["fund_house"].value_counts())

print("\n" + "=" * 60)
print("Categories")
print("=" * 60)
print(fund_df["category"].value_counts())

print("\n" + "=" * 60)
print("Plans")
print("=" * 60)
print(fund_df["plan"].value_counts())

print("\n" + "=" * 60)
print("Risk Categories")
print("=" * 60)
print(fund_df["risk_category"].value_counts())

# ==========================================================
# Data Cleaning
# ==========================================================

print("\n" + "=" * 60)
print("Data Cleaning Process")
print("=" * 60)

fund_df["launch_date"] = pd.to_datetime(fund_df["launch_date"])

string_columns = [
    "fund_house",
    "scheme_name",
    "category",
    "sub_category",
    "plan",
    "benchmark",
    "fund_manager",
    "risk_category",
    "sebi_category_code"
]

for column in string_columns:
    fund_df[column] = fund_df[column].str.strip()

print("✓ Launch date converted to datetime.")
print("✓ Text columns standardized.")
print("✓ Dataset cleaned successfully.")

# ==========================================================
# Save Clean Dataset
# ==========================================================

print("\n" + "=" * 60)
print("Saving Clean Dataset")
print("=" * 60)

output_file = PROCESSED_DATA_PATH / "clean_fund_master.csv"

fund_df.to_csv(output_file, index=False)

print(f"Dataset successfully saved to:\n{output_file}")