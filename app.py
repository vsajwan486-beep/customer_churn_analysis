
import os
import joblib
import pandas as pd
import streamlit as st

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Customer Churn Prediction")
st.write(
    "Enter customer details to estimate their likelihood "
    "of leaving the telecom company."
)

MODEL_PATH = "models/churn_pipeline.joblib"
DATA_PATH = "data/processed/customers_clean.csv"


# -----------------------------
# Load model and reference data
# -----------------------------
@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


@st.cache_data
def load_reference_data():
    return pd.read_csv(DATA_PATH)


if not os.path.exists(MODEL_PATH):
    st.error(f"Model file not found: {MODEL_PATH}")
    st.stop()

if not os.path.exists(DATA_PATH):
    st.error(f"Reference dataset not found: {DATA_PATH}")
    st.stop()

try:
    pipeline = load_model()
    reference_df = load_reference_data()
except Exception as exc:
    st.error(f"Could not load the model or dataset: {exc}")
    st.stop()


# -----------------------------
# Read the trained feature schema
# -----------------------------
preprocessor = pipeline.named_steps["preprocessor"]
expected_columns = list(preprocessor.feature_names_in_)

numeric_columns = []
categorical_columns = []

for name, transformer, columns in preprocessor.transformers_:
    if name == "numeric":
        numeric_columns = list(columns)
    elif name == "categorical":
        categorical_columns = list(columns)

missing_columns = [
    col for col in expected_columns
    if col not in reference_df.columns
]

if missing_columns:
    st.error(
        "The reference dataset is missing required model columns: "
        + ", ".join(missing_columns)
    )
    st.stop()


# -----------------------------
# Customer input form
# -----------------------------
st.subheader("Customer information")

st.caption(
    "The available choices and numerical ranges are based on "
    "the project's reference dataset."
)

customer_input = {}

with st.form("customer_form"):
    col1, col2 = st.columns(2)

    for i, feature in enumerate(expected_columns):
        container = col1 if i % 2 == 0 else col2

        with container:
            series = reference_df[feature].dropna()

            if feature in numeric_columns:
                if series.empty:
                    st.error(
                        f"No reference values available for {feature}."
                    )
                    st.stop()

                values = pd.to_numeric(series, errors="coerce").dropna()

                if values.empty:
                    st.error(
                        f"{feature} is configured as numeric in the "
                        "model but has no numeric reference values. "
                        "Check the preprocessing notebook and retrain "
                        "if the column was incorrectly typed."
                    )
                    st.stop()

                minimum = float(values.min())
                maximum = float(values.max())
                default = float(values.median())

                customer_input[feature] = st.number_input(
                    feature,
                    min_value=minimum,
                    max_value=maximum,
                    value=min(max(default, minimum), maximum),
                    key=f"num_{feature}"
                )

            elif feature in categorical_columns:
                options = sorted(
                    series.astype(str).unique().tolist()
                )

                if not options:
                    st.error(
                        f"No reference categories available for {feature}."
                    )
                    st.stop()

                customer_input[feature] = st.selectbox(
                    feature,
                    options=options,
                    key=f"cat_{feature}"
                )

            else:
                st.error(
                    f"Feature type not supported by this form: {feature}"
                )
                st.stop()

    submitted = st.form_submit_button(
        "Predict Customer Churn",
        type="primary",
        use_container_width=True
    )


# -----------------------------
# Prediction
# -----------------------------
if submitted:
    input_df = pd.DataFrame(
        [customer_input],
        columns=expected_columns
    )

    try:
        prediction = int(pipeline.predict(input_df)[0])
        probabilities = pipeline.predict_proba(input_df)[0]

        # Locate the probability associated with class 1
        classes = list(pipeline.classes_)
        churn_index = classes.index(1)
        churn_probability = float(probabilities[churn_index])

        st.divider()
        st.subheader("Prediction result")

        metric_col1, metric_col2 = st.columns(2)

        metric_col1.metric(
            "Estimated churn probability",
            f"{churn_probability:.1%}"
        )

        metric_col2.metric(
            "Predicted class",
            "Churn" if prediction == 1 else "Stay"
        )

        if prediction == 1:
            st.warning(
                "The model classifies this customer as likely to churn."
            )
        else:
            st.success(
                "The model classifies this customer as likely to stay."
            )

        st.caption(
            "This is a model estimate based on historical data, "
            "not a guarantee or proof of future customer behavior. "
            "The default classification threshold is used."
        )

        with st.expander("View submitted customer information"):
            st.dataframe(input_df, use_container_width=True)

    except Exception as exc:
        st.error(f"Prediction failed: {exc}")
