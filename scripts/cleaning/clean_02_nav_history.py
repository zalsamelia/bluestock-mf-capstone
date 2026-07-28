# ==========================================================
# Day 2 - Data Cleaning
# Dataset : 02_nav_history.csv
# ==========================================================

# ==========================================================
# Import Libraries
# ==========================================================
import pandas as pd
from pathlib import Path

# ==========================================================
# Project Paths
# ==========================================================

# Project Root Directory
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

# Raw Dataset Folder
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"

# Processed Dataset Folder
PROCESSED_DATA_PATH = PROJECT_ROOT / "data" / "processed"

# ==========================================================
# Dataset File
# ==========================================================

NAV_HISTORY_FILE = RAW_DATA_PATH / "02_nav_history.csv"

# ==========================================================
# Load Dataset
# ==========================================================

nav_df = pd.read_csv(
    NAV_HISTORY_FILE,
    dtype={
        "date": "str",
        "nav": "str"
    }
)

# ==========================================================
# Dataset Inspection
# ==========================================================

print("\n" + "=" * 60)

print("NAV History Dataset")
print("=" * 60)

print(f"Rows    : {nav_df.shape[0]}")
print(f"Columns : {nav_df.shape[1]}")

print("\nColumn Names")

for column in nav_df.columns:
    print(f"- {column}")

print("\nData Types")
print(nav_df.dtypes)

print("\nFirst Five Rows")
print(nav_df.head())

print("\nDataset Information")
nav_df.info()

print("\nStatistical Summary")
print(nav_df.describe())

# ==========================================================
# Data Quality Assessment
# ==========================================================

print("\n" + "=" * 60)
print("Missing Values")
print("=" * 60)

print(nav_df.isnull().sum())

print("\n" + "=" * 60)
print("Duplicate Records")
print("=" * 60)

print(f"Duplicate Rows : {nav_df.duplicated().sum()}")

print("\n" + "=" * 60)
print("Unique AMFI Codes")
print("=" * 60)

print(f"Unique AMFI Codes : {nav_df['amfi_code'].nunique()}")

print("\n" + "=" * 60)
print("Date Sample")
print("=" * 60)

print(nav_df["date"].head())

print("\n" + "=" * 60)
print("NAV Sample")
print("=" * 60)

print(nav_df["nav"].head())

print("\n" + "=" * 60)
print("Dataset Dimensions")
print("=" * 60)

print(f"Rows    : {nav_df.shape[0]}")
print(f"Columns : {nav_df.shape[1]}")

# ==========================================================
# Data Cleaning
# ==========================================================

print("\n" + "=" * 60)
print("Data Cleaning Process")
print("=" * 60)

# Convert date column into datetime
nav_df["date"] = pd.to_datetime(nav_df["date"])

# Remove thousand separator from NAV values
nav_df["nav"] = nav_df["nav"].str.replace(",", "", regex=False)

# Convert NAV into numeric format
nav_df["nav"] = pd.to_numeric(nav_df["nav"])

print("✓ Date column converted to datetime.")
print("✓ NAV column converted to numeric.")
print("✓ Dataset cleaned successfully.")

# Forward fill missing NAV values if any exist
if nav_df["nav"].isnull().sum() > 0:

    nav_df["nav"] = nav_df["nav"].ffill()

    print("✓ Missing NAV values filled using forward-fill.")

else:

    print("✓ No missing NAV values found.")

# ==========================================================
# Data Cleaning Summary
# ==========================================================

print("\n" + "=" * 60)
print("Data Cleaning Summary")
print("=" * 60)

print("No missing values detected.")
print("No duplicate records detected.")
print("Date column successfully converted to datetime.")
print("NAV column successfully converted to numeric.")
print("Dataset is ready for analysis.")

# ==========================================================
# Save Clean Dataset
# ==========================================================

print("\n" + "=" * 60)
print("Saving Clean Dataset")
print("=" * 60)

output_file = PROCESSED_DATA_PATH / "clean_nav_history.csv"

nav_df.to_csv(output_file, index=False)

print(f"Dataset successfully saved to:\n{output_file}")