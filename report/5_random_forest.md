# Model: Random Forest (Person C)

## Model Choice & Justification
- Handles non-linear relationships in tabular data effectively.
- Reduces overfitting by averaging multiple decision trees.
- Is robust to noisy data, such as the probabilistic churn and "Karen" customers added to the dataset.
- Improves generalization over a single Decision Tree baseline.

## Training Config
- Split: 80/20 Stratified (random_state=42)
- Parameters: [e.g., n_estimators=100, max_depth=None]

## Evaluation
| Metric | Score |
| :--- | :--- |
| Accuracy | |
| F1-Score | |
| ROC-AUC | |

## Interpretation
[Feature Importance comparison vs Decision Tree]
