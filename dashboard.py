
from pathlib import Path

import pandas as pd
import plotly.express as px
import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Customer Churn Dashboard",
    page_icon="📊",
    layout="wide"
)

# Load the dataset
PROJECT_DIR = Path(__file__).resolve().parent
DATA_PATH = (
    PROJECT_DIR
    / "data"
    / "processed"
    / "customers_clean.csv"
)

st.title("Customer Churn Analysis Dashboard")
st.caption("Explore churn patterns and customer behavior.")

if not DATA_PATH.exists():
    st.error(f"Dataset not found: {DATA_PATH}")
    st.stop()

df = pd.read_csv(DATA_PATH)

required_columns = {
    "customerID", "Churn", "Contract", "MonthlyCharges"
}

missing = required_columns - set(df.columns)

if missing:
    st.error(f"Missing required columns: {sorted(missing)}")
    st.stop()

# Normalize churn labels for consistent calculations
df["Churn"] = df["Churn"].astype(str).str.strip().str.lower()

if not df["Churn"].isin(["yes", "no"]).all():
    st.error("Churn must contain only Yes/No values.")
    st.stop()

df["Churned"] = df["Churn"].eq("yes")

# Sidebar filter
st.sidebar.header("Filters")

contracts = sorted(df["Contract"].dropna().unique().tolist())

selected_contracts = st.sidebar.multiselect(
    "Select contract type",
    options=contracts,
    default=contracts
)

# Filter by contract
filtered_df = df[df["Contract"].isin(selected_contracts)].copy()

# Filter by churn status
churn_filter = st.sidebar.selectbox(
    "Customer Status",
    ["All", "Churned", "Retained"]
)

if churn_filter == "Churned":
    filtered_df = filtered_df[filtered_df["Churned"]]
elif churn_filter == "Retained":
    filtered_df = filtered_df[~filtered_df["Churned"]]

if filtered_df.empty:
    st.warning("No customers match the selected filters.")
    st.stop()

# KPI calculations
total_customers = len(filtered_df)
churned_customers = int(filtered_df["Churned"].sum())
churn_rate = 100 * churned_customers / total_customers

col1, col2, col3 = st.columns(3)

col1.metric("Total Customers", f"{total_customers:,}")
col2.metric("Churned Customers", f"{churned_customers:,}")
col3.metric("Churn Rate", f"{churn_rate:.2f}%")

st.divider()

# Churn rate by contract
contract_summary = (
    filtered_df.groupby("Contract", dropna=False)
    .agg(
        total_customers=("customerID", "size"),
        churned_customers=("Churned", "sum")
    )
    .reset_index()
)

contract_summary["churn_rate_percent"] = (
    100
    * contract_summary["churned_customers"]
    / contract_summary["total_customers"]
)

left, right = st.columns(2)

with left:
    st.subheader("Churn Rate by Contract")

    fig = px.bar(
        contract_summary,
        x="Contract",
        y="churn_rate_percent",
        text="churn_rate_percent",
        labels={
            "Contract": "Contract Type",
            "churn_rate_percent": "Churn Rate (%)"
        },
        title="Percentage of Customers Who Churned"
    )

    fig.update_traces(texttemplate="%{text:.2f}%", textposition="outside")
    fig.update_layout(yaxis_range=[0, 100])
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.subheader("Customer Churn Distribution")

    churn_counts = (
        filtered_df["Churned"]
        .map({True: "Churned", False: "Retained"})
        .value_counts()
        .rename_axis("Customer Status")
        .reset_index(name="Customers")
    )

    fig = px.pie(
        churn_counts,
        names="Customer Status",
        values="Customers",
        title="Churned vs Retained Customers"
    )

    st.plotly_chart(fig, use_container_width=True)

# Data table
st.subheader("Contract Summary")
st.dataframe(contract_summary, use_container_width=True)

st.subheader("Monthly Charges by Customer Status")

charge_summary = (
    filtered_df.groupby("Churned")["MonthlyCharges"]
    .agg(["mean", "median", "count"])
    .reset_index()
)

charge_summary["Customer Status"] = charge_summary["Churned"].map({
    True: "Churned",
    False: "Retained"
})

charge_summary = charge_summary.rename(columns={
    "mean": "Average Monthly Charges",
    "median": "Median Monthly Charges",
    "count": "Customer Count"
})

st.dataframe(
    charge_summary[
        [
            "Customer Status",
            "Customer Count",
            "Average Monthly Charges",
            "Median Monthly Charges"
        ]
    ],
    use_container_width=True
)

st.subheader("Explore Customer Records")
st.dataframe(filtered_df.drop(columns=["Churned"]), use_container_width=True)

st.subheader("Export Your Analysis")

csv_data = filtered_df.drop(
    columns=["Churned"],
    errors="ignore"
).to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Filtered Customers CSV",
    data=csv_data,
    file_name="filtered_customers.csv",
    mime="text/csv"
)
