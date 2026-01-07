# 2. Feature Engineering (Person B)

## 2.1 Feature Categories

We processed the raw data to create features for modeling:

1.  **Raw Numerical**: `age`, `income`, `total_orders`, `avg_order_value`, `days_since_last_purchase`.
2.  **Derived Numerical**: `estimated_spend` (Total Orders × Avg Order Value), `spend_ratio` (Estimated Spend / Income).
3.  **Text-Derived Features**: `sentiment_score`, `risk_score` (Extracted from `review_text` using keyword matching).
4.  **Target**: `churn` (pre-generated during simulation using a probabilistic risk-score rule that combines recency, frequency, and sentiment).

## 2.2 Text Feature Extraction

We wrote a Python function to extract sentiment and risk from the `review_text` field using keyword matching:
- **Negative/High Risk**: Words like "disappointed", "poor", "slow", "bad".
- **Positive/Low Risk**: Words like "satisfied", "great", "excellent".

**Transformation Example**:
| Review Text | Extracted Sentiment | Extracted Risk |
| :--- | :--- | :--- |
| "Product quality was bad" | Negative | High |
| "Decent service" | Neutral | Medium |

## 2.3 Encoding

To make these categorical features usable for Machine Learning models (like Decision Trees and Neural Networks):
- **Sentiment**: Mapped to Ordinal (`Negative=0, Neutral=1, Positive=2`).
- **Churn Risk**: Mapped to Ordinal (`Low=0, Medium=1, High=2`).

## 2.4 Exploratory Data Analysis (EDA) Summary

A brief analysis of the engineered features revealed:
- **Churn Correlation**: As expected, `churn` is highly correlated with `days_since_last_purchase` (by definition) and `sentiment_score` (negative sentiment correlates with churn).
- **Income Distribution**: The dataset shows a realistic right-skewed income distribution.
- **Completeness**: No missing values were found after processing.

## 2.5 Implementation Notes

The keyword lists were chosen based on common e-commerce review patterns. The extraction is done with simple string matching in Python.
