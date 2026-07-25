import pandas as pd
from pathlib import Path

RAW_DATA_PATH = Path("data/raw")

print("=" * 70)
print("FUND MASTER EXPLORATION")
print("=" * 70)

# Load fund master
df = pd.read_csv(RAW_DATA_PATH / "01_fund_master.csv")

print(f"\n Total skema dana: {len(df)}")

print("\n Unique Fund Houses (Perusahaan Pengelola Dana):")
for house in df["fund_house"].unique():
    print(f"  - {house}")

print("\n Unique Categories:")
for cat in df["category"].unique():
    print(f"  - {cat}")

print("\n Unique Sub-Categories:")
for sub in df["sub_category"].unique():
    print(f"  - {sub}")

print("\n Unique Risk Grades:")
for risk in df["risk_category"].unique():
    print(f"  - {risk}")

print("\n" + "=" * 70)