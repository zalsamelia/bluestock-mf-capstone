"""
Load Clean Data into SQLite Database

This script creates the SQLite database schema and loads all
cleaned datasets into the dimensional and fact tables.

Process:
1. Create database schema from schema.sql
2. Remove existing records
3. Load cleaned CSV datasets
4. Create date dimension table
5. Load dimension tables
6. Load fact tables
7. Verify loaded records
8. Display loading summary

Outputs:
- bluestock_mf.db
"""

# ==========================================================
# Import Libraries
# ==========================================================

import sqlite3
import pandas as pd
from pathlib import Path


# ==========================================================
# Project Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

PROCESSED_DATA_PATH = PROJECT_ROOT / "data" / "processed"

SQL_PATH = PROJECT_ROOT / "sql"

DATABASE_PATH = PROJECT_ROOT / "bluestock_mf.db"


# ==========================================================
# Helper Functions
# ==========================================================

def get_table_columns(connection, table_name):
    """
    Return the existing columns of a SQLite table.
    """

    query = f"PRAGMA table_info({table_name})"

    columns = pd.read_sql_query(
        query,
        connection
    )

    return columns["name"].tolist()


def infer_sqlite_type(series):
    """
    Infer a suitable SQLite data type from a pandas Series.
    """

    if pd.api.types.is_integer_dtype(series):
        return "INTEGER"

    if pd.api.types.is_float_dtype(series):
        return "REAL"

    if pd.api.types.is_datetime64_any_dtype(series):
        return "TEXT"

    return "TEXT"


def ensure_table_columns(connection, table_name, dataframe):
    """
    Ensure that all columns from the dataframe exist
    in the corresponding SQLite table.

    Missing columns are automatically added to the table.
    """

    existing_columns = get_table_columns(
        connection,
        table_name
    )

    dataframe_columns = dataframe.columns.tolist()

    missing_columns = [
        column
        for column in dataframe_columns
        if column not in existing_columns
    ]

    if not missing_columns:
        return

    print(
        f"\nAdditional columns detected in {table_name}:"
    )

    for column in missing_columns:

        sql_type = infer_sqlite_type(
            dataframe[column]
        )

        print(
            f"Adding column: {column} ({sql_type})"
        )

        alter_sql = f"""
        ALTER TABLE {table_name}
        ADD COLUMN "{column}" {sql_type}
        """

        connection.execute(alter_sql)

    connection.commit()

    print(
        f"✓ Missing columns added to {table_name}."
    )


def clear_table(connection, table_name):
    """
    Remove existing records from a SQLite table.
    """

    connection.execute(
        f"DELETE FROM {table_name}"
    )


# ==========================================================
# Main Pipeline
# ==========================================================

def main():
    """
    Create SQLite database and load all cleaned datasets.
    """

    print("\n" + "=" * 60)
    print("BLUESTOCK MUTUAL FUND DATABASE LOADER")
    print("=" * 60)


    # ======================================================
    # Connect to SQLite
    # ======================================================

    print("\nConnecting to SQLite database...")

    connection = sqlite3.connect(
        DATABASE_PATH
    )

    print("✓ Database connection established.")


    try:

        # ==================================================
        # Create Database Schema
        # ==================================================

        print("\nCreating database schema...")

        schema_file = SQL_PATH / "schema.sql"

        with open(
            schema_file,
            "r",
            encoding="utf-8"
        ) as file:

            schema_sql = file.read()

        connection.executescript(
            schema_sql
        )

        connection.commit()

        print(
            "✓ Database schema created successfully."
        )


        # ==================================================
        # Load Cleaned CSV Files
        # ==================================================

        print("\nReading cleaned datasets...")

        fund_df = pd.read_csv(
            PROCESSED_DATA_PATH /
            "clean_fund_master.csv"
        )

        nav_df = pd.read_csv(
            PROCESSED_DATA_PATH /
            "clean_nav_history.csv"
        )

        transaction_df = pd.read_csv(
            PROCESSED_DATA_PATH /
            "clean_investor_transactions.csv"
        )

        performance_df = pd.read_csv(
            PROCESSED_DATA_PATH /
            "clean_scheme_performance.csv"
        )

        print("✓ Cleaned datasets loaded.")


        # ==================================================
        # Display Performance Columns
        # ==================================================

        print(
            "\nPerformance dataset columns:"
        )

        for column in performance_df.columns:

            print(
                f"  - {column}"
            )


        # ==================================================
        # Create Date Dimension
        # ==================================================

        print(
            "\nCreating date dimension..."
        )

        nav_dates = pd.to_datetime(
            nav_df["date"],
            errors="coerce"
        )

        transaction_dates = pd.to_datetime(
            transaction_df["transaction_date"],
            errors="coerce"
        )

        fund_dates = pd.to_datetime(
            fund_df["launch_date"],
            errors="coerce"
        )

        all_dates = pd.concat(
            [
                nav_dates,
                transaction_dates,
                fund_dates
            ],
            ignore_index=True
        )

        all_dates = (
            all_dates
            .dropna()
            .drop_duplicates()
            .sort_values()
        )

        dim_date = pd.DataFrame()

        dim_date["date"] = all_dates

        dim_date["year"] = (
            dim_date["date"].dt.year
        )

        dim_date["quarter"] = (
            dim_date["date"].dt.quarter
        )

        dim_date["month"] = (
            dim_date["date"].dt.month
        )

        dim_date["month_name"] = (
            dim_date["date"].dt.month_name()
        )

        dim_date["day"] = (
            dim_date["date"].dt.day
        )

        dim_date["day_name"] = (
            dim_date["date"].dt.day_name()
        )

        # SQLite will store dates as TEXT
        dim_date["date"] = (
            dim_date["date"]
            .dt.strftime("%Y-%m-%d")
        )

        print(
            f"✓ Date dimension created: "
            f"{len(dim_date)} records"
        )


        # ==================================================
        # Prepare Table Structures
        # ==================================================

        print(
            "\nChecking SQLite table structures..."
        )

        ensure_table_columns(
            connection,
            "dim_fund",
            fund_df
        )

        ensure_table_columns(
            connection,
            "dim_date",
            dim_date
        )

        ensure_table_columns(
            connection,
            "fact_nav",
            nav_df
        )

        ensure_table_columns(
            connection,
            "fact_transactions",
            transaction_df
        )

        ensure_table_columns(
            connection,
            "fact_performance",
            performance_df
        )

        print(
            "\n✓ Table structures verified."
        )


        # ==================================================
        # Remove Existing Records
        # ==================================================

        print(
            "\nRemoving existing records..."
        )

        tables_to_clear = [
            "fact_performance",
            "fact_transactions",
            "fact_nav",
            "dim_date",
            "dim_fund"
        ]

        for table in tables_to_clear:

            clear_table(
                connection,
                table
            )

        connection.commit()

        print(
            "✓ Existing records removed."
        )


        # ==================================================
        # Load dim_fund
        # ==================================================

        print(
            "\nLoading dim_fund..."
        )

        fund_df.to_sql(
            "dim_fund",
            connection,
            if_exists="append",
            index=False
        )

        print(
            f"✓ dim_fund loaded: "
            f"{len(fund_df)} records"
        )


        # ==================================================
        # Load dim_date
        # ==================================================

        print(
            "\nLoading dim_date..."
        )

        dim_date.to_sql(
            "dim_date",
            connection,
            if_exists="append",
            index=False
        )

        print(
            f"✓ dim_date loaded: "
            f"{len(dim_date)} records"
        )


        # ==================================================
        # Load fact_nav
        # ==================================================

        print(
            "\nLoading fact_nav..."
        )

        nav_df.to_sql(
            "fact_nav",
            connection,
            if_exists="append",
            index=False
        )

        print(
            f"✓ fact_nav loaded: "
            f"{len(nav_df)} records"
        )


        # ==================================================
        # Load fact_transactions
        # ==================================================

        print(
            "\nLoading fact_transactions..."
        )

        transaction_df.to_sql(
            "fact_transactions",
            connection,
            if_exists="append",
            index=False
        )

        print(
            f"✓ fact_transactions loaded: "
            f"{len(transaction_df)} records"
        )


        # ==================================================
        # Load fact_performance
        # ==================================================

        print(
            "\nLoading fact_performance..."
        )

        performance_df.to_sql(
            "fact_performance",
            connection,
            if_exists="append",
            index=False
        )

        print(
            f"✓ fact_performance loaded: "
            f"{len(performance_df)} records"
        )


        # ==================================================
        # Commit Changes
        # ==================================================

        connection.commit()


        # ==================================================
        # Verify Database
        # ==================================================

        print(
            "\n" + "=" * 60
        )

        print(
            "DATABASE LOADING SUMMARY"
        )

        print(
            "=" * 60
        )

        tables = [
            "dim_fund",
            "dim_date",
            "fact_nav",
            "fact_transactions",
            "fact_performance"
        ]

        for table in tables:

            result = connection.execute(
                f"SELECT COUNT(*) FROM {table}"
            ).fetchone()

            count = result[0]

            print(
                f"{table:<25}: {count:,} records"
            )


        # ==================================================
        # Verify Performance Table Columns
        # ==================================================

        print(
            "\nChecking fact_performance columns..."
        )

        performance_columns = get_table_columns(
            connection,
            "fact_performance"
        )

        print(
            "\nColumns:"
        )

        for column in performance_columns:

            print(
                f"  ✓ {column}"
            )


        # ==================================================
        # Final Message
        # ==================================================

        print(
            "\n" + "=" * 60
        )

        print(
            "DATABASE CREATED SUCCESSFULLY"
        )

        print(
            "=" * 60
        )

        print(
            f"\nDatabase Location:"
        )

        print(
            DATABASE_PATH
        )

        print(
            "\nAll cleaned datasets have been loaded "
            "into SQLite successfully."
        )

    finally:

        # ==================================================
        # Close Connection
        # ==================================================

        connection.close()

        print(
            "\nDatabase connection closed."
        )


# ==========================================================
# Script Entry Point
# ==========================================================

if __name__ == "__main__":
    main()