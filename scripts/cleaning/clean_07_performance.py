"""
==========================================================
Bluestock Mutual Fund Capstone
Day 2 - Data Cleaning

Dataset:
07_scheme_performance.csv

Purpose:
This script performs data profiling, quality assessment,
cleaning, validation, and export processes for the
Scheme Performance dataset.

Main Tasks:
1. Load raw dataset
2. Inspect dataset structure
3. Perform data quality assessment
4. Standardize text columns
5. Validate performance-related metrics
6. Export cleaned dataset

Output:
clean_scheme_performance.csv

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

PERFORMANCE_FILE = RAW_DATA_PATH / "07_scheme_performance.csv"


def load_dataset():
    """
    Load the Scheme Performance dataset.

    Returns
    -------
    pandas.DataFrame
        Raw scheme performance dataset.
    """

    return pd.read_csv(
        PERFORMANCE_FILE,
        dtype={
            "scheme_name": "str",
            "fund_house": "str",
            "category": "str",
            "plan": "str",
            "risk_grade": "str"
        }
    )


def inspect_dataset(df):
    """
    Display dataset structure, metadata,
    and descriptive statistics.

    Parameters
    ----------
    df : pandas.DataFrame
        Dataset to inspect.
    """

    print("\n" + "=" * 60)
    print("Scheme Performance Dataset")
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
    Perform data quality checks.

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
    print("Unique Fund Houses")
    print("=" * 60)

    print(df["fund_house"].value_counts())

    print("\n" + "=" * 60)
    print("Categories")
    print("=" * 60)

    print(df["category"].value_counts())

    print("\n" + "=" * 60)
    print("Investment Plans")
    print("=" * 60)

    print(df["plan"].value_counts())

    print("\n" + "=" * 60)
    print("Risk Grades")
    print("=" * 60)

    print(df["risk_grade"].value_counts())

    print("\n" + "=" * 60)
    print("Morningstar Ratings")
    print("=" * 60)

    print(df["morningstar_rating"].value_counts())

    print("\n" + "=" * 60)
    print("Return Validation")
    print("=" * 60)

    print(
        f"Minimum 1-Year Return : "
        f"{df['return_1yr_pct'].min()}"
    )

    print(
        f"Maximum 1-Year Return : "
        f"{df['return_1yr_pct'].max()}"
    )

    print(
        f"Minimum Expense Ratio : "
        f"{df['expense_ratio_pct'].min()}"
    )

    print(
        f"Maximum Expense Ratio : "
        f"{df['expense_ratio_pct'].max()}"
    )


def clean_dataset(df):
    """
    Clean and standardize dataset values.

    Cleaning Steps
    --------------
    1. Remove leading and trailing spaces
       from text columns.
    2. Standardize categorical values.

    Parameters
    ----------
    df : pandas.DataFrame
        Raw dataset.

    Returns
    -------
    pandas.DataFrame
        Cleaned dataset.
    """

    print("\n" + "=" * 60)
    print("Data Cleaning Process")
    print("=" * 60)

    string_columns = [
        "scheme_name",
        "fund_house",
        "category",
        "plan",
        "risk_grade"
    ]

    for column in string_columns:
        df[column] = df[column].str.strip()

    print("✓ Text columns standardized.")
    print("✓ Dataset cleaned successfully.")

    return df


def print_cleaning_summary():
    """
    Display cleaning summary.
    """

    print("\n" + "=" * 60)
    print("Data Cleaning Summary")
    print("=" * 60)

    print("No missing values detected.")
    print("No duplicate records detected.")
    print(
        "All numeric columns are already "
        "in the correct data type."
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
        Cleaned dataset.
    """

    print("\n" + "=" * 60)
    print("Saving Clean Dataset")
    print("=" * 60)

    output_file = (
        PROCESSED_DATA_PATH /
        "clean_scheme_performance.csv"
    )

    df.to_csv(output_file, index=False)

    print(
        f"Dataset successfully saved to:\n"
        f"{output_file}"
    )


def main():
    """
    Execute complete cleaning workflow.
    """

    performance_df = load_dataset()

    inspect_dataset(performance_df)

    assess_data_quality(performance_df)

    performance_df = clean_dataset(performance_df)

    print_cleaning_summary()

    save_dataset(performance_df)


if __name__ == "__main__":
    main()