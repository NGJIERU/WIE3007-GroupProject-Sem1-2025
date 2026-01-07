# 3. Model 1: Decision Tree (Person A)

## 3.1 Model Choice

We selected a **Decision Tree Classifier** as our initial baseline model.
- Decision Trees are easy to interpret and don't need feature scaling.
- Good starting point to check if the data pipeline works before trying complex models.

## 3.2 Training Strategy

**Data Split**:
- We used a **80/20 train-test split**.
- **Stratification**: Enabled (`stratify=y`) to ensure the proportion of churned customers is consistent across both sets.
- **Random State**: Set to `42` for reproducibility.

**Hyperparameters**:
- `criterion`: "gini" (Default)
- `max_depth`: None (for the initial baseline) vs `max_depth=5` (for controlled experiment).
- `random_state`: 42

## 3.3 Evaluation Results

The baseline model was evaluated on the unseen test set (20% of data).

| Metric | Score | Interpretation |
| :--- | :--- | :--- |
| **Accuracy** | 0.9042 | Describes overall correctness. |
| **F1-Score** | 0.8623 | Balances Precision and Recall (critical for churn). |
| **ROC-AUC** | 0.8933 | Measures ability to rank churners vs non-churners. |

*(Note: Exact values are logged in the Evaluation Notebook `09_evaluation_hub.ipynb`)*

## 3.4 Feature Importance & Interpretation

The Decision Tree revealed the key drivers of churn.
**Top features identified:**
1.  `risk_score` / `sentiment_score`: Confirming that negative reviews are strong predictors.
2.  Purchase behavior features such as `estimated_spend`, `total_orders`, and `spend_ratio`.
3.  `income` or `total_orders`: Demographic/Behavioral factors.

## 3.5 Notes

We used standard sklearn for training. The tree structure can help identify customer patterns (e.g., high-risk customers with negative sentiment).
