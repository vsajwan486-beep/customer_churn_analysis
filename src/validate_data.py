
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = (
    PROJECT_DIR
    / "data"
    / "processed"
    / "customers_clean.csv"
)

if not DATA_PATH.exists():
    raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")

df = pd.read_csv(DATA_PATH)

required_columns = [
    "customerID",
    "Churn",
    "Contract",
    "MonthlyCharges"
]

missing_columns = [
    col for col in required_columns
    if col not in df.columns
]

if missing_columns:
    raise ValueError(
        f"Missing required columns: {missing_columns}"
    )

print("DATA QUALITY REPORT")
print("-" * 35)

print(f"Total rows: {len(df)}")
print(f"Total columns: {len(df.columns)}")
print(f"Duplicate rows: {df.duplicated().sum()}")
print(f"Duplicate customer IDs: {df['customerID'].duplicated().sum()}")

print("\nMissing values in required columns:")
print(df[required_columns].isnull().sum())

print("\nChurn values:")
print(df["Churn"].value_counts(dropna=False))

print("\nContract values:")
print(df["Contract"].value_counts(dropna=False))

# Check numeric values
charges = pd.to_numeric(df["MonthlyCharges"], errors="coerce")

print("\nMonthlyCharges values that are missing or non-numeric:")
print(charges.isna().sum())

if not df["Churn"].dropna().astype(str).str.strip().str.lower().isin(
    ["yes", "no"]
).all():
    print("WARNING: Churn contains unexpected values.")

if (charges.dropna() < 0).any():
    print("WARNING: Negative monthly charges found.")

print("\nValidation report completed.")

# Independent churn-rate calculation
churn_normalized = (
    df["Churn"].astype("string").str.strip().str.lower()
)

valid_churn = churn_normalized.isin(["yes", "no"])

if valid_churn.sum() == 0:
    print("Cannot calculate churn rate: no valid churn values.")
else:
    churned = (churn_normalized[valid_churn] == "yes").sum()
    valid_total = valid_churn.sum()
    churn_rate = 100 * churned / valid_total

    print("\nCHURN VALIDATION")
    print(f"Valid churn records: {valid_total}")
    print(f"Churned customers: {churned}")
    print(f"Churn rate: {churn_rate:.2f}%")