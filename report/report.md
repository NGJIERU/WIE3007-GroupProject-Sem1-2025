# Introduction & Objectives

## Introduction

E-commerce businesses need to understand customer behavior and identify customers who might stop buying (churn). This helps with customer retention and marketing. However, real customer data is often private or hard to get.

For this project, we created a simulated dataset and used text analysis to extract features from customer reviews. This lets us build and test predictive models without needing actual business data.

This project focuses on a simulated e-commerce business scenario, where customer demographic information, purchase behavior, and textual feedback are analyzed to predict customer churn and support business decision-making.

---

## Objectives

The objectives of this project are as follows:

1. Simulate a realistic business dataset with over 1,000 customer records.
2. Engineer features from the data, including extracting info from customer review text.
3. Build and compare multiple models to predict customer churn.
4. Evaluate model performance using standard metrics (accuracy, F1, ROC-AUC).
5. Use GitHub for version control and track each team member's contributions.

---

## Scope of the Project

This project uses a simulated e-commerce dataset and focuses on classification. We used Python, Jupyter Notebook, and GitHub. The goal is to build interpretable and reproducible models, not production deployment.

# Dataset Simulation and Description

## Dataset Overview

We generated a synthetic e-commerce customer dataset since real business data is private and hard to access. The dataset includes customer demographics, purchase behavior, and review text.

---

## Dataset Generation

We used Python scripts to generate the dataset with realistic business rules (e.g., customers with longer inactivity tend to have negative reviews). A total of **1,200 customer records** were generated.

---

## Dataset Schema

The final dataset consists of the following attributes:

| Attribute | Description |
|---------|------------|
| `customer_id` | Unique identifier for each customer |
| `age` | Customer age (18–65 years) |
| `income` | Annual customer income |
| `total_orders` | Total number of past purchases |
| `avg_order_value` | Average value per transaction |
| `days_since_last_purchase` | Number of days since the most recent purchase |
| `review_text` | Short textual customer feedback |

These are typical fields you'd find in a real e-commerce database.

---

## Business Rules and Realism Constraints

We added some business logic to make the data realistic:

- Customers with higher income levels tend to place more orders and have higher average order values.
- Customers with a longer duration since their last purchase are more likely to provide negative feedback.
- Customers with frequent and recent purchases are more likely to provide positive feedback.
- Customers who do not strongly exhibit either pattern are assigned neutral feedback.

This creates natural correlations between the variables.

---

## Data Validation and Quality Checks

We checked the data after generation:

- All numerical attributes fall within predefined and realistic ranges.
- No missing values were observed across the dataset.
- Each customer record is uniquely identifiable.
- Summary statistics indicate reasonable distributions across demographic and behavioral attributes.

The final dataset is saved as a CSV file in the `data/` folder.

---

## Dataset Availability

The synthetic dataset is stored in the project GitHub repository under the `data/` directory. All dataset generation steps are documented within the Jupyter Notebook to ensure reproducibility and version traceability.

