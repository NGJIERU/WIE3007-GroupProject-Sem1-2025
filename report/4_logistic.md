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
- Parameters: 
- Baseline
  - `penalty='l2'`
  - `C=10.0`
  - `solver='lbfgs'`
  - `max_iter=1000`
  - `random_state=42`
- Controlled
  - `penalty='l2'`
  - `C=0.1`
  - `solver='lbfgs'`
  - `max_iter=1000`
  - `random_state=42`
- Tuned(GridSearchCV)
  - `penalty='l2'`
  - `C=0.001`
  - `solver='liblinear'`
  - `max_iter=500`
  - `random_state=42`
  - `class_weight=None`

## Evaluation
Baseline:
| Metric | Score |
| :--- | :--- |
| Trained Accuracy | 0.9375 |
| Test Accuracy | 0.9417 |
| Gap | -0.0042 |
| F1-Score | 0.9176 |
| ROC-AUC | 0.9647 |

Controlled:
| Metric | Score |
| :--- | :--- |
| Trained Accuracy | 0.9375 |
| Test Accuracy | 0.9417 |
| Gap | -0.0042 |
| F1-Score | 0.9176 |

Tuned:
| Metric | Score |
| :--- | :--- |
| Trained Accuracy | 0.9375 |
| Test Accuracy | 0.9417 |
| Gap | -0.0042 |
| F1-Score | 0.9176 |

## Interpretation
- Feature importance analysed using Logistic Regression coefficients
- Baseline model shows no overfitting (train ≈ test accuracy)
- Controlled model maintains performance, indicating effective regularisation
- Tuned model (C via GridSearchCV) shows no significant change, suggesting model is already optimal
- Top feature: total orders

## Bias-Variance Analysis
- Low C (strong regularisation): underfitting → high bias, constrained model
- Moderate C: optimal → minimal train–test gap, best generalisation
- High C (weak regularisation): slight variance increase, but no clear overfitting observed

## Conclusion
- Logistic Regression effectively captures linear relationships in the dataset
- Regularisation helps maintain stable generalisation
- GridSearchCV tuning of C provides limited improvement due to already well-balanced model
- Model is robust against data leakage and distributes importance across multiple features