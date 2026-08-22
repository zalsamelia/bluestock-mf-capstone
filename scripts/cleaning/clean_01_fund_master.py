"""
clean_fund_master.py

Day 2 - Data Cleaning
Dataset: 01_fund_master.csv

This script performs exploratory analysis, data quality
assessment, and basic cleaning on the Fund Master dataset.

Cleaning steps:
- Convert launch_date to datetime
- Standardize text columns
- Remove leading and trailing whitespace
- Save cleaned dataset into processed folder

Input:
data/raw/01_fund_master.csv

Output:
data/processed/clean_fund_master.csv

Project:
Bluestock Mutual Fund Analytics Platform

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

FUND_MASTER_FILE = RAW_DATA_PATH / "01_fund_master.csv"


# ==========================================================
# Load Dataset Function
# ==========================================================

def load_dataset():
    """
    Load fund master dataset with predefined data types.

    Returns
    -------
    pandas.DataFrame
        Loaded fund master dataset.
    """

    return pd.read_csv(
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
# Dataset Inspection Function
# ==========================================================

def inspect_dataset(fund_df):
    """
    Display dataset overview and structure.

    Parameters
    ----------
    fund_df : pandas.DataFrame
        Fund master dataset.

    Returns
    -------
    None
    """

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
# Data Quality Assessment Function
# ==========================================================

def assess_data_quality(fund_df):
    """
    Perform basic data quality checks.

    Parameters
    ----------
    fund_df : pandas.DataFrame
        Fund master dataset.

    Returns
    -------
    None
    """

    print("\n" + "=" * 60)
    print("Missing Values")
    print("=" * 60)

    print(fund_df.isnull().sum())

    print("\n" + "=" * 60)
    print("Duplicate Records")
    print("=" * 60)

    print(
        f"Duplicate Rows : "
        f"{fund_df.duplicated().sum()}"
    )

    print("\n" + "=" * 60)
    print("Fund Houses")
    print("=" * 60)

    print(
        fund_df["fund_house"].value_counts()
    )

    print("\n" + "=" * 60)
    print("Categories")
    print("=" * 60)

    print(
        fund_df["category"].value_counts()
    )

    print("\n" + "=" * 60)
    print("Plans")
    print("=" * 60)

    print(
        fund_df["plan"].value_counts()
    )

    print("\n" + "=" * 60)
    print("Risk Categories")
    print("=" * 60)

    print(
        fund_df["risk_category"].value_counts()
    )


# ==========================================================
# Data Cleaning Function
# ==========================================================

def clean_dataset(fund_df):
    """
    Clean and standardize dataset fields.

    Parameters
    ----------
    fund_df : pandas.DataFrame
        Raw fund master dataset.

    Returns
    -------
    pandas.DataFrame
        Cleaned dataset.
    """

    print("\n" + "=" * 60)
    print("Data Cleaning Process")
    print("=" * 60)

    fund_df["launch_date"] = pd.to_datetime(
        fund_df["launch_date"]
    )

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

        fund_df[column] = (
            fund_df[column]
            .astype(str)
            .str.strip()
        )

    print(
        "✓ Launch date converted to datetime."
    )

    print(
        "✓ Text columns standardized."
    )

    print(
        "✓ Dataset cleaned successfully."
    )

    return fund_df


# ==========================================================
# Save Dataset Function
# ==========================================================

def save_dataset(fund_df):
    """
    Save cleaned dataset to processed folder.

    Parameters
    ----------
    fund_df : pandas.DataFrame
        Cleaned dataset.

    Returns
    -------
    pathlib.Path
        Output file path.
    """

    print("\n" + "=" * 60)
    print("Saving Clean Dataset")
    print("=" * 60)

    output_file = (
        PROCESSED_DATA_PATH /
        "clean_fund_master.csv"
    )

    fund_df.to_csv(
        output_file,
        index=False
    )

    print(
        f"Dataset successfully saved to:\n"
        f"{output_file}"
    )

    return output_file


# ==========================================================
# Main Function
# ==========================================================

def main():
    """
    Execute full fund master cleaning workflow.

    Returns
    -------
    None
    """

    fund_df = load_dataset()

    inspect_dataset(fund_df)

    assess_data_quality(fund_df)

    fund_df = clean_dataset(fund_df)

    save_dataset(fund_df)


# ==========================================================
# Entry Point
# ==========================================================

if __name__ == "__main__":
    main()