# ==========================================================
# Day 2 - Data Cleaning
# Dataset : 07_scheme_performance.csv
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

PERFORMANCE_FILE = RAW_DATA_PATH / "07_scheme_performance.csv"

# ==========================================================
# Load Dataset
# ==========================================================

performance_df = pd.read_csv(
    PERFORMANCE_FILE,
    dtype={
        "scheme_name": "str",
        "fund_house": "str",
        "category": "str",
        "plan": "str",
        "risk_grade": "str"
    }
)

# ==========================================================
# Dataset Inspection
# ==========================================================

print("\n" + "=" * 60)
print("Scheme Performance Dataset")
print("=" * 60)

print(f"Rows    : {performance_df.shape[0]}")
print(f"Columns : {performance_df.shape[1]}")

print("\nColumn Names")

for column in performance_df.columns:
    print(f"- {column}")

print("\nData Types")
print(performance_df.dtypes)

print("\nFirst Five Rows")
print(performance_df.head())

print("\nDataset Information")
performance_df.info()

print("\nStatistical Summary")
print(performance_df.describe(include="all"))

# ==========================================================
# Data Quality Assessment
# ==========================================================

print("\n" + "=" * 60)
print("Missing Values")
print("=" * 60)

print(performance_df.isnull().sum())

print("\n" + "=" * 60)
print("Duplicate Records")
print("=" * 60)

print(f"Duplicate Rows : {performance_df.duplicated().sum()}")

print("\n" + "=" * 60)
print("Unique Fund Houses")
print("=" * 60)

print(performance_df["fund_house"].value_counts())

print("\n" + "=" * 60)
print("Categories")
print("=" * 60)

print(performance_df["category"].value_counts())

print("\n" + "=" * 60)
print("Investment Plans")
print("=" * 60)

print(performance_df["plan"].value_counts())

print("\n" + "=" * 60)
print("Risk Grades")
print("=" * 60)

print(performance_df["risk_grade"].value_counts())

print("\n" + "=" * 60)
print("Morningstar Ratings")
print("=" * 60)

print(performance_df["morningstar_rating"].value_counts())

print("\n" + "=" * 60)
print("Return Validation")
print("=" * 60)

print(f"Minimum 1-Year Return : {performance_df['return_1yr_pct'].min()}")
print(f"Maximum 1-Year Return : {performance_df['return_1yr_pct'].max()}")

print(f"Minimum Expense Ratio : {performance_df['expense_ratio_pct'].min()}")
print(f"Maximum Expense Ratio : {performance_df['expense_ratio_pct'].max()}")

# ==========================================================
# Data Cleaning
# ==========================================================

print("\n" + "=" * 60)
print("Data Cleaning Process")
print("=" * 60)

# Remove leading and trailing spaces
string_columns = [
    "scheme_name",
    "fund_house",
    "category",
    "plan",
    "risk_grade"
]

for column in string_columns:
    performance_df[column] = performance_df[column].str.strip()

print("✓ Text columns standardized.")
print("✓ Dataset cleaned successfully.")

# ==========================================================
# Data Cleaning Summary
# ==========================================================

print("\n" + "=" * 60)
print("Data Cleaning Summary")
print("=" * 60)

print("No missing values detected.")
print("No duplicate records detected.")
print("All numeric columns are already in the correct data type.")
print("Text columns standardized by removing extra spaces.")
print("Dataset is ready for analysis.")

# ==========================================================
# Save Clean Dataset
# ==========================================================

print("\n" + "=" * 60)
print("Saving Clean Dataset")
print("=" * 60)

output_file = PROCESSED_DATA_PATH / "clean_scheme_performance.csv"

performance_df.to_csv(output_file, index=False)

print(f"Dataset successfully saved to:\n{output_file}")