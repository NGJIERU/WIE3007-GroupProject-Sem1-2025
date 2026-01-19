# Model: XGBoost (Person D)

## Model Choice & Justification
- Gradient boosting algorithm for ensemble learning  
- State-of-the-art performance on tabular data  
- Handles missing values automatically  
- Captures non-linear feature interactions effectively 

## Training Config
- **Train/Test Split:** 80/20 Stratified (random_state=42)  
- **Parameters:**
- Baseline
  - `n_estimators=500`  
  - `max_depth=6`  
  - `learning_rate=0.05`  
  - `subsample=1.0`  
  - `colsample_bytree=1.0`  
- Controlled
  - `n_estimators=300`  
  - `max_depth=3`  
  - `learning_rate=0.05`  
  - `subsample=0.8`  
  - `colsample_bytree=0.8`
- Tuned(GridSearchCV)
  - `n_estimators=500`  
  - `max_depth=2`  
  - `learning_rate=0.01`  
  - `subsample=0.7`  
  - `colsample_bytree=0.7`  
## Evaluation
Baseline
| Metric | Score |
| :--- | :--- |
| Train Accuracy |1.0000|
| Test Accuracy |0.9417|
| Gap |0.0583|
| F1-Score |0.9205|
| ROC-AUC |0.9641|
Controlled
| Metric | Score |
| :--- | :--- |
| Train Accuracy |0.9521|
| Test Accuracy |0.9333|
| Gap |0.0187|
| F1-Score |0.9070|
Tuned
| Metric | Score |
| :--- | :--- |
| Train Accuracy |0.9375|
| Test Accuracy |0.9417|
| Gap |-0.0042|
| F1-Score |0.9176|


## Interpretation
- Feature importance analyzed using **gain-based importance from XGBoost**  
- Top features contributed significantly to predicting churn  
- Model distributes predictive power across multiple behavioural and demographic features, reducing over-reliance on any single variable  
