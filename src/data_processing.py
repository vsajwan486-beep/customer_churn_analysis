
import pandas as pd


def clean_customer_data(df: pd.DataFrame) -> pd.DataFrame:
    """Return a cleaned copy of customer data."""

    # Work on a copy so the original DataFrame is preserved.
    cleaned = df.copy()

    # Remove unnecessary spaces from column names.
    cleaned.columns = cleaned.columns.str.strip()

    # Convert TotalCharges to numeric if the column exists.
    if "TotalCharges" in cleaned.columns:
        cleaned["TotalCharges"] = pd.to_numeric(
            cleaned["TotalCharges"].astype("string").str.strip(),
            errors="coerce"
        )

    # Remove exact duplicate rows only after reviewing the audit.
    cleaned = cleaned.drop_duplicates()

    return cleaned