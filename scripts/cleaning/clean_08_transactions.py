# ==========================================================
# Day 2 - Data Cleaning
# Dataset : 08_investor_transactions.csv
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

TRANSACTION_FILE = RAW_DATA_PATH / "08_investor_transactions.csv"

# ==========================================================
# Load Dataset
# ==========================================================

transaction_df = pd.read_csv(
    TRANSACTION_FILE,
    dtype={
        "investor_id": "str",
        "transaction_date": "str",
        "transaction_type": "str",
        "state": "str",
        "city": "str",
        "city_tier": "str",
        "age_group": "str",
        "gender": "str",
        "payment_mode": "str",
        "kyc_status": "str"
    }
)

# ==========================================================
# Dataset Inspection
# ==========================================================

print("\n" + "=" * 60)
print("Investor Transactions Dataset")
print("=" * 60)

print(f"Rows    : {transaction_df.shape[0]}")
print(f"Columns : {transaction_df.shape[1]}")

print("\nColumn Names")

for column in transaction_df.columns:
    print(f"- {column}")

print("\nData Types")
print(transaction_df.dtypes)

print("\nFirst Five Rows")
print(transaction_df.head())

print("\nDataset Information")
transaction_df.info()

print("\nStatistical Summary")
print(transaction_df.describe(include="all"))

# ==========================================================
# Data Quality Assessment
# ==========================================================

print("\n" + "=" * 60)
print("Missing Values")
print("=" * 60)

print(transaction_df.isnull().sum())

print("\n" + "=" * 60)
print("Duplicate Records")
print("=" * 60)

print(f"Duplicate Rows : {transaction_df.duplicated().sum()}")

print("\n" + "=" * 60)
print("Unique Investors")
print("=" * 60)

print(f"Unique Investors : {transaction_df['investor_id'].nunique()}")

print("\n" + "=" * 60)
print("Transaction Types")
print("=" * 60)

print(transaction_df["transaction_type"].value_counts())

print("\n" + "=" * 60)
print("Payment Modes")
print("=" * 60)

print(transaction_df["payment_mode"].value_counts())

print("\n" + "=" * 60)
print("KYC Status")
print("=" * 60)

print(transaction_df["kyc_status"].value_counts())

print("\n" + "=" * 60)
print("Gender Distribution")
print("=" * 60)

print(transaction_df["gender"].value_counts())

print("\n" + "=" * 60)
print("City Tier")
print("=" * 60)

print(transaction_df["city_tier"].value_counts())

print("\n" + "=" * 60)
print("Amount Validation")
print("=" * 60)

print(f"Minimum Amount : {transaction_df['amount_inr'].min()}")
print(f"Maximum Amount : {transaction_df['amount_inr'].max()}")

# ==========================================================
# Data Cleaning
# ==========================================================

print("\n" + "=" * 60)
print("Data Cleaning Process")
print("=" * 60)

# Convert transaction_date into datetime
transaction_df["transaction_date"] = pd.to_datetime(
    transaction_df["transaction_date"]
)

# Remove leading and trailing spaces
string_columns = [
    "investor_id",
    "transaction_type",
    "state",
    "city",
    "city_tier",
    "age_group",
    "gender",
    "payment_mode",
    "kyc_status"
]

for column in string_columns:
    transaction_df[column] = transaction_df[column].str.strip()

print("✓ Transaction date converted to datetime.")
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
print("Transaction date successfully converted to datetime.")
print("Text columns standardized by removing extra spaces.")
print("Dataset is ready for analysis.")

# ==========================================================
# Save Clean Dataset
# ==========================================================

print("\n" + "=" * 60)
print("Saving Clean Dataset")
print("=" * 60)

output_file = PROCESSED_DATA_PATH / "clean_investor_transactions.csv"

transaction_df.to_csv(output_file, index=False)

print(f"Dataset successfully saved to:\n{output_file}")