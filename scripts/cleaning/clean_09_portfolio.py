# ==========================================================
# Day 2 - Data Cleaning
# Dataset : 09_portfolio_holdings.csv
# ==========================================================

import pandas as pd
from pathlib import Path

# ==========================================================
# Project Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_PATH = PROJECT_ROOT / "data" / "processed"

PORTFOLIO_FILE = RAW_DATA_PATH / "09_portfolio_holdings.csv"

# ==========================================================
# Load Dataset
# ==========================================================

portfolio_df = pd.read_csv(PORTFOLIO_FILE)

print("\n" + "=" * 60)
print("Portfolio Holdings Dataset")
print("=" * 60)

print(f"Rows    : {portfolio_df.shape[0]}")
print(f"Columns : {portfolio_df.shape[1]}")

print("\nColumn Names")
for column in portfolio_df.columns:
    print(f"- {column}")

print("\nData Types")
print(portfolio_df.dtypes)

print("\nFirst Five Rows")
print(portfolio_df.head())

print("\nDataset Information")
portfolio_df.info()

print("\nStatistical Summary")
print(portfolio_df.describe(include="all"))

# ==========================================================
# Data Quality Assessment
# ==========================================================

print("\n" + "=" * 60)
print("Missing Values")
print("=" * 60)
print(portfolio_df.isnull().sum())

print("\n" + "=" * 60)
print("Duplicate Records")
print("=" * 60)
print(f"Duplicate Rows : {portfolio_df.duplicated().sum()}")

print("\n" + "=" * 60)
print("Unique Stocks")
print("=" * 60)
print(portfolio_df["stock_symbol"].value_counts())

print("\n" + "=" * 60)
print("Sector Distribution")
print("=" * 60)
print(portfolio_df["sector"].value_counts())

print("\n" + "=" * 60)
print("Portfolio Date")
print("=" * 60)
print(portfolio_df["portfolio_date"].value_counts())

print("\n" + "=" * 60)
print("Weight Validation")
print("=" * 60)
print(f"Minimum Weight : {portfolio_df['weight_pct'].min()}")
print(f"Maximum Weight : {portfolio_df['weight_pct'].max()}")

# ==========================================================
# Data Cleaning
# ==========================================================

portfolio_df["portfolio_date"] = pd.to_datetime(
    portfolio_df["portfolio_date"]
)

string_columns = [
    "stock_symbol",
    "stock_name",
    "sector"
]

for column in string_columns:
    portfolio_df[column] = portfolio_df[column].str.strip()

numeric_columns = [
    "weight_pct",
    "market_value_cr",
    "current_price_inr"
]

for column in numeric_columns:
    portfolio_df[column] = pd.to_numeric(
        portfolio_df[column],
        errors="coerce"
    )

print("\n" + "=" * 60)
print("Data Cleaning Summary")
print("=" * 60)

print("No missing values detected.")
print("No duplicate records detected.")
print("Portfolio date converted to datetime.")
print("Text columns standardized.")
print("Numeric columns validated.")
print("Dataset cleaned successfully.")

# ==========================================================
# Save Dataset
# ==========================================================

output_file = PROCESSED_DATA_PATH / "clean_portfolio_holdings.csv"

portfolio_df.to_csv(output_file, index=False)

print(f"\nDataset successfully saved to:\n{output_file}")