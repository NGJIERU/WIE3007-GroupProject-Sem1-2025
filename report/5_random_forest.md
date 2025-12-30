# Model: Random Forest (Person C)

## Model Choice & Justification
- Handles non-linear relationships in tabular data effectively.
- Reduces overfitting by averaging multiple decision trees.
- Is robust to noisy data, such as the probabilistic churn and "Karen" customers added to the dataset.
- Improves generalization over a single Decision Tree baseline.

## Training Config
- Split: 80/20 Stratified (random_state=42)

Parameters:
- `n_estimators` = 200
- `max_depth` = 10 
- `max_features` = 'sqrt' 
- `random_state` = 42 

## Evaluation
| Metric | Score |
| :--- | :--- |
| Accuracy |0.9583|
| F1-Score |0.9425|
| ROC-AUC |0.9674|

## Interpretation
The Random Forest model achieved high but realistic performance, confirming it learned genuine non-linear patterns rather than exploiting data leakage.

Feature Importance:
Top features driving churn predictions include:
- `risk_score` – strongest predictor, aligns with expected risk-driven churn.
- `sentiment_score` – captures customer dissatisfaction from reviews.
- `spend_ratio` – indicates economic behavior impact on churn.

Compared to the baseline Decision Tree, Random Forest distributes predictive power across multiple features, improving stability and reducing over-reliance on any single feature. 
