
import sqlite3
from pathlib import Path

import pandas as pd

# Find the main project directory
PROJECT_DIR = Path(__file__).resolve().parent.parent

CSV_PATH = PROJECT_DIR / "data" / "processed" / "customers_clean.csv"
DB_PATH = PROJECT_DIR / "churn_analysis.db"
OUTPUT_DIR = PROJECT_DIR / "reports" / "sql"

# Check that the data file exists
if not CSV_PATH.exists():
    raise FileNotFoundError(f"Dataset not found: {CSV_PATH}")

# Load cleaned customer data
df = pd.read_csv(CSV_PATH)

# Create database and customers table
with sqlite3.connect(DB_PATH) as connection:
    df.to_sql("customers", connection, if_exists="replace", index=False)

    # Overall churn summary
    overall = pd.read_sql_query("""
        SELECT
            COUNT(*) AS total_customers,
            SUM(
                CASE
                    WHEN LOWER(TRIM(Churn)) = 'yes' THEN 1
                    ELSE 0
                END
            ) AS churned_customers,
            ROUND(
                100.0 * SUM(
                    CASE
                        WHEN LOWER(TRIM(Churn)) = 'yes' THEN 1
                        ELSE 0
                    END
                ) / COUNT(*),
                2
            ) AS churn_rate_percent
        FROM customers;
    """, connection)

    # Churn by contract type
    contract_summary = pd.read_sql_query("""
        SELECT
            Contract,
            COUNT(*) AS total_customers,
            SUM(
                CASE
                    WHEN LOWER(TRIM(Churn)) = 'yes' THEN 1
                    ELSE 0
                END
            ) AS churned_customers,
            ROUND(
                100.0 * SUM(
                    CASE
                        WHEN LOWER(TRIM(Churn)) = 'yes' THEN 1
                        ELSE 0
                    END
                ) / COUNT(*),
                2
            ) AS churn_rate_percent
        FROM customers
        GROUP BY Contract
        ORDER BY churn_rate_percent DESC;
    """, connection)

# Create output directory
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Export results
overall.to_csv(OUTPUT_DIR / "overall_churn.csv", index=False)
contract_summary.to_csv(
    OUTPUT_DIR / "churn_by_contract.csv",
    index=False
)

# Display results
print("\nOVERALL CHURN SUMMARY")
print(overall.to_string(index=False))

print("\nCHURN BY CONTRACT")
print(contract_summary.to_string(index=False))

print("\nReports saved to:", OUTPUT_DIR)
