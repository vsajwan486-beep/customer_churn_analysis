# Customer Churn Analysis & Prediction

A data analytics and machine learning project that analyzes customer churn patterns and predicts potential customer churn using Python, SQL, and Streamlit.

## Project Overview

This project explores customer data to identify churn patterns, analyze customer segments, and build machine learning models to predict whether customers may leave a service.

## Technologies Used

- **Python** — Pandas, NumPy, Scikit-learn
- **SQL** — SQLite, queries, joins, aggregations
- **Visualization** — Matplotlib, Plotly
- **Dashboard** — Streamlit
- **Tools** — Jupyter Notebook, VS Code, Git, GitHub

## Key Features

- Data cleaning and exploratory data analysis (EDA).
- Customer churn analysis using SQL.
- Logistic Regression and Random Forest classification.
- Model evaluation using accuracy, precision, recall, F1-score, and ROC-AUC.
- Interactive dashboard with customer filters and visualizations.
- Customer churn prediction using a saved machine learning pipeline.

## Project Structure

```text
customer-churn-analysis/
├── data/
├── notebooks/
├── models/
├── reports/
├── src/
├── app.py
├── dashboard.py
├── requirements.txt
└── README.md
```

## Installation and Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/vsajwan486-beep/customer-churn-analysis.git
   cd customer-churn-analysis
   ```

2. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Place the cleaned dataset at the required path:

   `data/processed/customers_clean.csv`

4. Run the dashboard:

   ```bash
   python -m streamlit run dashboard.py
   ```

   To run the prediction app, if configured:

   ```bash
   python -m streamlit run app.py
   ```

## Skills Demonstrated

Python programming, data cleaning, exploratory data analysis, SQL, data visualization, machine learning, model evaluation, dashboard development, and GitHub version control.

## Author

**Vivek Sajwan**

- [GitHub](https://github.com/vsajwan486-beep)
- [LeetCode](https://leetcode.com/u/vivek_sajwan/)
- [HackerRank](https://www.hackerrank.com/vsajwan486/hackos)

*This project was developed for learning and portfolio purposes. Actual results depend on the dataset and model evaluation.*
