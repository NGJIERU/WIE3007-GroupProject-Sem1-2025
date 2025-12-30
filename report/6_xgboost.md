# Model: XGBoost (Person D)

## Model Choice & Justification
- Gradient boosting algorithm for ensemble learning  
- State-of-the-art performance on tabular data  
- Handles missing values automatically  
- Captures non-linear feature interactions effectively 

## Training Config
- **Train/Test Split:** 80/20 Stratified (random_state=42)  
- **Parameters:**  
  - `n_estimators=300`  
  - `max_depth=4`  
  - `learning_rate=0.05`  
  - `subsample=0.8`  
  - `colsample_bytree=0.8`  

## Evaluation
| Metric | Score |
| :--- | :--- |
| Accuracy |0.945833|
| F1-Score |0.926554|
| ROC-AUC |0.962225|

## Interpretation
- Feature importance analyzed using **gain-based importance from XGBoost**  
- Top features contributed significantly to predicting churn  
- Model distributes predictive power across multiple behavioural and demographic features, reducing over-reliance on any single variable  
