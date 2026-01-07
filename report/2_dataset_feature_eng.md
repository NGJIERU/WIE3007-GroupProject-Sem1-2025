# 2. Feature Engineering (Person B)

## 2.1 Feature Categories

We transformed the raw simulated data into a model-ready feature set. The features are categorized as follows:

1.  **Raw Numerical**: `age`, `income`, `total_orders`, `avg_order_value`, `days_since_last_purchase`.
2.  **Derived Numerical**: `estimated_spend` (Total Orders × Avg Order Value), `spend_ratio` (Estimated Spend / Income).
3.  **LLM-Derived Text Features**: `sentiment_score`, `risk_score` (Extracted from `review_text`).
4.  **Target**: `churn` (pre-generated during simulation using a probabilistic risk-score rule that combines recency, frequency, and sentiment).

## 2.2 LLM-Aided Feature Extraction

To utilize the unstructured `review_text`, we employed a Large Language Model (LLM) to design a keyword-based extraction purpose.

**LLM Prompt**:
> "You are a sentiment analyst. Given short e-commerce reviews, provide a set of keywords to classify them into:
> 1. Sentiment: Positive / Neutral / Negative
> 2. Churn Risk: Low / Medium / High
> Return python-ready lists of keywords."

**Logic Implementation**:
Based on the LLM's output, we implemented a Python function `extract_sentiment_and_risk`.
- **Negative/High Risk**: Contains words like "disappointed", "poor", "slow", "bad".
- **Positive/Low Risk**: Contains words like "satisfied", "great", "excellent".

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

## 2.5 AI Usage Documentation (Feature Engineering)

**Usage**: AI was used to **design the text extraction logic**.
**Role**: The AI acted as a "Domain Expert" suggesting which keywords indicate churn risk. The actual processing was done via deterministic Python code (Person B) to ensure reproducibility.
