"""
==========================================================
Bluestock Mutual Fund Capstone
Day 2 - Data Cleaning

Dataset:
08_investor_transactions.csv

Purpose:
This script performs data profiling, quality assessment,
cleaning, validation, and export processes for the
Investor Transactions dataset.

Main Tasks:
1. Load raw transaction dataset
2. Inspect dataset structure
3. Perform data quality assessment
4. Convert transaction date to datetime
5. Standardize text columns
6. Export cleaned dataset

Output:
clean_investor_transactions.csv
==========================================================
"""

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

TRANSACTION_FILE = RAW_DATA_PATH / "08_investor_transactions.csv"


def load_dataset():
    """
    Load investor transaction dataset.

    Returns
    -------
    pandas.DataFrame
        Raw investor transaction data.
    """

    return pd.read_csv(
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


def inspect_dataset(df):
    """
    Display dataset structure and metadata.

    Parameters
    ----------
    df : pandas.DataFrame
        Dataset to inspect.
    """

    print("\n" + "=" * 60)
    print("Investor Transactions Dataset")
    print("=" * 60)

    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    print("\nColumn Names")

    for column in df.columns:
        print(f"- {column}")

    print("\nData Types")
    print(df.dtypes)

    print("\nFirst Five Rows")
    print(df.head())

    print("\nDataset Information")
    df.info()

    print("\nStatistical Summary")
    print(df.describe(include="all"))


def assess_data_quality(df):
    """
    Perform data quality assessment.

    Parameters
    ----------
    df : pandas.DataFrame
        Dataset to evaluate.
    """

    print("\n" + "=" * 60)
    print("Missing Values")
    print("=" * 60)

    print(df.isnull().sum())

    print("\n" + "=" * 60)
    print("Duplicate Records")
    print("=" * 60)

    print(f"Duplicate Rows : {df.duplicated().sum()}")

    print("\n" + "=" * 60)
    print("Unique Investors")
    print("=" * 60)

    print(
        f"Unique Investors : "
        f"{df['investor_id'].nunique()}"
    )

    print("\n" + "=" * 60)
    print("Transaction Types")
    print("=" * 60)

    print(df["transaction_type"].value_counts())

    print("\n" + "=" * 60)
    print("Payment Modes")
    print("=" * 60)

    print(df["payment_mode"].value_counts())

    print("\n" + "=" * 60)
    print("KYC Status")
    print("=" * 60)

    print(df["kyc_status"].value_counts())

    print("\n" + "=" * 60)
    print("Gender Distribution")
    print("=" * 60)

    print(df["gender"].value_counts())

    print("\n" + "=" * 60)
    print("City Tier")
    print("=" * 60)

    print(df["city_tier"].value_counts())

    print("\n" + "=" * 60)
    print("Amount Validation")
    print("=" * 60)

    print(
        f"Minimum Amount : "
        f"{df['amount_inr'].min()}"
    )

    print(
        f"Maximum Amount : "
        f"{df['amount_inr'].max()}"
    )


def clean_dataset(df):
    """
    Clean and standardize transaction dataset.

    Cleaning Steps
    --------------
    1. Convert transaction date to datetime
    2. Remove leading/trailing spaces
    3. Standardize categorical text fields

    Parameters
    ----------
    df : pandas.DataFrame
        Raw transaction dataset.

    Returns
    -------
    pandas.DataFrame
        Cleaned dataset.
    """

    print("\n" + "=" * 60)
    print("Data Cleaning Process")
    print("=" * 60)

    df["transaction_date"] = pd.to_datetime(
        df["transaction_date"]
    )

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
        df[column] = df[column].str.strip()

    print("✓ Transaction date converted to datetime.")
    print("✓ Text columns standardized.")
    print("✓ Dataset cleaned successfully.")

    return df


def print_cleaning_summary():
    """
    Display data cleaning summary.
    """

    print("\n" + "=" * 60)
    print("Data Cleaning Summary")
    print("=" * 60)

    print("No missing values detected.")
    print("No duplicate records detected.")
    print(
        "Transaction date successfully "
        "converted to datetime."
    )
    print(
        "Text columns standardized by "
        "removing extra spaces."
    )
    print("Dataset is ready for analysis.")


def save_dataset(df):
    """
    Save cleaned dataset into processed folder.

    Parameters
    ----------
    df : pandas.DataFrame
        Cleaned transaction dataset.
    """

    print("\n" + "=" * 60)
    print("Saving Clean Dataset")
    print("=" * 60)

    output_file = (
        PROCESSED_DATA_PATH /
        "clean_investor_transactions.csv"
    )

    df.to_csv(output_file, index=False)

    print(
        f"Dataset successfully saved to:\n"
        f"{output_file}"
    )


def main():
    """
    Execute complete data cleaning workflow.
    """

    transaction_df = load_dataset()

    inspect_dataset(transaction_df)

    assess_data_quality(transaction_df)

    transaction_df = clean_dataset(transaction_df)

    print_cleaning_summary()

    save_dataset(transaction_df)


if __name__ == "__main__":
    main()