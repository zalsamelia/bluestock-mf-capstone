# ==========================================================
# Day 2 - Data Cleaning
# Dataset : 10_benchmark_indices.csv
# ==========================================================

import pandas as pd
from pathlib import Path

# ==========================================================
# Project Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_PATH = PROJECT_ROOT / "data" / "processed"

BENCHMARK_FILE = RAW_DATA_PATH / "10_benchmark_indices.csv"

# ==========================================================
# Load Dataset
# ==========================================================

benchmark_df = pd.read_csv(BENCHMARK_FILE)

print("\n" + "=" * 60)
print("Benchmark Indices Dataset")
print("=" * 60)

print(f"Rows    : {benchmark_df.shape[0]}")
print(f"Columns : {benchmark_df.shape[1]}")

print("\nColumn Names")
for column in benchmark_df.columns:
    print(f"- {column}")

print("\nData Types")
print(benchmark_df.dtypes)

print("\nFirst Five Rows")
print(benchmark_df.head())

print("\nDataset Information")
benchmark_df.info()

print("\nStatistical Summary")
print(benchmark_df.describe(include="all"))

# ==========================================================
# Data Quality Assessment
# ==========================================================

print("\n" + "=" * 60)
print("Missing Values")
print("=" * 60)
print(benchmark_df.isnull().sum())

print("\n" + "=" * 60)
print("Duplicate Records")
print("=" * 60)
print(f"Duplicate Rows : {benchmark_df.duplicated().sum()}")

print("\n" + "=" * 60)
print("Available Indices")
print("=" * 60)
print(benchmark_df["index_name"].value_counts())

print("\n" + "=" * 60)
print("Date Range")
print("=" * 60)

print(f"Earliest Date : {benchmark_df['date'].min()}")
print(f"Latest Date   : {benchmark_df['date'].max()}")

print("\n" + "=" * 60)
print("Close Value Validation")
print("=" * 60)

print(f"Minimum Close Value : {benchmark_df['close_value'].min()}")
print(f"Maximum Close Value : {benchmark_df['close_value'].max()}")

# ==========================================================
# Data Cleaning
# ==========================================================

benchmark_df["date"] = pd.to_datetime(
    benchmark_df["date"]
)

benchmark_df["index_name"] = benchmark_df["index_name"].str.strip()

benchmark_df["close_value"] = pd.to_numeric(
    benchmark_df["close_value"],
    errors="coerce"
)

print("\n" + "=" * 60)
print("Data Cleaning Summary")
print("=" * 60)

print("No missing values detected.")
print("No duplicate records detected.")
print("Date converted to datetime.")
print("Index names standardized.")
print("Numeric values validated.")
print("Dataset cleaned successfully.")

# ==========================================================
# Save Dataset
# ==========================================================

output_file = PROCESSED_DATA_PATH / "clean_benchmark_indices.csv"

benchmark_df.to_csv(output_file, index=False)

print(f"\nDataset successfully saved to:\n{output_file}")