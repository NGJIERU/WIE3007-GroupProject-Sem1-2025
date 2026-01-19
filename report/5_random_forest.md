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
Random Forest got the best results. The ensemble approach helps avoid overfitting.

Top features:
- `risk_score` - strongest predictor
- `sentiment_score` - captures negative reviews
- `spend_ratio` - spending behavior

Unlike single Decision Tree, Random Forest spreads importance across features, making it more stable. 
