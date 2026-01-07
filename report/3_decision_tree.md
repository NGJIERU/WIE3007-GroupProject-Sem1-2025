# 3. Model 1: Decision Tree (Person A)

## 3.1 Model Choice

We selected a **Decision Tree Classifier** as our initial baseline model.
- **Reasoning**: Decision Trees are highly interpretable, handle both numerical and categorical data well without extensive scaling, and provide a clear "white-box" logic that is useful for explaining churn drivers.
- **Role**: This model serves as the "System Integration Test" to validate the entire data pipeline before deploying more complex algorithms.

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

| Metric | Score (Approx) | Interpretation |
| :--- | :--- | :--- |
| **Accuracy** | ~XX% | Describes overall correctness. |
| **F1-Score** | ~XX% | Balances Precision and Recall (critical for churn). |
| **ROC-AUC** | ~0.XX | Measures ability to rank churners vs non-churners. |

*(Note: Exact values are logged in the Evaluation Notebook `09_evaluation_hub.ipynb`)*

## 3.4 Feature Importance & Interpretation

The Decision Tree revealed the key drivers of churn.
**Top features identified:**
1.  `days_since_last_purchase`: (Expected, as it's part of the churn definition).
2.  `risk_score` / `sentiment_score`: Confirming that negative reviews are strong predictors.
3.  `income` or `total_orders`: Demographic/Behavioral factors.

## 3.5 AI Usage Documentation (Modeling)

**Usage**: AI was **not used** for the core training code (which used standard `sklearn` libraries).
**Potential AI Role**: AI can be used in the future to summarize the complex tree rules into natural language "personas" of churners (e.g., "High Income but dissatisfied customers").
