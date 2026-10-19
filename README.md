# Customer Churn Analysis & Prediction

## Project Overview

This project analyzes customer churn in a telecommunications dataset and builds a machine learning model to estimate whether a customer is likely to leave the company.

The project combines data cleaning, exploratory data analysis, visualization, machine learning, model evaluation, and an interactive Streamlit application.

## Technologies Used

- Python
- Pandas and NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook

## Project Features

- Data cleaning and preprocessing
- Exploratory data analysis and visualizations
- Customer churn prediction using classification models
- Model evaluation using accuracy, precision, recall, F1-score, and ROC-AUC
- Feature importance analysis
- Saved preprocessing and prediction pipeline
- Interactive Streamlit application

## Project Structure

- `app.py` — Streamlit application
- `data/` — Dataset files
- `notebooks/` — Analysis and machine learning notebooks
- `models/` — Saved machine learning pipeline
- `reports/` — Analysis reports and visualizations
- `requirements.txt` — Python dependencies

## Installation and Usage

1. Clone or download this repository.
2. Create and activate a Python virtual environment.
3. Install the dependencies:

   `python -m pip install -r requirements.txt`

4. Start the application:

   `python -m streamlit run app.py`

5. Open the local URL displayed in the terminal.

## Model Evaluation

The project evaluates the model using multiple classification metrics rather than relying on accuracy alone.

- Accuracy:0.759
- Precision:0.351
- Recall:0.775
- F1-score:0.63
- ROC-AUC:0.841

## Limitations

The model learns patterns from historical data. Its predictions are estimates and do not establish the causes of customer churn.

Performance on future customers may differ from performance on the evaluation dataset. The application is a portfolio demonstration, not a production-ready customer retention system.

## Future Improvements

- Cross-validation and hyperparameter tuning
- Improved probability calibration and decision-threshold selection
- Additional model evaluation
- Deployment of the Streamlit application
- Monitoring of model performance on new data

## Author

Vivek Sajwan
