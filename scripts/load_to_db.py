# ==========================================================
# Day 2 - Load Clean Data into SQLite Database
# ==========================================================

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
# Connect to SQLite Database
# ==========================================================

connection = sqlite3.connect(DATABASE_PATH)

cursor = connection.cursor()

# ==========================================================
# Create Database Schema
# ==========================================================

schema_file = SQL_PATH / "schema.sql"

with open(schema_file, "r", encoding="utf-8") as file:
    schema_sql = file.read()

cursor.executescript(schema_sql)

connection.commit()

print("Database schema created successfully.")

# ==========================================================
# Remove Existing Records
# ==========================================================

print("\nRemoving existing records...")

cursor.execute("DELETE FROM dim_fund")
cursor.execute("DELETE FROM dim_date")
cursor.execute("DELETE FROM fact_nav")
cursor.execute("DELETE FROM fact_transactions")
cursor.execute("DELETE FROM fact_performance")

connection.commit()

print("Done.")

# ==========================================================
# Load Clean CSV Files
# ==========================================================

print("\nReading cleaned datasets...")

fund_df = pd.read_csv(
    PROCESSED_DATA_PATH / "clean_fund_master.csv"
)

nav_df = pd.read_csv(
    PROCESSED_DATA_PATH / "clean_nav_history.csv"
)

transaction_df = pd.read_csv(
    PROCESSED_DATA_PATH / "clean_investor_transactions.csv"
)

performance_df = pd.read_csv(
    PROCESSED_DATA_PATH / "clean_scheme_performance.csv"
)

print("Done.")

# ==========================================================
# Create Date Dimension
# ==========================================================

print("\nCreating date dimension...")

all_dates = pd.concat(
    [
        pd.to_datetime(nav_df["date"]),
        pd.to_datetime(transaction_df["transaction_date"]),
        pd.to_datetime(fund_df["launch_date"])
    ]
)

all_dates = all_dates.drop_duplicates()

all_dates = all_dates.sort_values()

dim_date = pd.DataFrame()

dim_date["date"] = all_dates

dim_date["year"] = dim_date["date"].dt.year

dim_date["quarter"] = dim_date["date"].dt.quarter

dim_date["month"] = dim_date["date"].dt.month

dim_date["month_name"] = dim_date["date"].dt.month_name()

dim_date["day"] = dim_date["date"].dt.day

dim_date["day_name"] = dim_date["date"].dt.day_name()

print("Done.")

# ==========================================================
# Load Dimension Tables
# ==========================================================

print("\nLoading dim_fund...")

fund_df.to_sql(
    "dim_fund",
    connection,
    if_exists="append",
    index=False
)

print("Done.")

print("\nLoading dim_date...")

dim_date.to_sql(
    "dim_date",
    connection,
    if_exists="append",
    index=False
)

print("Done.")

# ==========================================================
# Load Fact Tables
# ==========================================================

print("\nLoading fact_nav...")

nav_df.to_sql(
    "fact_nav",
    connection,
    if_exists="append",
    index=False
)

print("Done.")

print("\nLoading fact_transactions...")

transaction_df.to_sql(
    "fact_transactions",
    connection,
    if_exists="append",
    index=False
)

print("Done.")

print("\nLoading fact_performance...")

performance_df.to_sql(
    "fact_performance",
    connection,
    if_exists="append",
    index=False
)

print("Done.")

connection.commit()

# ==========================================================
# Summary
# ==========================================================

print("\n" + "=" * 60)
print("Database Successfully Created")
print("=" * 60)

print(f"Database Location : {DATABASE_PATH}")

print("\nLoaded Tables")
print("- dim_fund")
print("- dim_date")
print("- fact_nav")
print("- fact_transactions")
print("- fact_performance")

print("\nTotal Records Loaded")
print(f"dim_fund             : {len(fund_df)}")
print(f"dim_date             : {len(dim_date)}")
print(f"fact_nav             : {len(nav_df)}")
print(f"fact_transactions    : {len(transaction_df)}")
print(f"fact_performance     : {len(performance_df)}")

print("\nAll datasets successfully loaded into SQLite.")

# ==========================================================
# Close Database Connection
# ==========================================================

connection.close()

print("Database connection closed.")