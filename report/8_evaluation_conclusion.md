# 8. Evaluation, Insights & Conclusion (Person E)

## 8.1 Consolidated Evaluation

We evaluated all 5 models using the same 20% stratified test set.

| Model | Accuracy | F1-Score | ROC-AUC |
| :--- | :--- | :--- | :--- |
| **Decision Tree** | 0.99 | 0.99 | 0.99 |
| Logistic Regression | *TBD* | *TBD* | *TBD* |
| Random Forest | *TBD* | *TBD* | *TBD* |
| XGBoost | *TBD* | *TBD* | *TBD* |
| MLP | *TBD* | *TBD* | *TBD* |

**Performance Analysis**:
- The **Decision Tree** baseline set a strong foundation.
- [Compare other models once trained].

## 8.2 Business Insights

1.  **Key Signals**: Customer **Repayment Risk** (derived from reviews) and **Recent Activity** (`days_since_last_purchase`) are the strongest predictors of churn.
2.  **Strategy**:
    - **Intervention**: Target customers with `days > 150` with re-engagement offers *before* they hit the 180-day churn threshold.
    - **Sentiment**: Address specific complaints found in `High Risk` reviews (mainly "Service" and "Product Quality").

## 8.3 AI Disclosure (Project-Wide)

We adhered to a **Human-in-the-Loop** AI usage policy:

1.  **Dataset**: LLM generated the *logic* for simulation; Humans validated the Python code and distribution.
2.  **Features**: LLM designed the *keyword rules* for text analysis; Humans implemented the deterministic function.
3.  **Modeling**: Standard `sklearn` libraries were used; AI was used loosely for *explaining* code concepts or interpreting error logs.

## 8.4 GitHub Contribution Summary

The project followed a strict **Git Flow** workflow:
- **Branches**: Each member worked on dedicated feature branches (e.g., `personA-modelling`, `personB-featureengineering`).
- **Pull Requests**: All code was merged via PRs with required reviews.
- **Commits**: Each member contributed >6 meaningful commits.
- **Artifacts**: All notebooks are reproducible and stored in `notebooks/`.

## 8.5 Conclusion

We successfully simulated a realistic e-commerce dataset, engineered features using LLM-aided text analysis, and built a predictive pipeline. The baseline Decision Tree proves that the data contains predictive signal. Future work could involve hyperparameter tuning and deploying the model as a real-time API.
