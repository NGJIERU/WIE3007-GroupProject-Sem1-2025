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
| Accuracy | |
| F1-Score | |
| ROC-AUC | |

## Interpretation
[SHAP values or Gain-based importance]
