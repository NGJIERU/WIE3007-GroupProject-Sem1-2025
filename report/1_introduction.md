# 1. Introduction & Dataset Simulation (Person A)

## 1.1 Introduction & Background

### Context
In e-commerce, keeping existing customers is just as important as getting new ones. Predicting which customers might stop buying (churn) helps businesses act early. This project predicts churn risk using transaction data, customer demographics, and review text.

### Motivation
Unhappy customers often leave negative reviews before they stop buying. By catching these signals early, businesses can try to retain them. This project applies predictive modeling to a simulated dataset for the WIE3007 course.

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

## 1.4 Implementation Notes

The dataset was generated using Python with `numpy` and the `random` module. We added business rules to create realistic correlations (e.g., inactive customers tend to have negative reviews).
