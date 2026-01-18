# Model: MLP / Neural Network (Person E)

## Model Choice & Justification
The MLP (Multi-Layer Perceptron) was chosen because it can capture complex non-linear interactions among customer features that linear models (like Logistic Regression) might overlook. This "Deep Learning" component complements the tree-based models in the project, offers a flexible method to modeling complex relationships in the retail dataset.

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

Risk Score – the most influential feature, identifying high-risk or churn-prone customers.

Sentiment Score – reflects customer satisfaction or dissatisfaction, strongly impacting churn predictions.

Estimated Spend – indicates the potential monetary value and engagement of a customer.

Total Orders – shows how purchase frequency affects the likelihood of churn.

In contrast to more straightforward linear models such as Logistic Regression or the baseline Decision Tree, the MLP captures non-linear relationships and distributes predictive insights across multiple features, providing a more comprehensive understanding of consumer behavior.