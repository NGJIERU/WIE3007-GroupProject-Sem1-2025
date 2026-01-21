# Model: MLP / Neural Network (Person E)

## Model Choice & Justification
MLP (neural network) can capture non-linear patterns that simpler models might miss. It's a good comparison to tree-based methods.

## Training Config
-Data Split: 80/20 Stratified (random_state=42)

-Architecture: 3 hidden layers with 100, 50, 25 units; ReLU activation

-Optimizer & Loss: Adam optimizer; Binary Crossentropy

-Scaling: StandardScaler applied to all features

## Evaluation
| Metric | Score |
| :--- | :--- |
| Accuracy |0.9292 |
| F1-Score |0.9017 |
| ROC-AUC |0.9618 |

## Interpretation
The MLP captures non-linear patterns in the dataset, making it more flexible than linear models. While it slightly underperforms compared to tree-based ensembles (Random Forest, XGBoost), it offers insightful information about feature interactions. Since the model is a "black-box," methods like permutation importance are necessary for interpretation.

Feature Importance:
Top features driving churn predictions include:

sentiment_score – strongest predictor, reflecting customer satisfaction or dissatisfaction.

risk_score – highlights high-risk or churn-prone customers.

total_orders – shows how purchase frequency impacts churn likelihood.

In contrast to more straightforward linear models such as Logistic Regression or the baseline Decision Tree, the MLP captures non-linear relationships and distributes predictive insights across multiple features, providing a more comprehensive understanding of consumer behavior.