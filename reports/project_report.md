# Customer Churn Analysis — Project Findings

## 1. Project Overview

This project analyzes customer churn using the IBM Telco Customer Churn dataset. The objective is to identify patterns associated with customer churn and understand which customer groups may require additional retention efforts.

The analysis uses Python, Pandas, Matplotlib, and Seaborn to clean data, calculate churn rates, compare customer groups, and create visualizations.

## 2. Overall Customer Churn

The standard IBM Telco Customer Churn dataset contains 7,043 customers, of whom 1,869 churned. This corresponds to an overall churn rate of approximately 26.5%.

**Finding:** Approximately one in four customers left the company.

**Business implication:** Customer churn can reduce recurring revenue and increase the cost of acquiring replacement customers. Understanding churn patterns can help the business develop more effective retention strategies.

## 3. Churn by Contract Type

**Finding:** Customers with month-to-month contracts typically have higher churn rates than customers with one-year or two-year contracts.

**Business implication:** The company could investigate whether contract flexibility, targeted retention offers, or incentives for longer-term commitments improve customer retention.

## 4. Churn by Customer Tenure

**Finding:** Customers who churn tend to have shorter tenures than customers who remain with the company.

**Business implication:** The early customer lifecycle may be an important period for retention efforts. The company could investigate onboarding quality, service issues, and early customer satisfaction.

## 5. Churn by Monthly Charges

**Finding:** Customers who churn tend to have higher monthly charges on average than customers who stay.

**Business implication:** The company should investigate pricing, perceived value, and service quality to understand whether these factors are associated with customer churn. Higher monthly charges alone do not prove that price causes churn.

## 6. Churn by Payment Method

**Finding:** Customers using electronic checks typically exhibit higher churn rates than customers using automatic bank transfers or credit card payments.

**Business implication:** The company could investigate payment convenience and customer preferences, and test whether encouraging automatic payments improves retention.

## 7. Churn by Internet Service

**Finding:** Fiber-optic customers commonly exhibit higher churn rates than DSL customers in the standard dataset.

**Business implication:** The company should investigate service quality, pricing, customer expectations, and support experience before deciding on retention interventions.

## 8. Churn by Online Security

**Finding:** Customers without online security services often have higher churn rates than customers who have these services.

**Business implication:** The company could evaluate whether security education, improved service access, or relevant service bundles improve customer satisfaction and retention.

## 9. Churn by Tech Support

**Finding:** Customers without tech support services commonly have higher churn rates than customers who have these services.

**Business implication:** The company could investigate whether improved technical support access and service quality are associated with better retention.

## 10. Churn by Senior-Citizen Status

**Finding:** Senior citizens typically have a higher churn rate than non-senior customers in the standard dataset.

**Business implication:** The company could investigate differences in customer needs and experiences to identify opportunities for better service and retention.

## 11. Churn by Partner and Dependent Status

**Finding:** Customers without partners or dependents commonly show higher churn rates than customers who have them.

**Business implication:** Household characteristics may be associated with different retention patterns. These relationships should be investigated alongside contract type, tenure, and service usage rather than treated as direct causes of churn.

## 12. Churn by Gender

**Finding:** Male and female customers generally have relatively similar churn rates compared with the differences commonly observed across contract type and tenure.

**Business implication:** The company should prioritize variables that demonstrate stronger and more consistent relationships with churn in the actual analysis.

## 13. Key Business Recommendations

Based on the patterns identified in the exploratory analysis, the following actions could be investigated:

1. **Improve early customer retention:** Review onboarding, early support, and customer satisfaction for newer customers.
2. **Evaluate contract incentives:** Test whether appropriate longer-term contract offers improve retention.
3. **Investigate pricing concerns:** Examine the relationship between monthly charges, service packages, and churn.
4. **Improve payment convenience:** Evaluate whether automatic payment options are associated with improved retention.
5. **Review internet service quality:** Investigate customer satisfaction, pricing, and support among fiber-optic customers.
6. **Evaluate additional services:** Study whether online security and tech support services are associated with improved retention.
7. **Measure results:** Track churn rates over time and evaluate proposed interventions before implementing them broadly.

These are potential actions to investigate, not proven solutions.

## 14. Limitations of the Analysis

* The analysis is based on the available dataset and may not represent every telecom business.
* Observed relationships do not establish causation.
* Customer churn patterns may change over time.
* Additional statistical analysis or predictive modeling may be needed to estimate churn risk reliably.
* Business recommendations should be tested before implementation.

## 15. Final Conclusion

The exploratory analysis of the IBM Telco Customer Churn dataset helps identify customer groups associated with higher churn rates. Common patterns include higher churn among month-to-month customers, customers with shorter tenure, customers paying higher monthly charges, and customers using electronic checks.

These findings suggest that retention efforts could focus on improving the early customer experience, investigating pricing and service concerns, and evaluating appropriate contract and payment options.

The analysis demonstrates how data analytics can transform customer data into useful business insights. However, the findings should be validated using the project's actual calculations and visualizations. Further analysis and controlled experiments can help determine which interventions genuinely improve customer retention.

## 16. Tools and Technologies Used

* Python
* Pandas
* Matplotlib
* Seaborn
* Jupyter Notebook

## 17. Project Outcome

This project demonstrates practical skills in data cleaning, exploratory data analysis, churn-rate calculation, data visualization, business interpretation, and communicating analytical findings. It provides a foundation for future work in customer churn prediction and data-driven decision-making.



## Feature Importance and Model Explainability

### Objective
The objective of this analysis is to identify which customer characteristics contribute most to the Random Forest model's churn predictions.

### Methodology
I examined the model's built-in feature importance scores and used permutation importance with ROC-AUC scoring to assess how shuffling individual transformed features affected predictive performance.

### Key Findings
- The highest-ranked feature in the model was: [insert your actual feature].
- Another important feature was: [insert your actual feature].
- The permutation importance analysis showed that: [describe your actual results].

### Business Implications
The results can help the company identify customer characteristics associated with elevated churn risk and prioritize further investigation or retention experiments.

### Limitations
Feature importance indicates predictive usefulness, not causation. The analysis uses historical customer data, and the model's findings should be validated before being used to make business decisions.
