# Model: Logistic Regression (Person B)

## Model Choice & Justification
Logistic Regression was selected as a strong and interpretable linear baseline.

- It produces calibrated probability outputs that are useful for churn risk ranking.
- It is fast to train and easy to explain (via coefficients).
- It serves as a complementary comparison against tree-based and neural network models.

## Training Config
- Split: 80/20 Stratified (random_state=42)
- Leakage prevention: `days_since_last_purchase` was dropped from the feature set.
- Scaling: `StandardScaler` applied (fit on train, transform test) for numerical stability.
- Parameters: `penalty='l2'`, `C=1.0`, `solver='lbfgs'`, `max_iter=1000`, `random_state=42`

## Evaluation
| Metric | Score |
| :--- | :--- |
| Accuracy | 0.9417 |
| F1-Score | 0.9176 |
| ROC-AUC | 0.9638 |

## Interpretation
The model achieved strong performance, indicating that a linear decision boundary is sufficient to capture much of the churn signal in the engineered feature space.

Coefficient inspection shows that sentiment-related features (e.g., `risk_score` / `sentiment_score`) contribute strongly to churn prediction, while purchase behavior features (e.g., `estimated_spend`, `spend_ratio`, `total_orders`) provide additional signal.
