# Introduction & Objectives

## Introduction

In recent years, businesses have increasingly relied on data-driven decision-making to remain competitive in rapidly evolving markets. In the e-commerce and retail sector, understanding customer purchasing behavior and identifying customers at risk of churn are critical for improving customer retention, optimizing marketing strategies, and maximizing long-term revenue. However, real-world customer datasets are often sensitive, incomplete, or difficult to access due to privacy and confidentiality constraints.

To address these challenges, this project adopts a data mining approach supported by Artificial Intelligence (AI), including Generative AI (GenAI), Large Language Models (LLMs), and Small Language Models (SLMs). By simulating a realistic business dataset and applying AI-enhanced analytics, this project demonstrates how modern data mining techniques can be used to extract insights and build predictive models even in the absence of real proprietary data.

This project focuses on a simulated e-commerce business scenario, where customer demographic information, purchase behavior, and textual feedback are analyzed to predict customer churn and support business decision-making.

---

## Objectives

The objectives of this project are as follows:

1. To simulate a realistic business dataset with over 1,000 customer records using GenAI-assisted data generation techniques.
2. To apply AI-enhanced feature engineering, including text-based feature extraction using LLMs and SLMs.
3. To develop and compare multiple predictive models for customer churn or purchase behavior prediction.
4. To evaluate model performance using appropriate metrics and interpret results with AI-assisted insights.
5. To demonstrate collaborative data mining practices using GitHub version control with transparent individual contributions.

---

## Scope of the Project

This project is limited to a simulated e-commerce customer dataset and focuses on supervised learning techniques for classification. The tools and technologies used include Python, Jupyter Notebook, GitHub, and AI models from the Hugging Face ecosystem. The project emphasizes interpretability, reproducibility, and practical business relevance rather than production deployment.

# Dataset Simulation and Description

## Dataset Overview

This project utilizes a synthetically generated e-commerce customer dataset to support data mining and predictive modelling tasks. Due to privacy, confidentiality, and accessibility limitations associated with real-world business data, synthetic data generation was adopted as a practical and ethical alternative. The dataset represents commonly available customer demographic information, purchasing behavior, and customer-provided textual feedback in an e-commerce context.

The simulated dataset serves as the foundational input for subsequent analysis stages in this project.

---

## GenAI-Assisted Dataset Simulation

Generative Artificial Intelligence (GenAI) was used to assist in the conceptual design of the dataset structure and the formulation of realistic business rules. Specifically, GenAI was leveraged to guide the development of reproducible Python-based logic for dataset generation rather than directly producing static data. This approach ensures transparency, reproducibility, and controlled data characteristics.

Using this approach, a total of **1,200 synthetic customer records** were generated, exceeding the minimum requirement of 1,000 records specified in the project guidelines.

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

These attributes were selected to reflect realistic variables commonly found in e-commerce customer databases.

---

## Business Rules and Realism Constraints

To enhance realism, several domain-inspired business rules were incorporated during data generation:

- Customers with higher income levels tend to place more orders and have higher average order values.
- Customers with a longer duration since their last purchase are more likely to provide negative feedback.
- Customers with frequent and recent purchases are more likely to provide positive feedback.
- Customers who do not strongly exhibit either pattern are assigned neutral feedback.

These constraints ensure meaningful relationships between variables while avoiding artificial feature construction.

---

## Data Validation and Quality Checks

Basic data validation was performed following dataset generation to ensure data integrity and consistency:

- All numerical attributes fall within predefined and realistic ranges.
- No missing values were observed across the dataset.
- Each customer record is uniquely identifiable.
- Summary statistics indicate reasonable distributions across demographic and behavioral attributes.

The validated dataset was stored as a CSV file and made available for downstream tasks in the project pipeline.

---

## Dataset Availability

The synthetic dataset is stored in the project GitHub repository under the `data/` directory. All dataset generation steps are documented within the Jupyter Notebook to ensure reproducibility and version traceability.

