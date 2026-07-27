# Data Dictionary

## Bluestock Fintech Internship

### Day 2 – SQLite Database Documentation

---

# Overview

This document describes the database structure used in the Bluestock Mutual Fund Analytics project. It provides an explanation of each table, the purpose of every column, the corresponding data types, and the relationships between tables.

The database was created after completing the data cleaning process and follows a Star Schema design to support analytical queries and dashboard development.

---

# Database Tables

The SQLite database consists of five tables:

- dim_fund
- dim_date
- fact_nav
- fact_transactions
- fact_performance

---

# 1. dim_fund

**Source File**

`clean_fund_master.csv`

**Overview**

This table contains the master information for every mutual fund scheme. It is used as the main reference table across the database and is linked to multiple fact tables through the AMFI code.

| Column | Data Type | Description | Constraint |
|---------|-----------|-------------|------------|
| amfi_code | INTEGER | Unique AMFI code assigned to each mutual fund scheme | Primary Key |
| fund_house | TEXT | Asset management company offering the scheme | |
| scheme_name | TEXT | Mutual fund scheme name | |
| category | TEXT | Primary fund category | |
| sub_category | TEXT | Detailed category of the scheme | |
| plan | TEXT | Investment plan (Direct or Regular) | |
| launch_date | DATE | Date when the scheme was launched | |
| benchmark | TEXT | Benchmark index used to evaluate fund performance | |
| expense_ratio_pct | REAL | Annual expense ratio (%) | |
| exit_load_pct | REAL | Exit load charged upon redemption (%) | |
| min_sip_amount | INTEGER | Minimum SIP investment amount | |
| min_lumpsum_amount | INTEGER | Minimum lump sum investment amount | |
| fund_manager | TEXT | Name of the fund manager | |
| risk_category | TEXT | Overall investment risk level | |
| sebi_category_code | TEXT | SEBI category classification code | |

---

# 2. dim_date

**Source**

Generated from all unique dates available in the cleaned datasets.

**Overview**

This table stores calendar information used for date-based analysis and reporting.

| Column | Data Type | Description | Constraint |
|---------|-----------|-------------|------------|
| date | DATE | Calendar date | Primary Key |
| year | INTEGER | Year | |
| quarter | INTEGER | Quarter of the year | |
| month | INTEGER | Month number | |
| month_name | TEXT | Full month name | |
| day | INTEGER | Day of the month | |
| day_name | TEXT | Day of the week | |

---

# 3. fact_nav

**Source File**

`clean_nav_history.csv`

**Overview**

This table records the daily Net Asset Value (NAV) of each mutual fund scheme.

| Column | Data Type | Description | Constraint |
|---------|-----------|-------------|------------|
| amfi_code | INTEGER | Mutual fund identifier | Foreign Key → dim_fund |
| date | DATE | NAV observation date | Foreign Key → dim_date |
| nav | REAL | Daily Net Asset Value | |

---

# 4. fact_transactions

**Source File**

`clean_investor_transactions.csv`

**Overview**

This table stores investor transaction records, including investment details and investor information.

| Column | Data Type | Description | Constraint |
|---------|-----------|-------------|------------|
| investor_id | TEXT | Unique investor identifier | |
| transaction_date | DATE | Date of transaction | Foreign Key → dim_date |
| amfi_code | INTEGER | Mutual fund identifier | Foreign Key → dim_fund |
| transaction_type | TEXT | Type of transaction (SIP, Lumpsum, Redemption) | |
| amount_inr | REAL | Transaction amount in Indian Rupees | |
| state | TEXT | Investor state | |
| city | TEXT | Investor city | |
| city_tier | TEXT | City classification (T30 or B30) | |
| age_group | TEXT | Investor age group | |
| gender | TEXT | Investor gender | |
| annual_income_lakh | REAL | Annual income (Lakhs INR) | |
| payment_mode | TEXT | Payment method | |
| kyc_status | TEXT | KYC verification status | |

---

# 5. fact_performance

**Source File**

`clean_scheme_performance.csv`

**Overview**

This table contains fund performance indicators and risk measurements used for evaluating mutual fund performance.

| Column | Data Type | Description | Constraint |
|---------|-----------|-------------|------------|
| amfi_code | INTEGER | Mutual fund identifier | Foreign Key → dim_fund |
| scheme_name | TEXT | Mutual fund scheme name | |
| fund_house | TEXT | Asset management company | |
| category | TEXT | Fund category | |
| plan | TEXT | Investment plan | |
| return_1yr_pct | REAL | One-year return (%) | |
| return_3yr_pct | REAL | Three-year return (%) | |
| return_5yr_pct | REAL | Five-year return (%) | |
| benchmark_3yr_pct | REAL | Three-year benchmark return (%) | |
| alpha | REAL | Alpha value | |
| beta | REAL | Beta value | |
| sharpe_ratio | REAL | Sharpe Ratio | |
| sortino_ratio | REAL | Sortino Ratio | |
| std_dev_ann_pct | REAL | Annualized standard deviation (%) | |
| max_drawdown_pct | REAL | Maximum drawdown (%) | |
| aum_crore | INTEGER | Assets Under Management (Crore INR) | |
| expense_ratio_pct | REAL | Expense ratio (%) | |
| morningstar_rating | INTEGER | Morningstar rating (1–5) | |
| risk_grade | TEXT | Overall risk classification | |

---

# Table Relationships

The database follows a Star Schema design.

- `dim_fund` is connected to `fact_nav`, `fact_transactions`, and `fact_performance` through the `amfi_code` column.
- `dim_date` is connected to `fact_nav` using the `date` column and to `fact_transactions` using the `transaction_date` column.

This design reduces data redundancy and makes analytical queries more efficient.

---

# Notes

The database was built using the cleaned datasets generated during the data cleaning stage. Date fields were converted to datetime format where applicable, numerical columns were validated, and text fields were standardized before loading the data into SQLite.

The original datasets remain in the `data/raw` directory, while the cleaned datasets are stored in `data/processed`. The SQLite database created for this project is named `bluestock_mf.db`.