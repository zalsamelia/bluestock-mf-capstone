import requests
import pandas as pd
from pathlib import Path
from datetime import datetime

RAW_DATA_PATH = Path("data/raw")

# List of schemes to fetch as per Day 1 instructions
SCHEMES_TO_FETCH = {
    125497: "HDFC_Top_100_Direct",  
    119551: "SBI_Bluechip",
    120503: "ICICI_Bluechip",
    118632: "Nippon_Large_Cap",
    119092: "Axis_Bluechip",
    120841: "Kotak_Bluechip"
}

print("=" * 30)
print("LIVE NAV FETCH FROM mfapi.in")
print("=" * 30)

for code, name in SCHEMES_TO_FETCH.items():
    print(f"\n Fetching: {name.replace('_', ' ')} (Code: {code})")
    
    try:
        # Call mfapi.in API
        url = f"https://api.mfapi.in/mf/{code}"
        response = requests.get(url, timeout=10)
        response.raise_for_status() # Check for HTTP errors
        
        data = response.json()
        nav_data = data.get("data", [])
        
        if nav_data:
            # Convert to DataFrame
            df = pd.DataFrame(nav_data)
            
            # Clean data slightly: convert date to datetime and sort
            df["date"] = pd.to_datetime(df["date"])
            df = df.sort_values("date", ascending=False).reset_index(drop=True)
            
            # Save as CSV in data/raw folder
            filename = f"live_nav_{code}_{name}.csv"
            filepath = RAW_DATA_PATH / filename
            df.to_csv(filepath, index=False)
            
            print(f"SUCCESS! {len(df)} records saved.")
            print(f"   ↳ Latest NAV: ₹{df.iloc[0]['nav']} (Date: {df.iloc[0]['date'].strftime('%Y-%m-%d')})")
        else:
            print(f"No NAV data found for code {code}.")
            
    except requests.exceptions.RequestException as e:
        print(f"FAILED to fetch data for {name}. Error: {e}")

print("\n" + "=" * 30)
print("LIVE NAV FETCH COMPLETED!")
print("=" * 30)