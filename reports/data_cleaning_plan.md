# Data Cleaning Plan

## Project
Bluestock Mutual Fund Analytics Capstone

## Phase
Day 2 – Data Cleaning & Database Preparation

---

# 1. Objective

The objective of Day 2 is to clean and validate all datasets before loading them into the SQLite database. The cleaned datasets will serve as the primary data source for SQL analysis, dashboard development, and reporting in the following stages of the project.

The cleaning process focuses on improving data quality, ensuring consistency, correcting data types, handling missing values, removing duplicate records, and validating business rules.

---

# 2. Dataset Overview

| No. | Dataset | Status | Notes |
|-----|---------|--------|------|
| 01 | fund_master.csv | Validation Only | Master reference dataset |
| 02 | nav_history.csv | Cleaning Required | Main historical NAV dataset |
| 03 | aum_by_fund_house.csv | Validation Only | AUM summary dataset |
| 04 | monthly_sip_inflows.csv | Cleaning Required | Contains missing YoY values |
| 05 | category_inflows.csv | Validation Only | Category summary dataset |
| 06 | industry_folio_count.csv | Validation Only | Industry statistics |
| 07 | scheme_performance.csv | Cleaning Required | Requires numeric validation |
| 08 | investor_transactions.csv | Cleaning Required | Requires transaction validation |
| 09 | portfolio_holdings.csv | Validation Only | Portfolio allocation dataset |
| 10 | benchmark_indices.csv | Validation Only | Benchmark performance dataset |

---

# 3. Data Cleaning Tasks

## Dataset: nav_history.csv

Issues

- Date column stored as string
- NAV values require numeric validation
- Possible duplicate records
- Missing NAV values
- Invalid NAV values (must be greater than zero)

Cleaning Actions

- Convert date to datetime format
- Convert NAV to numeric
- Remove duplicate records
- Handle missing NAV values using forward fill when appropriate
- Remove invalid NAV values

---

## Dataset: monthly_sip_inflows.csv

Issues

- Missing values in YoY Growth (%)

Cleaning Actions

- Verify whether missing values are expected
- Retain or impute values based on business context
- Validate numeric columns

---

## Dataset: scheme_performance.csv

Issues

- Return columns require numeric validation
- Expense ratio must be within an acceptable range
- Negative Sharpe Ratio should be flagged

Cleaning Actions

- Convert return columns to numeric
- Validate expense ratio values
- Create a flag for negative Sharpe Ratio
- Remove invalid records if necessary

---

## Dataset: investor_transactions.csv

Issues

- Transaction date stored as string
- Inconsistent transaction type naming
- Invalid transaction amounts
- Duplicate transactions
- KYC status validation

Cleaning Actions

- Convert transaction date to datetime
- Standardize transaction type values
- Remove duplicate records
- Filter invalid transaction amounts
- Validate KYC status values

---

## Validation Tasks for Remaining Datasets

The following datasets do not require major cleaning but will be validated for data consistency.

- fund_master.csv
- aum_by_fund_house.csv
- category_inflows.csv
- industry_folio_count.csv
- portfolio_holdings.csv
- benchmark_indices.csv

Validation includes:

- Checking missing values
- Checking duplicate records
- Verifying data types
- Validating numeric columns
- Confirming categorical consistency

---

# 4. Cleaning Priority

The datasets will be cleaned in the following order.

| Priority | Dataset | Reason |
|----------|---------|--------|
| 1 | nav_history.csv | Largest dataset and core source for time-series analysis |
| 2 | investor_transactions.csv | Required for transaction analytics |
| 3 | scheme_performance.csv | Required for fund performance analysis |
| 4 | monthly_sip_inflows.csv | Requires missing value validation |
| 5 | Remaining datasets | Validation and consistency checks |

---

# 5. Output Files

All cleaned datasets will be stored in:

```

data/processed/

```

| Raw Dataset | Output File |
|-------------|------------|
| fund_master.csv | clean_fund_master.csv |
| nav_history.csv | clean_nav_history.csv |
| aum_by_fund_house.csv | clean_aum_by_fund_house.csv |
| monthly_sip_inflows.csv | clean_monthly_sip_inflows.csv |
| category_inflows.csv | clean_category_inflows.csv |
| industry_folio_count.csv | clean_industry_folio_count.csv |
| scheme_performance.csv | clean_scheme_performance.csv |
| investor_transactions.csv | clean_investor_transactions.csv |
| portfolio_holdings.csv | clean_portfolio_holdings.csv |
| benchmark_indices.csv | clean_benchmark_indices.csv |

---

# 6. Expected Deliverables

By the end of Day 2, the following deliverables should be completed:

- Cleaned CSV files stored in `data/processed/`
- SQLite database (`bluestock_mf.db`)
- Database schema (`schema.sql`)
- SQL queries (`queries.sql`)
- Data dictionary (`data_dictionary.md`)
- Git commit with the Day 2 progress

---

# 7. Notes

- The original datasets in `data/raw/` must remain unchanged.
- All cleaning operations must be performed on copies of the original datasets.
- Every cleaning step should be reproducible and documented.
- All cleaned datasets must be validated before loading into SQLite.