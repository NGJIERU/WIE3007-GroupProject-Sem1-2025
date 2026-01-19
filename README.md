# WIE3007 Data Mining Group Project

## Customer Churn Prediction using Machine Learning

This project predicts customer churn in an e-commerce setting using various machine learning models. We simulate a realistic customer dataset, engineer features from transaction data and review text, and compare multiple classification models.

---

## Quick Start

### 1. Clone the repository
```bash
git clone https://github.com/NGJIERU/WIE3007-GroupProject-Sem1-2025.git
cd WIE3007-GroupProject-Sem1-2025
```

### 2. Set up Python environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**Required packages:**
- pandas
- numpy
- matplotlib
- scikit-learn
- jupyter
- xgboost (optional, for XGBoost model)

### 3. Run the notebooks
Open Jupyter Notebook or VS Code and run the notebooks in order (01 → 10).

```bash
jupyter notebook
```

---

## Project Structure

```
WIE3007-GroupProject-Sem1-2025/
│
├── data/                          # Dataset files
│   ├── synthetic_customers_raw.csv   # Raw simulated customer data (1200 records)
│   ├── features.csv                  # Engineered features for modeling
│   └── target.csv                    # Target variable (churn: 0 or 1)
│
├── notebooks/                     # Jupyter notebooks (run in order)
│   ├── 01_dataset_simulation.ipynb      # Generate synthetic customer data
│   ├── 02_feature_engineering.ipynb     # Create features from raw data
│   ├── 03_validation_checks.ipynb       # Data quality checks
│   ├── 04_model_decision_tree.ipynb     # Decision Tree (baseline)
│   ├── 05_model_logistic_regression.ipynb
│   ├── 06_model_random_forest.ipynb
│   ├── 07_model_xgboost.ipynb
│   ├── 08_model_mlp.ipynb               # Neural Network
│   ├── 09_evaluation_hub.ipynb          # Compare all models side-by-side
│   └── 10_final_insights_optional.ipynb # Optional LLM-based insights
│
├── report/                        # Project report (Markdown)
│   ├── report.md                     # Main report overview
│   ├── 1_introduction.md             # Introduction & dataset simulation
│   ├── 2_dataset_feature_eng.md      # Feature engineering details
│   ├── 3_decision_tree.md            # Decision Tree model report
│   ├── 4_logistic.md                 # Logistic Regression report
│   ├── 5_random_forest.md            # Random Forest report
│   ├── 6_xgboost.md                  # XGBoost report
│   ├── 7_mlp.md                      # MLP/Neural Network report
│   └── 8_evaluation_conclusion.md    # Final evaluation & conclusion
│
├── regression_check.py            # Automated validation script
├── requirements.txt               # Python dependencies
└── README.md                      # This file
```

---

## How to Go Through This Project

### Step 1: Understand the Data

Start by reading `report/1_introduction.md` to understand:
- What problem we're solving (customer churn prediction)
- How the dataset was simulated
- What features are available

Then look at the raw data:
```python
import pandas as pd
df = pd.read_csv("data/synthetic_customers_raw.csv")
df.head()
```

### Step 2: Run the Notebooks in Order

| Notebook | What it does | Output |
|----------|--------------|--------|
| `01_dataset_simulation.ipynb` | Generates 1200 synthetic customer records | `data/synthetic_customers_raw.csv` |
| `02_feature_engineering.ipynb` | Extracts sentiment from reviews, creates derived features | `data/features.csv`, `data/target.csv` |
| `03_validation_checks.ipynb` | Checks data quality (no missing values, correct ranges) | Validation report |
| `04_model_decision_tree.ipynb` | Trains Decision Tree baseline model | Model metrics |
| `05_model_logistic_regression.ipynb` | Trains Logistic Regression | Model metrics |
| `06_model_random_forest.ipynb` | Trains Random Forest | Model metrics |
| `07_model_xgboost.ipynb` | Trains XGBoost | Model metrics |
| `08_model_mlp.ipynb` | Trains Neural Network (MLP) | Model metrics |
| `09_evaluation_hub.ipynb` | **Compares all 5 models** | Comparison table & charts |
| `10_final_insights_optional.ipynb` | (Optional) LLM-generated business insights | Business recommendations |

**Important:** Run notebooks from the `notebooks/` folder. All data paths use `../data/`.

### Step 3: Check the Evaluation Results

Open `09_evaluation_hub.ipynb` to see the final comparison:

| Model | Accuracy | F1-Score | ROC-AUC |
|-------|----------|----------|---------|
| Decision Tree | 0.90 | 0.86 | 0.89 |
| Logistic Regression | 0.94 | 0.92 | 0.96 |
| Random Forest | **0.96** | **0.94** | **0.97** |
| XGBoost | 0.95 | 0.93 | 0.96 |
| MLP | 0.93 | 0.90 | 0.96 |

**Best model:** Random Forest

### Step 4: Read the Full Report

The `report/` folder contains detailed documentation:
1. Start with `report/report.md` for an overview
2. Read individual model reports (3-7) for training details
3. See `report/8_evaluation_conclusion.md` for final conclusions

---

## Dataset Description

### Raw Data (`synthetic_customers_raw.csv`)

| Column | Type | Description |
|--------|------|-------------|
| `customer_id` | int | Unique customer identifier |
| `age` | int | Customer age (18-65) |
| `income` | float | Annual income |
| `total_orders` | int | Number of past orders |
| `avg_order_value` | float | Average order amount |
| `days_since_last_purchase` | int | Days since last activity |
| `review_text` | string | Customer feedback text |
| `churn` | int | Target variable (0=stay, 1=churn) |

### Engineered Features (`features.csv`)

| Feature | Description |
|---------|-------------|
| `estimated_spend` | total_orders × avg_order_value |
| `spend_ratio` | estimated_spend / income |
| `sentiment_score` | Extracted from review text (0=negative, 1=neutral, 2=positive) |
| `risk_score` | Churn risk indicator (0=low, 1=medium, 2=high) |

---

## Validation

Run the automated regression check to verify everything works:

```bash
python regression_check.py
```

This script checks:
- All data files exist with correct shapes (1200 rows)
- No missing values
- All expected columns are present
- Model metrics are within expected tolerance

Expected output:
```
✅ Data checks passed
✅ Metric tolerance checks passed
```

---

## Troubleshooting

### "No module named sklearn"
Install scikit-learn:
```bash
pip install scikit-learn
```

### "No module named xgboost"
XGBoost is optional. Install if needed:
```bash
pip install xgboost
```

### Notebook can't find data files
Make sure you're running notebooks from inside the `notebooks/` folder. All paths use `../data/`.

### Wrong Python version
This project was tested with Python 3.10+. Check your version:
```bash
python --version
```

---

## Team Contributions

Each team member worked on dedicated branches and contributed through pull requests.

| Person | Responsibility |
|--------|----------------|
| Person A | Dataset simulation, Decision Tree |
| Person B | Feature engineering, Logistic Regression |
| Person C | Random Forest |
| Person D | XGBoost |
| Person E | MLP, Evaluation & Conclusion |

---

## Course Information

- **Course:** WIE3007 Data Mining
- **University:** Universiti Malaya
- **Semester:** 2025/2026 Semester 1

---

## License

This project is for educational purposes as part of WIE3007 coursework.
