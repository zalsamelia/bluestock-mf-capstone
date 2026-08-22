"""
verify_database.py

SQLite Database Verification Script.

This script performs a basic validation of the Bluestock
Mutual Fund SQLite database by checking whether the main
tables exist and displaying their total row counts.

Purpose:
- Verify successful database creation
- Confirm data loading completion
- Validate ETL output before dashboard development
- Support final project quality assurance

Tables Verified:
- dim_fund
- fact_nav
- fact_transactions
- fact_performance

Database:
bluestock_mf.db

Project:
Bluestock Mutual Fund Analytics Platform

"""

# ==========================================================
# Import Libraries
# ==========================================================

import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

# ==========================================================
# Project Paths
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATABASE_PATH = PROJECT_ROOT / "bluestock_mf.db"


# ==========================================================
# Tables to Verify
# ==========================================================

TABLES = [
    "dim_fund",
    "fact_nav",
    "fact_transactions",
    "fact_performance",
]


# ==========================================================
# Database Verification Function
# ==========================================================

def verify_database():
    """
    Verify database connectivity and table row counts.

    The function connects to the SQLite database and
    retrieves the total number of records from each
    key table.

    Returns
    -------
    None

    Prints verification results directly to console.
    """

    # ------------------------------------------------------
    # Connect to SQLite Database
    # ------------------------------------------------------

    engine = create_engine(
        f"sqlite:///{DATABASE_PATH}"
    )

    print("=" * 60)
    print("BLUESTOCK DATABASE VERIFICATION")
    print("=" * 60)

    # ------------------------------------------------------
    # Verify Each Table
    # ------------------------------------------------------

    for table in TABLES:

        try:

            query = (
                f"SELECT COUNT(*) AS total_rows "
                f"FROM {table}"
            )

            count = pd.read_sql(
                query,
                engine
            )

            print(
                f"{table:<25} : "
                f"{count.iloc[0, 0]} rows"
            )

        except Exception as error:

            print(
                f"{table:<25} : "
                f"ERROR -> {error}"
            )

    print("=" * 60)
    print("Verification Finished")


# ==========================================================
# Main Function
# ==========================================================

def main():
    """
    Execute database verification process.

    Returns
    -------
    None
    """

    verify_database()


# ==========================================================
# Entry Point
# ==========================================================

if __name__ == "__main__":
    main()