"""
Bluestock Mutual Fund Capstone
Day 2 - Data Cleaning

Dataset:
05_category_inflows.csv

Purpose:
This script performs data inspection, data quality assessment,
data cleaning, and exports a cleaned version of the category
inflows dataset for further analysis and dashboard development.

Author: Bluestock Data Analyst Intern
"""

import pandas as pd
from pathlib import Path


# ==========================================================
# Project Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent

RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw"
PROCESSED_DATA_PATH = PROJECT_ROOT / "data" / "processed"

CATEGORY_FILE = RAW_DATA_PATH / "05_category_inflows.csv"


def load_dataset():
    """
    Load category inflows dataset from the raw data folder.

    Returns
    -------
    pandas.DataFrame
        Raw category inflows dataset.
    """
    return pd.read_csv(CATEGORY_FILE)


def inspect_dataset(category_df):
    """
    Display basic dataset information including shape,
    columns, data types, sample records, and summary statistics.

    Parameters
    ----------
    category_df : pandas.DataFrame
        Dataset to inspect.
    """

    print("\n" + "=" * 60)
    print("Category Inflows Dataset")
    print("=" * 60)

    print(f"Rows    : {category_df.shape[0]}")
    print(f"Columns : {category_df.shape[1]}")

    print("\nColumn Names")
    for column in category_df.columns:
        print(f"- {column}")

    print("\nData Types")
    print(category_df.dtypes)

    print("\nFirst Five Rows")
    print(category_df.head())

    print("\nDataset Information")
    category_df.info()

    print("\nStatistical Summary")
    print(category_df.describe(include="all"))


def data_quality_assessment(category_df):
    """
    Perform basic data quality checks such as missing values,
    duplicates, category distribution, and inflow validation.

    Parameters
    ----------
    category_df : pandas.DataFrame
        Dataset to evaluate.
    """

    print("\n" + "=" * 60)
    print("Missing Values")
    print("=" * 60)
    print(category_df.isnull().sum())

    print("\n" + "=" * 60)
    print("Duplicate Records")
    print("=" * 60)
    print(f"Duplicate Rows : {category_df.duplicated().sum()}")

    print("\n" + "=" * 60)
    print("Categories")
    print("=" * 60)
    print(category_df["category"].value_counts())

    print("\n" + "=" * 60)
    print("Net Inflow Validation")
    print("=" * 60)
    print(
        f"Minimum Net Inflow : "
        f"{category_df['net_inflow_crore'].min()}"
    )
    print(
        f"Maximum Net Inflow : "
        f"{category_df['net_inflow_crore'].max()}"
    )


def clean_dataset(category_df):
    """
    Clean category inflows dataset.

    Cleaning Steps:
    --------------
    1. Convert month column to datetime.
    2. Standardize category names.
    3. Convert net inflow values to numeric.

    Parameters
    ----------
    category_df : pandas.DataFrame
        Raw dataset.

    Returns
    -------
    pandas.DataFrame
        Cleaned dataset.
    """

    category_df["month"] = pd.to_datetime(
        category_df["month"]
    )

    category_df["category"] = (
        category_df["category"]
        .astype(str)
        .str.strip()
    )

    category_df["net_inflow_crore"] = pd.to_numeric(
        category_df["net_inflow_crore"],
        errors="coerce"
    )

    print("\n" + "=" * 60)
    print("Data Cleaning Summary")
    print("=" * 60)

    print("Month converted to datetime.")
    print("Category names standardized.")
    print("Numeric values validated.")
    print("Dataset cleaned successfully.")

    return category_df


def save_dataset(category_df):
    """
    Save cleaned dataset into the processed folder.

    Parameters
    ----------
    category_df : pandas.DataFrame
        Cleaned dataset.
    """

    output_file = (
        PROCESSED_DATA_PATH /
        "clean_category_inflows.csv"
    )

    category_df.to_csv(
        output_file,
        index=False
    )

    print(
        f"\nDataset saved to:\n{output_file}"
    )


def main():
    """
    Execute complete category inflows cleaning pipeline.
    """

    category_df = load_dataset()

    inspect_dataset(category_df)

    data_quality_assessment(category_df)

    category_df = clean_dataset(category_df)

    save_dataset(category_df)


if __name__ == "__main__":
    main()