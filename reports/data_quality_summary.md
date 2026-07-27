# Data Quality Summary - Day 1
**Project:** Bluestock Fintech Mutual Fund Analytics Capstone
**Author:** Zalsabila Melia
**Date:** July 25, 2026

## Overview
For Day 1, I ingested the 10 provided CSV datasets and fetched the live NAV data for the 6 required schemes using the mfapi.in API. In total, the pipeline processed over 87,000 rows of raw data.

## Validation Checks
I ran a validation check on the AMFI codes across the datasets. All 40 unique scheme codes in the `fund_master` file match perfectly with the codes in `nav_history`. There are no orphan codes or missing mappings, and the column structures for all files match the provided schema documentation.

## Issues to Fix (Day 2 Cleaning)
During the initial ingestion, I noticed a few formatting quirks that need to be cleaned up before analysis:

* **NAV Format (`02_nav_history.csv`):** The `nav` column is currently being read as a string (object) because the numbers contain commas (e.g., "543,856"). I'll need to remove these commas and cast the column to float64 tomorrow.
* **Date Columns:** Most of the date and month columns (like `date`, `launch_date`, `transaction_date`, and `month`) are currently parsed as strings. I'll convert these to proper datetime objects in the cleaning script so they can be sorted and used for time-series analysis.
* **Missing Values (`04_monthly_sip_inflows.csv`):** The `yoy_growth_pct` column has `NaN` values for the first few months of 2022. This is expected since there is no 2021 data to calculate the Year-over-Year growth. I'll handle this during the cleaning phase (likely by dropping or forward-filling).

## Next Steps
The raw data is intact and ready for the next phase. Tomorrow, I'll focus on fixing these type errors and loading the clean data into the SQLite database.