# ==========================================================
# Verify SQLite Database
# ==========================================================

import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

# ==========================================================
# Project Path
# ==========================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATABASE_PATH = PROJECT_ROOT / "bluestock_mf.db"

# ==========================================================
# Connect SQLite
# ==========================================================

engine = create_engine(f"sqlite:///{DATABASE_PATH}")

# ==========================================================
# Tables to Verify
# ==========================================================

tables = [
    "dim_fund",
    "fact_nav",
    "fact_transactions",
    "fact_performance",
]

print("=" * 60)
print("BLUESTOCK DATABASE VERIFICATION")
print("=" * 60)

for table in tables:
    try:
        query = f"SELECT COUNT(*) AS total_rows FROM {table}"
        count = pd.read_sql(query, engine)

        print(f"{table:<25} : {count.iloc[0,0]} rows")

    except Exception as e:
        print(f"{table:<25} : ERROR -> {e}")

print("=" * 60)
print("Verification Finished")