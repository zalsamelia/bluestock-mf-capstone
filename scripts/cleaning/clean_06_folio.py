# ==========================================================
# Day 2 - Data Cleaning
# Dataset : 06_industry_folio_count.csv
# ==========================================================

import pandas as pd
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_PATH = PROJECT_ROOT / "data" / "processed"

FOLIO_FILE = RAW_DATA_PATH / "06_industry_folio_count.csv"

folio_df = pd.read_csv(FOLIO_FILE)

print("\n" + "=" * 60)
print("Industry Folio Count Dataset")
print("=" * 60)

print(f"Rows    : {folio_df.shape[0]}")
print(f"Columns : {folio_df.shape[1]}")

print("\nColumn Names")
for column in folio_df.columns:
    print(f"- {column}")

print("\nData Types")
print(folio_df.dtypes)

print("\nFirst Five Rows")
print(folio_df.head())

print("\nDataset Information")
folio_df.info()

print("\nStatistical Summary")
print(folio_df.describe(include="all"))

# ==========================================================
# Data Quality Assessment
# ==========================================================

print("\n" + "=" * 60)
print("Missing Values")
print("=" * 60)
print(folio_df.isnull().sum())

print("\n" + "=" * 60)
print("Duplicate Records")
print("=" * 60)
print(f"Duplicate Rows : {folio_df.duplicated().sum()}")

print("\n" + "=" * 60)
print("Month Range")
print("=" * 60)

print(f"Earliest Month : {folio_df['month'].min()}")
print(f"Latest Month   : {folio_df['month'].max()}")

print("\n" + "=" * 60)
print("Total Folios Validation")
print("=" * 60)

print(f"Minimum Total Folios : {folio_df['total_folios_crore'].min()}")
print(f"Maximum Total Folios : {folio_df['total_folios_crore'].max()}")

# ==========================================================
# Data Cleaning
# ==========================================================

folio_df["month"] = pd.to_datetime(folio_df["month"])

numeric_columns = [
    "total_folios_crore",
    "equity_folios_crore",
    "debt_folios_crore",
    "hybrid_folios_crore",
    "others_folios_crore"
]

for column in numeric_columns:
    folio_df[column] = pd.to_numeric(
        folio_df[column],
        errors="coerce"
    )

print("\n" + "=" * 60)
print("Data Cleaning Summary")
print("=" * 60)

print("Month converted to datetime.")
print("Numeric columns validated.")
print("Dataset cleaned successfully.")

# ==========================================================
# Save Dataset
# ==========================================================

output_file = PROCESSED_DATA_PATH / "clean_industry_folio_count.csv"

folio_df.to_csv(output_file, index=False)

print(f"\nDataset saved to:\n{output_file}")