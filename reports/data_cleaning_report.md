# Data Cleaning Report

## Bluestock Fintech Internship

### Day 2 – Data Cleaning

## Overview

The objective of this task was to inspect and clean all datasets provided for the Bluestock Mutual Fund Analytics project before moving to the exploratory data analysis stage. Each dataset was reviewed individually to identify potential data quality issues and ensure that the information was consistent, properly formatted, and ready for further analysis.

To preserve data integrity, the original datasets stored in the `data/raw` directory were left unchanged. All cleaned datasets were exported separately to the `data/processed` directory.

---

# Dataset Cleaning Summary

## 01. Fund Master

The Fund Master dataset serves as the primary reference table for all mutual fund schemes used throughout the project. During the cleaning process, the dataset structure, column names, and data types were inspected. Missing values and duplicate records were checked, while categorical columns such as fund house, category, plan, benchmark, fund manager, and risk category were standardized by removing unnecessary whitespace. The `launch_date` column was converted into the datetime format to improve compatibility for future analysis.

The cleaned dataset was exported as:

`clean_fund_master.csv`

---

## 02. NAV History

The NAV History dataset contains the daily Net Asset Value of each mutual fund scheme. The cleaning process focused on validating AMFI codes, reviewing date values, and ensuring NAV values could be interpreted correctly as numerical data. Date values were converted into datetime format, while NAV values were transformed into numeric values after removing formatting characters. Duplicate records and missing values were also verified before exporting the cleaned dataset.

The cleaned dataset was exported as:

`clean_nav_history.csv`

---

## 03. AUM by Fund House

This dataset records the Assets Under Management (AUM) of each fund house over different reporting periods. During cleaning, the dataset structure was validated, date values were converted into datetime format, and fund house names were standardized to improve consistency. Numeric columns were also verified to ensure they contained valid numerical values.

The cleaned dataset was exported as:

`clean_aum_by_fund_house.csv`

---

## 04. Monthly SIP Inflows

The Monthly SIP Inflows dataset provides monthly statistics related to Systematic Investment Plan (SIP) investments. The month column was converted into datetime format, while all numerical columns were validated to ensure they were stored using appropriate numeric data types. Missing values and duplicate records were reviewed before the cleaned dataset was generated.

The cleaned dataset was exported as:

`clean_monthly_sip_inflows.csv`

---

## 05. Category Inflows

This dataset summarizes monthly net inflows across different mutual fund categories. During cleaning, category names were standardized, the month column was converted into datetime format, and net inflow values were validated as numeric data. Basic quality checks confirmed that the dataset contained no duplicate records requiring removal.

The cleaned dataset was exported as:

`clean_category_inflows.csv`

---

## 06. Industry Folio Count

The Industry Folio Count dataset contains quarterly statistics regarding the number of investor folios across different fund segments. The cleaning process included validating numerical columns, converting the reporting month into datetime format, and checking for missing values and duplicate observations. No significant inconsistencies were identified.

The cleaned dataset was exported as:

`clean_industry_folio_count.csv`

---

## 07. Scheme Performance

This dataset contains historical performance indicators for each mutual fund scheme, including returns, alpha, beta, Sharpe ratio, Sortino ratio, and risk measurements. During cleaning, all performance metrics were validated as numeric values, categorical fields were reviewed for consistency, and duplicate records were checked. Since the dataset was already well structured, only minor formatting improvements were required.

The cleaned dataset was exported as:

`clean_scheme_performance.csv`

---

## 08. Investor Transactions

The Investor Transactions dataset records individual investment activities. The cleaning process focused on validating transaction dates, transaction types, payment methods, investor demographics, KYC status, and investment amounts. Categorical fields were reviewed for consistency, while numerical columns were confirmed to contain valid values. Duplicate transactions and missing values were also inspected before exporting the cleaned dataset.

The cleaned dataset was exported as:

`clean_investor_transactions.csv`

---

## 09. Portfolio Holdings

This dataset contains the stock holdings of each mutual fund portfolio. During cleaning, portfolio dates were converted into datetime format, stock information was standardized by trimming unnecessary whitespace, and financial columns such as portfolio weight, market value, and current price were validated as numeric values. Basic quality checks confirmed that no duplicate records or missing values required additional handling.

The cleaned dataset was exported as:

`clean_portfolio_holdings.csv`

---

## 10. Benchmark Indices

The Benchmark Indices dataset stores historical closing values for several market indices used as performance benchmarks. During cleaning, the date column was converted into datetime format, index names were standardized, and closing values were validated as numeric data. Missing values and duplicate records were inspected to ensure the dataset was suitable for subsequent analysis.

The cleaned dataset was exported as:

`clean_benchmark_indices.csv`

---

# Overall Result

The data cleaning phase was completed successfully for all ten datasets. Throughout the process, each dataset was inspected for missing values, duplicate records, inconsistent formatting, and incorrect data types. Date columns were converted into datetime objects where applicable, numerical fields were validated, and text columns were standardized to improve consistency.

The original datasets remain unchanged in the `data/raw` directory, while the cleaned versions have been stored in `data/processed`. These processed datasets provide a reliable foundation for the next phase of the project, which focuses on exploratory data analysis and dashboard development.

---

# Conclusion

Day 2 focused on improving data quality across all project datasets before moving to the analysis stage. Each dataset was successfully inspected, cleaned, and validated by handling data types, formatting inconsistencies, duplicate records, and missing values where applicable.

All cleaned datasets were exported to the `data/processed` directory while preserving the original files in `data/raw`. This approach ensures data integrity, supports reproducibility, and provides a reliable foundation for the upcoming exploratory data analysis, SQL queries, and dashboard development tasks.