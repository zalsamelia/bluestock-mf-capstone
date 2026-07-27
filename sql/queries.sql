-- ==========================================================
-- Bluestock Mutual Fund Analytics
-- Day 2
-- SQL Analytical Queries
-- ==========================================================
-- =====================================================

-- Query 1
-- Top 5 Funds by Assets Under Management (AUM)
-- =====================================================
SELECT
    scheme_name,
    fund_house,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- =====================================================
-- Query 2
-- Lowest Expense Ratio
-- =====================================================

SELECT
    scheme_name,
    fund_house,
    expense_ratio_pct
FROM fact_performance
ORDER BY expense_ratio_pct ASC
LIMIT 5;

-- =====================================================
-- Query 3
-- Top Sharpe Ratio
-- =====================================================
SELECT
    scheme_name,
    sharpe_ratio,
    risk_grade
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- =====================================================
-- Query 4
-- Average 3-Year Return
-- =====================================================
SELECT

    category,

    ROUND(AVG(return_3yr_pct),2) AS average_return

FROM fact_performance

GROUP BY category

ORDER BY average_return DESC;

-- =====================================================
-- Query 5
-- Transactions by State
-- =====================================================
SELECT

    state,

    COUNT(*) AS total_transactions

FROM fact_transactions

GROUP BY state

ORDER BY total_transactions DESC;

-- =====================================================
-- Query 6
-- Average Investment by Age Group
-- =====================================================
SELECT

    age_group,

    ROUND(AVG(amount_inr),2) AS average_investment

FROM fact_transactions

GROUP BY age_group

ORDER BY average_investment DESC;

-- =====================================================
-- Query 7
-- Investor Distribution
-- =====================================================
SELECT

    city_tier,

    COUNT(*) AS total_transactions

FROM fact_transactions

GROUP BY city_tier;

-- =====================================================
-- Query 8
-- Monthly Transaction Volume
-- =====================================================
SELECT

    strftime('%Y-%m', transaction_date) AS month,

    COUNT(*) AS total_transactions

FROM fact_transactions

GROUP BY month

ORDER BY month;

-- =====================================================
-- Query 9
-- Average NAV by Fund
-- =====================================================
SELECT

    d.scheme_name,

    ROUND(AVG(f.nav),2) AS average_nav

FROM fact_nav f

JOIN dim_fund d

ON f.amfi_code = d.amfi_code

GROUP BY d.scheme_name

ORDER BY average_nav DESC;

-- =====================================================
-- Query 10
-- Fund Outperformance
-- =====================================================
SELECT

    scheme_name,

    return_3yr_pct,

    benchmark_3yr_pct,

    ROUND(return_3yr_pct - benchmark_3yr_pct,2) AS excess_return

FROM fact_performance

ORDER BY excess_return DESC;
