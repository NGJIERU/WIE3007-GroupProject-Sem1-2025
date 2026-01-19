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

**Notes**:
- Decision Tree is easy to interpret but not as accurate as the others.
- Logistic Regression works well as a simple baseline.
- Random Forest has the best scores overall.
- XGBoost is close behind Random Forest.
- MLP works but needs more tuning to match tree-based models.

All models beat random guessing, so our features are useful for prediction.

## 8.2 Business Insights

Based on our results, here are some practical takeaways:

| Insight | Feature(s) | Target Customers | Action |
|---------|------------|----------------|--------|
| High-risk customers are more likely to churn | `risk_score` | Customers identified as high-risk | Implement a targeted marketing campaign to address the specific needs of high-risk customers and reduce their likelihood of churning. |
| Positive sentiment is associated with higher retention | `sentiment_score` | Customers with negative or mixed reviews | Monitor customer feedback using sentiment analysis and address negative sentiment promptly to improve retention and marketing outcomes. |
| Spend ratio indicates customer behavior patterns | `spend_ratio` | All customers segmented by spending | Segment customers based on spend ratio and tailor marketing campaigns accordingly. For example, offer high-value promotions to high spenders to encourage continued engagement. |


## 8.3 Tools Used

We used standard Python libraries (pandas, sklearn, xgboost) for modeling. For text feature extraction, we wrote keyword-matching functions based on common sentiment words.

## 8.4 GitHub Contribution Summary

We used Git for version control:
- Each member worked on their own branch.
- Code was merged through pull requests.
- All notebooks are in the `notebooks/` folder.

## 8.5 Conclusion

We built a churn prediction pipeline using simulated e-commerce data. Random Forest performed best. Future work could include hyperparameter tuning and testing on real data.
