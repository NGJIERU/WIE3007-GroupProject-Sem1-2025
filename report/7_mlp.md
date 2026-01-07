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
MLP works but doesn't beat tree-based models on this dataset. Top features are similar to other models: `sentiment_score`, `risk_score`, `total_orders`.

Neural networks need more tuning to match tree performance here.