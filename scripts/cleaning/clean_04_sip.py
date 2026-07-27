# ==========================================================
# Day 2 - Data Cleaning
# Dataset : 04_monthly_sip_inflows.csv
# ==========================================================

import pandas as pd
from pathlib import Path

# ==========================================================
# Project Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_PATH = PROJECT_ROOT / "data" / "processed"

SIP_FILE = RAW_DATA_PATH / "04_monthly_sip_inflows.csv"

# ==========================================================
# Load Dataset
# ==========================================================

sip_df = pd.read_csv(SIP_FILE)

print("\n" + "=" * 60)
print("Monthly SIP Inflows Dataset")
print("=" * 60)

print(f"Rows    : {sip_df.shape[0]}")
print(f"Columns : {sip_df.shape[1]}")

print("\nColumn Names")
for column in sip_df.columns:
    print(f"- {column}")

print("\nData Types")
print(sip_df.dtypes)

print("\nFirst Five Rows")
print(sip_df.head())

print("\nDataset Information")
sip_df.info()

print("\nStatistical Summary")
print(sip_df.describe(include="all"))

# ==========================================================
# Data Quality Assessment
# ==========================================================

print("\n" + "=" * 60)
print("Missing Values")
print("=" * 60)
print(sip_df.isnull().sum())

print("\n" + "=" * 60)
print("Duplicate Records")
print("=" * 60)
print(f"Duplicate Rows : {sip_df.duplicated().sum()}")

print("\n" + "=" * 60)
print("Month Range")
print("=" * 60)
print(f"Earliest Month : {sip_df['month'].min()}")
print(f"Latest Month   : {sip_df['month'].max()}")

print("\n" + "=" * 60)
print("SIP Inflow Validation")
print("=" * 60)
print(f"Minimum SIP Inflow : {sip_df['sip_inflow_crore'].min()}")
print(f"Maximum SIP Inflow : {sip_df['sip_inflow_crore'].max()}")

# ==========================================================
# Data Cleaning
# ==========================================================

sip_df["month"] = pd.to_datetime(sip_df["month"])

numeric_columns = [
    "sip_inflow_crore",
    "active_sip_accounts_crore",
    "new_sip_accounts_lakh",
    "sip_aum_lakh_crore",
    "yoy_growth_pct"
]

for column in numeric_columns:
    sip_df[column] = pd.to_numeric(sip_df[column], errors="coerce")

print("\n" + "=" * 60)
print("Data Cleaning Summary")
print("=" * 60)

print("Month converted to datetime.")
print("Numeric columns validated.")
print("Dataset cleaned successfully.")

# ==========================================================
# Save Dataset
# ==========================================================

output_file = PROCESSED_DATA_PATH / "clean_monthly_sip_inflows.csv"

sip_df.to_csv(output_file, index=False)

print(f"\nDataset saved to:\n{output_file}")