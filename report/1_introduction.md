# 1. Introduction & Dataset Simulation (Person A)

## 1.1 Introduction & Background

### Context
In the highly competitive e-commerce sector, customer retention is as critical as acquisition. Predicting customer churn (whether a customer will stop purchasing) allows businesses to proactively intervene with targeted strategies. While traditional churn models rely on transaction history, this project aims to predict **Churn Risk** by combining transactional data with unstructured feedback (reviews) and customer demographics.

### Motivation
Customer dissatisfaction and reduced engagement often precede churn. By identifying at-risk customers early—specifically using purchase behavior signals and negative sentiment in reviews—businesses can reduce revenue loss. This project fulfills the WIE3007 objective of applying predictive modelling to solve a business problem using a simulated dataset.

### Scope
- **Domain**: E-commerce / Retail.
- **Task**: Binary Classification (Predict `churn`).
- **Data Source**: Fully simulated dataset (Privacy-safe).

## 1.2 Problem Statement

**Prediction Task**: Predict whether a customer is likely to churn (`churn = 1`) based on their purchase history, demographics, and review sentiment.

**Target Variable**:
- `churn`: A binary variable generated during simulation using a probabilistic rule combining recency (inactivity), frequency (orders), and review sentiment.

**Constraints**:
- **Dataset Size**: ~1,200 records (Simulated).
- **AI Usage**: Generative AI was used to design the simulation logic and business rules.

## 1.3 Dataset Simulation

### Methodology
To ensure a compliant and privacy-safe project, we simulated a dataset of 1,200 e-commerce customers. The simulation was designed to reflect realistic patterns (e.g., lower income correlates with lower order values; negative reviews correlate with churn).

### Dataset Schema
The raw dataset (`synthetic_customers_raw.csv`) contains the following key attributes:

| Column | Type | Description |
| :--- | :--- | :--- |
| `customer_id` | Int | Unique identifier |
| `age` | Int | Customer age (18-65) |
| `income` | Float | Annual income |
| `total_orders` | Int | Number of orders placed |
| `days_since_last_purchase`| Int | Days since last activity |
| `review_text` | String | Unstructured feedback |

### Sample Data
| customer_id | age | income | days_since_last_purchase | review_text |
| :--- | :--- | :--- | :--- | :--- |
| 1001 | 45 | 55000 | 12 | "Great service, very happy"|
| 1002 | 23 | 28000 | 200 | "Delivery was slow, disappointed"|

### Data Summary
- **Total Records**: 1200
- **Missing Values**: 0 (Controlled simulation)
- **Class Distribution**: ~30% Churn (Derived), ensuring a realistic imbalance.

## 1.4 AI Usage Documentation (Dataset)

**Usage**: Generative AI (LLM) was used to **design the business rules** for data generation, ensuring realistic correlations.

**Prompt Used**:
> "Design a Python script to generate a synthetic e-commerce customer dataset. Include fields like Age, Income, and a textual 'Review' field. Ensure that 'Review' text sentiment correlates with 'Days Since Last Purchase' (e.g., neg reviews = long inactivity)."

**Implementation**:
The AI-suggested logic was implemented in Python using `numpy` and the standard `random` module. The code was reviewed and executed by the team (Person A) to generate the final CSV file.
