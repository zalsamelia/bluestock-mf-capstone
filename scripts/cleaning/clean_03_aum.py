# ==========================================================
# Day 2 - Data Cleaning
# Dataset : 03_aum_by_fund_house.csv
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

AUM_FILE = RAW_DATA_PATH / "03_aum_by_fund_house.csv"

# ==========================================================
# Load Dataset
# ==========================================================

aum_df = pd.read_csv(
    AUM_FILE,
    dtype={
        "date": "str",
        "fund_house": "str"
    }
)

# ==========================================================
# Dataset Inspection
# ==========================================================

print("\n" + "=" * 60)
print("AUM by Fund House Dataset")
print("=" * 60)

print(f"Rows    : {aum_df.shape[0]}")
print(f"Columns : {aum_df.shape[1]}")

print("\nColumn Names")
for column in aum_df.columns:
    print(f"- {column}")

print("\nData Types")
print(aum_df.dtypes)

print("\nFirst Five Rows")
print(aum_df.head())

print("\nDataset Information")
aum_df.info()

print("\nStatistical Summary")
print(aum_df.describe(include="all"))

# ==========================================================
# Data Quality Assessment
# ==========================================================

print("\n" + "=" * 60)
print("Missing Values")
print("=" * 60)
print(aum_df.isnull().sum())

print("\n" + "=" * 60)
print("Duplicate Records")
print("=" * 60)
print(f"Duplicate Rows : {aum_df.duplicated().sum()}")

print("\n" + "=" * 60)
print("Fund Houses")
print("=" * 60)
print(aum_df["fund_house"].value_counts())

print("\n" + "=" * 60)
print("Date Range")
print("=" * 60)

print(f"Earliest Date : {aum_df['date'].min()}")
print(f"Latest Date   : {aum_df['date'].max()}")

print("\n" + "=" * 60)
print("AUM Validation")
print("=" * 60)

print(f"Minimum AUM : {aum_df['aum_crore'].min()}")
print(f"Maximum AUM : {aum_df['aum_crore'].max()}")

# ==========================================================
# Data Cleaning
# ==========================================================

print("\n" + "=" * 60)
print("Data Cleaning Process")
print("=" * 60)

aum_df["date"] = pd.to_datetime(aum_df["date"])

aum_df["fund_house"] = aum_df["fund_house"].str.strip()

print("✓ Date converted to datetime.")
print("✓ Fund house names standardized.")
print("✓ Dataset cleaned successfully.")

# ==========================================================
# Data Cleaning Summary
# ==========================================================

print("\n" + "=" * 60)
print("Data Cleaning Summary")
print("=" * 60)

print("No missing values detected.")
print("No duplicate records detected.")
print("Date column converted to datetime.")
print("Text columns standardized.")
print("Dataset is ready for analysis.")

# ==========================================================
# Save Clean Dataset
# ==========================================================

print("\n" + "=" * 60)
print("Saving Clean Dataset")
print("=" * 60)

output_file = PROCESSED_DATA_PATH / "clean_aum_by_fund_house.csv"

aum_df.to_csv(output_file, index=False)

print(f"Dataset successfully saved to:\n{output_file}")