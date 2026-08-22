# Bluestock Mutual Fund Analytics Platform

![Python](https://img.shields.io/badge/Python-3.11-blue)

![Pandas](https://img.shields.io/badge/Pandas-2.x-orange)

![SQLite](https://img.shields.io/badge/SQLite-Database-blue)

![Power BI](https://img.shields.io/badge/PowerBI-Dashboard-yellow)

![Git](https://img.shields.io/badge/Git-Version%20Control-orange)

### Bluestock Fintech Data Analyst Internship Capstone Project

---

# Project Overview

This project was completed as part of the **Bluestock Fintech Data Analyst Internship Capstone Program**.

The project focuses on building an end-to-end **Mutual Fund Analytics Platform** for analyzing the Indian mutual fund industry. The workflow covers data cleaning, validation, ETL pipeline development, SQLite database construction, SQL analysis, exploratory data analysis, quantitative performance evaluation, business insights, and interactive dashboard development using Power BI.

The platform integrates multiple mutual fund datasets covering fund master information, historical NAV, scheme performance, investor transactions, SIP inflows, category inflows, folios, portfolio holdings, and benchmark market data.

The analysis evaluates mutual fund performance through return, risk, and risk-adjusted performance metrics including:

- 1-Year Return
- 3-Year Return
- 5-Year Return
- Sharpe Ratio
- Sortino Ratio
- Alpha
- Beta
- Standard Deviation
- Maximum Drawdown
- Composite Fund Score

The final project combines analytical outputs with an interactive Power BI dashboard designed using a **Clean Fintech Glassmorphism** visual style.

---

# Project Objectives

The project was developed to achieve the following objectives:

- Clean and preprocess raw mutual fund datasets
- Validate data quality and consistency
- Build a structured SQLite analytical database
- Design a simplified dimensional and fact-based database schema
- Perform SQL-based analytical queries
- Conduct exploratory data analysis
- Analyze historical mutual fund performance
- Calculate 1-Year, 3-Year, and 5-Year returns
- Evaluate risk-adjusted performance using Sharpe Ratio
- Measure downside risk using Sortino Ratio
- Analyze Alpha and Beta against benchmark indices
- Evaluate volatility using Standard Deviation
- Analyze Maximum Drawdown
- Develop a composite fund scoring model
- Rank mutual funds based on performance metrics
- Analyze investor transaction behavior
- Analyze SIP and industry inflow trends
- Develop an interactive Power BI dashboard
- Create a reproducible ETL pipeline
- Document the complete analytical workflow
- Prepare a final analytical report and presentation

---

# Project Workflow

```text
Raw Mutual Fund Data
        │
        ▼
Data Cleaning & Validation
        │
        ▼
Processed CSV Datasets
        │
        ▼
SQLite Database
        │
        ▼
SQL Analysis
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Performance Analytics
        │
        ▼
Business Insights
        │
        ▼
Power BI Dashboard
        │
        ▼
Final Report & Presentation
````

The complete ETL workflow is also automated through a master pipeline script:

```text
run_pipeline.py
       │
       ├── Data Cleaning
       │
       ├── Database Loading
       │
       └── Database Verification
```

---

# Data Sources

The project uses multiple cleaned datasets representing different aspects of the Indian mutual fund industry.

| Dataset                 | Description                                 |
| ----------------------- | ------------------------------------------- |
| Fund Master             | Mutual fund master information              |
| NAV History             | Historical mutual fund NAV data             |
| Scheme Performance      | Fund returns, risk, and performance metrics |
| Investor Transactions   | Investor transaction records                |
| Assets Under Management | Fund-level AUM information                  |
| Monthly SIP Inflows     | Monthly SIP investment trends               |
| Category Inflows        | Net inflow by mutual fund category          |
| Industry Folios         | Mutual fund folio statistics                |
| Portfolio Holdings      | Fund portfolio and security holdings        |
| Benchmark India         | Benchmark market performance data           |

The cleaned datasets are stored inside:

```text
data/processed/
```

---

# Data Cleaning & ETL

The project includes dedicated Python scripts for cleaning and preprocessing the source datasets.

The cleaning workflow covers:

* Column standardization
* Data type conversion
* Missing value handling
* Duplicate checking
* Date normalization
* Numerical validation
* Data consistency validation
* Output generation for analytical use

The cleaning scripts are organized under:

```text
scripts/
└── cleaning/
    ├── clean_01_fund_master.py
    ├── clean_02_nav_history.py
    ├── clean_03_aum.py
    ├── clean_04_sip.py
    ├── clean_05_category.py
    ├── clean_06_folio.py
    ├── clean_07_performance.py
    ├── clean_08_transactions.py
    ├── clean_09_portfolio.py
    └── clean_10_benchmark.py
```

Each production cleaning script has been reviewed and documented with Python docstrings.

---

# Automated ETL Pipeline

A master execution script was created to automate the complete ETL workflow.

The script is located at:

```text
scripts/run_pipeline.py
```

The pipeline executes the following processes:

* Data cleaning
* Database loading
* Database verification

The pipeline uses Python's `subprocess` module to execute each script sequentially. If one step fails, the pipeline stops and reports the failed script.

The complete pipeline can be executed using:

```bash
python scripts/run_pipeline.py
```

A successful execution produces:

```text
============================================================
PIPELINE COMPLETED SUCCESSFULLY
============================================================
```

The database loading and verification process has been successfully tested.

Current verification results include:

```text
dim_fund                  : 40 rows
fact_nav                  : 46000 rows
fact_transactions         : 32778 rows
fact_performance          : 40 rows
```

The SQLite database is generated as:

```text
bluestock_mf.db
```

---

# Database Design

SQLite is used as the analytical database for the project.

The database follows a simplified dimensional and fact-based architecture.

### Dimension Tables

* `dim_fund`
* `dim_date`

### Fact Tables

* `fact_nav`
* `fact_transactions`
* `fact_performance`

The database is designed to support analytical queries while reducing unnecessary data redundancy.

The main relationships are based on:

```text
amfi_code
date
```

The database schema is defined in:

```text
sql/schema.sql
```

---

# Database Verification

A dedicated verification script is used to validate the database after loading.

The script is located at:

```text
scripts/verify_database.py
```

The verification process checks whether the expected analytical tables contain records after the ETL process.

The database verification step is automatically executed by:

```text
scripts/run_pipeline.py
```

This ensures that the ETL workflow does not finish silently when database loading fails.

---

# Exploratory Data Analysis

The exploratory analysis focuses on understanding the characteristics of mutual funds, investor activity, and industry trends.

The EDA includes:

* Data quality assessment
* Missing value analysis
* Duplicate analysis
* Fund category analysis
* Return distribution
* NAV trend analysis
* Risk distribution
* Expense ratio analysis
* Fund house comparison
* Investor transaction analysis
* SIP trend analysis
* Industry trend exploration
* Correlation analysis of performance metrics

The main EDA notebook is located at:

```text
analysis/eda.ipynb
```

EDA outputs and supporting reports are stored under:

```text
analysis/
reports/
```

---

# Performance Analytics

The project includes a dedicated performance analytics workflow based on historical NAV and scheme performance data.

The analysis evaluates mutual funds using multiple financial metrics.

### Return Metrics

* 1-Year Return
* 3-Year Return
* 5-Year Return

### Risk Metrics

* Standard Deviation
* Maximum Drawdown
* Beta

### Risk-Adjusted Metrics

* Sharpe Ratio
* Sortino Ratio

### Benchmark Metrics

* Alpha
* Benchmark Return

### Composite Evaluation

A composite scoring framework is used to combine multiple performance and risk indicators into an overall fund score.

The performance analytics notebook is located at:

```text
analysis/performance_analytics.ipynb
```

Generated analytical outputs include:

```text
analysis/outputs/
├── alpha_beta.csv
├── cagr_summary.csv
├── fund_scorecard.csv
├── maximum_drawdown.csv
├── sharpe_ratio.csv
└── sortino_ratio.csv
```

---

# Business Insights

The analytical workflow is used to identify patterns and insights related to:

* Mutual fund performance
* Risk and return relationships
* Fund category behavior
* Fund house performance
* Benchmark outperformance
* Downside risk
* Investor transaction activity
* SIP growth
* Industry-level asset growth
* Category-level fund inflows

The analysis indicates that higher-return categories can also exhibit higher volatility and downside exposure. Therefore, evaluating funds using return alone may not provide a complete picture of investment performance.

Risk-adjusted metrics such as Sharpe Ratio, Sortino Ratio, Alpha, Beta, and Maximum Drawdown provide additional context when comparing mutual funds.

---
# Power BI Dashboards

The repository contains two Power BI dashboard files developed during the Bluestock Fintech Data Analyst Internship Capstone:

- `dashboard/bluestock_dashboard.pbix` — Initial dashboard developed during the Power BI learning and exploration stage using the cleaned mutual fund datasets.

- `dashboard/bluestock_mf_dashboard.pbix` — Final capstone dashboard developed according to the official Bluestock workspace requirements, covering Industry Overview, Fund Performance, Investor Analytics, and SIP & Market Trends.

The dashboard uses a **Clean Fintech Glassmorphism** design approach.

The visual design focuses on:

* Clean fintech aesthetics
* Premium but minimal interface
* Light background
* Soft borders
* Rounded containers
* Consistent KPI colors
* Recruiter-friendly presentation
* PDF-friendly layout

### Dashboard Color Palette

| Element        | Color     |
| -------------- | --------- |
| Background     | `#F3FBFC` |
| Total AUM      | `#6366F1` |
| SIP Inflows    | `#22D3EE` |
| Folios         | `#10B981` |
| Schemes        | `#F59E0B` |
| Primary Text   | `#0F172A` |
| Secondary Text | `#64748B` |
| Border         | `#D8EDF3` |
| Shadow         | `#79D4E4` |
| Header Accent  | `#22D3EE` |

---

# Dashboard Page 1 — Industry Overview

The first dashboard page focuses on an overview of the Indian mutual fund industry.

The page contains four main KPI cards:

* Total AUM
* SIP Inflows
* Folios
* Schemes

The page also includes:

* Industry AUM Trend
* AUM by AMC
* Key Takeaways

The dashboard layout was designed using a 16:9 canvas with a structured KPI and analytical visualization layout.

The main KPI measures were created in Power BI using DAX based on the available cleaned datasets.

For example, Total AUM is calculated from fund-level AUM data, while SIP Inflows are calculated from monthly SIP inflow data.

Investor Folios are evaluated from investor identifiers, and Scheme counts are based on unique mutual fund schemes.

---

# Dashboard Page 2 — Fund Performance

The Fund Performance page is designed to evaluate mutual fund performance and risk.

The planned visualizations include:

* Return vs Risk Scatter Plot
* Fund Scorecard Table
* NAV vs Benchmark Trend
* Fund House slicer
* Category slicer
* Plan slicer

The scatter plot compares:

```text
X-axis = Return
Y-axis = Risk / Standard Deviation
Bubble Size = AUM
```

This allows funds to be evaluated based on the relationship between performance, risk, and asset size.

---

# Dashboard Page 3 — Investor Analytics

The Investor Analytics page focuses on investor behavior and transaction activity.

The planned visualizations include:

* Transaction Amount by State
* SIP vs Lumpsum vs Redemption
* Age Group vs Average SIP Amount
* Monthly Transaction Volume

Interactive filters include:

* State
* Age Group
* City Tier

This page provides a behavioral view of mutual fund investors and their transaction patterns.

---

# Dashboard Page 4 — SIP & Market Trends

The SIP and Market Trends page focuses on industry-level investment activity and market movement.

The visualizations include:

* SIP Inflow Bar Chart
* Nifty 50 Line Chart
* Category Inflow Heatmap
* Top 5 Categories by Net Inflow for FY25

The primary analysis period covers:

```text
2022–2025
```

The page is designed to compare SIP investment trends against broader market movements.

---

# Dashboard Interactivity

The dashboard design includes interactive analytical features such as:

* Fund-level filtering
* Category filtering
* Plan filtering
* State filtering
* Age group filtering
* City tier filtering
* Tooltips
* Drill-through functionality
* NAV detail analysis

A planned drill-through workflow allows users to move from fund-level performance analysis to detailed NAV information.

---

# Published Power BI Dashboard

The Power BI dashboard has also been published for online viewing.

### Power BI Dashboard

[https://app.powerbi.com/view?r=eyJrIjoiZTZjZWQ3NzItMjJiZC00YTNkLThlOWYtYTdjYmIxMjM0NjU2IiwidCI6IjkwYWZmZTBmLWMyYTMtNDEwOC1iYjk4LTZjZWI0ZTk0ZWYxNSIsImMiOjEwfQ%3D%3D]
---

# Dashboard Files

The Power BI dashboard file is stored under:

```text
dashboard/
├── bluestock_mf_dashboard.pbix
├── bluestock_dashboard.pbix
└── dashboard_preview.png
```

The primary Power BI project file is:

```text
dashboard/bluestock_mf_dashboard.pbix

---

# Final Report

A final analytical report is being prepared as part of the Bluestock capstone deliverables.

The report follows the required structure:

### Executive Summary

Provides a concise overview of the project, objectives, methodology, and major findings.

### Data Sources

Documents the datasets used in the analysis and their respective purposes.

### ETL Design

Explains the data cleaning, transformation, database loading, and validation workflow.

### EDA Findings

Presents the main findings obtained during exploratory data analysis.

### Performance Analysis

Discusses mutual fund returns, risk, benchmark comparison, and risk-adjusted performance metrics.

### Dashboard Screenshots

Documents the Power BI dashboard pages and their analytical purpose.

### Limitations

Discusses limitations related to data availability, historical coverage, assumptions, and analytical methodology.

### Recommendations

Provides recommendations based on the analytical findings.

The target report length is:

```text
15–20 pages
```

---

# Presentation

A 12-slide presentation is prepared to communicate the project results in a concise business-oriented format.

The presentation structure includes:

```text
Title
Problem & Objective
Data Sources
Architecture
EDA Highlights
EDA Highlights
Performance Metrics
Performance Metrics
Dashboard Screenshot
Dashboard Screenshot
Key Findings
Thank You
```

The presentation is designed to summarize the analytical workflow, key findings, performance analysis, and dashboard results.

---

# Python Code Quality

The Python scripts have been cleaned and prepared for final submission.

Code improvements include:

* Adding module-level docstrings
* Adding function docstrings
* Removing unnecessary debug output
* Organizing imports
* Organizing project paths
* Structuring the ETL workflow
* Creating a centralized pipeline runner
* Adding error handling for pipeline execution

The master pipeline is:

```text
scripts/run_pipeline.py
```

This script provides a single entry point for executing the ETL workflow.

---

# Project Structure

```text
bluestock-mf-capstone/

│
├── analysis/
│   ├── eda.ipynb
│   ├── performance_analytics.ipynb
│   ├── visualization.ipynb
│   ├── figures/
│   └── outputs/
│       ├── alpha_beta.csv
│       ├── cagr_summary.csv
│       ├── fund_scorecard.csv
│       ├── maximum_drawdown.csv
│       ├── sharpe_ratio.csv
│       └── sortino_ratio.csv
│
├── dashboard/
│   ├── bluestock_mf_dashboard.pbix
│   ├── bluestock_dashboard.pbix
│   └── dashboard_preview.png
│
├── data/
│   ├── raw/
│   └── processed/
│
├── reports/
│   ├── business_insights.md
│   ├── data_cleaning_plan.md
│   ├── data_cleaning_report.md
│   ├── data_dictionary.md
│   ├── data_quality_summary.md
│   └── eda_report.md
│
├── scripts/
│   ├── cleaning/
│   │   ├── clean_01_fund_master.py
│   │   ├── clean_02_nav_history.py
│   │   ├── clean_03_aum.py
│   │   ├── clean_04_sip.py
│   │   ├── clean_05_category.py
│   │   ├── clean_06_folio.py
│   │   ├── clean_07_performance.py
│   │   ├── clean_08_transactions.py
│   │   ├── clean_09_portfolio.py
│   │   └── clean_10_benchmark.py
│   │
│   ├── load_to_db.py
│   ├── verify_database.py
│   └── run_pipeline.py
│
├── sql/
│   └── schema.sql
│
├── .gitignore
├── requirements.txt
├── README.md
└── bluestock_mf.db
```

---

# Tech Stack

The project uses the following technologies:

* Python 3.11
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* Scikit-learn
* SQLite
* SQL
* Jupyter Notebook
* Power BI
* Git
* GitHub

---

# How to Run

### Clone Repository

```bash
git clone https://github.com/<your_username>/bluestock-mf-capstone.git

cd bluestock-mf-capstone
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Complete ETL Pipeline

The recommended method is to execute the master pipeline:

```bash
python scripts/run_pipeline.py
```

The pipeline automatically executes:

```text
Data Cleaning
      ↓
Database Loading
      ↓
Database Verification
```

### Build SQLite Database

The database can also be generated directly using:

```bash
python scripts/load_to_db.py
```

### Verify Database

Run:

```bash
python scripts/verify_database.py
```

### Run SQL Analysis

```bash
python scripts/run_query.py
```

### Run Exploratory Data Analysis

Open:

```text
analysis/eda.ipynb
```

and run the notebook cells.

### Run Performance Analytics

Open:

```text
analysis/performance_analytics.ipynb
```

The notebook calculates:

* Historical Returns
* Sharpe Ratio
* Sortino Ratio
* Alpha
* Beta
* Maximum Drawdown
* Composite Fund Score

### Run Visualization

Open:

```text
analysis/visualization.ipynb
```

The notebook generates the analytical visualizations used for business insights.

### Open Power BI Dashboard

Open:

```text
dashboard/bluestock_mf_dashboard.pbix
```

using Power BI Desktop.

---

# Final Deliverables

The final Bluestock Mutual Fund Analytics project is designed to deliver:

* `Final_Report.pdf`
* `Bluestock_MF_Presentation.pptx`
* `bluestock_mf_dashboard.pbix`
* `Dashboard.pdf`
* Four Power BI dashboard screenshots
* Clean Python ETL scripts
* `run_pipeline.py`
* `README.md`
* SQLite analytical database
* SQL schema and analytical queries
* Cleaned datasets
* EDA outputs
* Performance analytics outputs
* Business insights
* GitHub repository

---

# GitHub Versioning

The final project repository is intended to be versioned using Git.

The final release tag is:

```text
v1.0
```

The final commit message is:

```text
Final: Complete Bluestock MF Capstone
```

The final repository should contain the complete analytical workflow, documentation, dashboard files, scripts, and supporting project outputs.

---

# Limitations

Several limitations should be considered when interpreting the results.

The analysis depends on the datasets provided for the project and therefore does not represent the complete Indian mutual fund market.

Historical AUM, SIP, investor, and performance data may have different levels of granularity and coverage.

Some industry-level metrics may not have the same historical structure as fund-level data.

The performance analysis is based on historical observations and should not be interpreted as a guarantee of future investment performance.

The composite fund score is an analytical framework developed for this project and should not be considered a formal investment recommendation.

---

# Future Improvements

Possible future enhancements include:

* Portfolio optimization using Modern Portfolio Theory
* CAPM-based investment analysis
* Monte Carlo portfolio simulation
* Machine learning-based fund recommendation
* Time-series forecasting for NAV prediction
* Automated scheduled ETL execution
* Power BI Service automation
* Real-time market data integration
* Advanced investor segmentation
* Portfolio risk simulation
* Automated data quality monitoring

---

# Self-Review Checklist

Before final submission, the project should be reviewed against the following checklist:

* All required datasets are available
* Data cleaning scripts execute successfully
* ETL pipeline executes successfully
* SQLite database loads successfully
* Database verification completes successfully
* SQL analysis runs without errors
* EDA notebooks run successfully
* Performance analytics run successfully
* Business insights are documented
* Power BI dashboard loads correctly
* Dashboard visualizations are complete
* Dashboard theme is consistent
* Dashboard screenshots are exported
* Final PDF report is complete
* 12-slide presentation is complete
* Python scripts contain appropriate documentation
* `run_pipeline.py` executes the complete ETL workflow
* README documentation is complete
* GitHub repository is organized
* Final Git tag `v1.0` is created

---

# Author

**Zalsabilah Rezky Amelia Arep**

Data Analyst Intern

Bluestock Fintech Internship Capstone Project

---

# Acknowledgements

This project was developed as part of the **Bluestock Fintech Data Analyst Internship Capstone Program**.

The project integrates data engineering, data analysis, quantitative performance evaluation, business intelligence, and data visualization into an end-to-end mutual fund analytics platform.

````

```text
https://github.com/zalsamelia>/bluestock-mf-capstone.git
````
