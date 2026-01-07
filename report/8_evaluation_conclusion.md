# 8. Evaluation, Insights & Conclusion (Person E)

## 8.1 Consolidated Evaluation

We evaluated all 5 models using the same 20% stratified test set.

| Model | Accuracy | F1-Score | ROC-AUC |
| :--- | :--- | :--- | :--- |
| **Decision Tree** | 0.90 | 0.86 | 0.89 |
| Logistic Regression | 0.94 | 0.92 | 0.97 |
| Random Forest | 0.96 | 0.94 | 0.97 |
| XGBoost | 0.95 | 0.93 | 0.96 |
| MLP | 0.93 | 0.90 | 0.96 |

**Performance Analysis**:
1.Decision Tree (Baseline): Provides a simple, interpretable benchmark. Captures basic patterns but underperforms ensemble models.

2.Logistic Regression: Strong linear model and good for capturing overall trends but may miss nonlinear interactions.

3.Random Forest: Best overall performance. Stable and robust because it able to ensemble and effectively models complex patterns.

4.XGBoost: Slightly lower accuracy than Random Forest but still highly capable and gradient boosting handles complex relationships effectively.

5.MLP (Neural Network): Captures nonlinear relationships, but slightly underperforms tree-based methods. For best results, additional hyperparameter tuning might be necessary.

Overall Insight:
Every model performs better than random guessing, demonstrating that the engineered features offer significant predictive signals. Tree-based ensemble models dominate in accuracy and robustness, while MLP and Logistic Regression serve as strong alternatives depending on interpretability or flexibility requirements.

## 8.2 Business Insights

Based on the machine model evaluation and feature importance analysis, we derived actionable insights to support customer retention and marketing strategies:

| Insight | Feature(s) | Target Customers | Action |
|---------|------------|----------------|--------|
| High-risk customers are more likely to churn | `risk_score` | Customers identified as high-risk | Implement a targeted marketing campaign to address the specific needs of high-risk customers and reduce their likelihood of churning. |
| Positive sentiment is associated with higher retention | `sentiment_score` | Customers with negative or mixed reviews | Monitor customer feedback using sentiment analysis and address negative sentiment promptly to improve retention and marketing outcomes. |
| Spend ratio indicates customer behavior patterns | `spend_ratio` | All customers segmented by spending | Segment customers based on spend ratio and tailor marketing campaigns accordingly. For example, offer high-value promotions to high spenders to encourage continued engagement. |


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
