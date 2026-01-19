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
The model works well - a linear model can capture most of the churn signal in our features.

Looking at the coefficients, sentiment features (`risk_score`, `sentiment_score`) are strong predictors. Purchase behavior (`estimated_spend`, `spend_ratio`) also helps.
