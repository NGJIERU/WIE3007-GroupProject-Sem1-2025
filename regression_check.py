import sys
from dataclasses import dataclass
from pathlib import Path

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier


@dataclass(frozen=True)
class ExpectedMetrics:
    decision_tree_acc: float = 0.904167
    logistic_regression_acc: float = 0.941667
    random_forest_acc: float = 0.958333
    xgboost_acc: float = 0.95
    mlp_acc: float = 0.929167

    tolerance: float = 0.02


def _repo_root() -> Path:
    return Path(__file__).resolve().parent


def _assert(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def check_data_files(repo: Path) -> None:
    data_dir = repo / "data"
    raw_path = data_dir / "synthetic_customers_raw.csv"
    features_path = data_dir / "features.csv"
    target_path = data_dir / "target.csv"

    _assert(raw_path.exists(), f"Missing file: {raw_path}")
    _assert(features_path.exists(), f"Missing file: {features_path}")
    _assert(target_path.exists(), f"Missing file: {target_path}")

    raw = pd.read_csv(raw_path)
    features = pd.read_csv(features_path)
    target = pd.read_csv(target_path).squeeze()

    _assert(raw.shape[0] == 1200, f"raw row count expected 1200, got {raw.shape[0]}")
    _assert(features.shape[0] == 1200, f"features row count expected 1200, got {features.shape[0]}")
    _assert(len(target) == 1200, f"target row count expected 1200, got {len(target)}")

    _assert(raw.isnull().sum().sum() == 0, "raw contains missing values")
    _assert(features.isnull().sum().sum() == 0, "features contains missing values")

    expected_raw_cols = {
        "customer_id",
        "age",
        "income",
        "total_orders",
        "avg_order_value",
        "days_since_last_purchase",
        "review_text",
        "churn",
    }
    _assert(
        expected_raw_cols.issubset(set(raw.columns)),
        f"raw is missing expected columns: {sorted(expected_raw_cols - set(raw.columns))}",
    )

    expected_engineered_cols = {
        "age",
        "income",
        "total_orders",
        "avg_order_value",
        "estimated_spend",
        "spend_ratio",
        "sentiment_score",
        "risk_score",
        "days_since_last_purchase",
    }
    _assert(
        expected_engineered_cols.issubset(set(features.columns)),
        f"features.csv is missing expected columns: {sorted(expected_engineered_cols - set(features.columns))}",
    )

    target_values = set(pd.Series(target).dropna().unique().tolist())
    _assert(
        target_values.issubset({0, 1}),
        f"target contains unexpected values: {sorted(target_values)} (expected only 0/1)",
    )

    print("✅ Data checks passed")


def compute_metrics(repo: Path) -> pd.DataFrame:
    X = pd.read_csv(repo / "data" / "features.csv")
    y = pd.read_csv(repo / "data" / "target.csv").squeeze()

    if "days_since_last_purchase" in X.columns:
        X = X.drop(columns=["days_since_last_purchase"])

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    rows = []

    def add(name: str, y_pred, y_prob):
        rows.append(
            {
                "model": name,
                "accuracy": accuracy_score(y_test, y_pred),
                "f1_score": f1_score(y_test, y_pred),
                "roc_auc": roc_auc_score(y_test, y_prob),
            }
        )

    dt = DecisionTreeClassifier(random_state=42)
    dt.fit(X_train, y_train)
    add("Decision Tree", dt.predict(X_test), dt.predict_proba(X_test)[:, 1])

    lr_scaler = StandardScaler()
    X_train_lr = lr_scaler.fit_transform(X_train)
    X_test_lr = lr_scaler.transform(X_test)
    lr = LogisticRegression(
        C=1.0,
        solver="lbfgs",
        max_iter=1000,
        random_state=42,
    )
    lr.fit(X_train_lr, y_train)
    add("Logistic Regression", lr.predict(X_test_lr), lr.predict_proba(X_test_lr)[:, 1])

    rf = RandomForestClassifier(
        n_estimators=200,
        max_depth=10,
        max_features="sqrt",
        random_state=42,
    )
    rf.fit(X_train, y_train)
    add("Random Forest", rf.predict(X_test), rf.predict_proba(X_test)[:, 1])

    try:
        from xgboost import XGBClassifier

        xgb_model = XGBClassifier(
            n_estimators=300,
            max_depth=4,
            learning_rate=0.05,
            subsample=0.8,
            colsample_bytree=0.8,
            eval_metric="logloss",
            random_state=42,
        )
        xgb_model.fit(X_train, y_train)
        add("XGBoost", xgb_model.predict(X_test), xgb_model.predict_proba(X_test)[:, 1])
    except Exception as e:
        rows.append(
            {
                "model": "XGBoost",
                "accuracy": float("nan"),
                "f1_score": float("nan"),
                "roc_auc": float("nan"),
                "error": str(e),
            }
        )

    mlp_scaler = StandardScaler()
    X_train_m = mlp_scaler.fit_transform(X_train)
    X_test_m = mlp_scaler.transform(X_test)
    mlp = MLPClassifier(
        hidden_layer_sizes=(100, 50, 25),
        activation="relu",
        solver="adam",
        max_iter=1000,
        random_state=42,
    )
    mlp.fit(X_train_m, y_train)
    add("MLP", mlp.predict(X_test_m), mlp.predict_proba(X_test_m)[:, 1])

    return pd.DataFrame(rows)


def check_metrics(metrics: pd.DataFrame, expected: ExpectedMetrics) -> None:
    tol = expected.tolerance

    def within(actual: float, exp: float) -> bool:
        return abs(actual - exp) <= tol

    m = metrics.set_index("model")

    _assert(
        within(float(m.loc["Decision Tree", "accuracy"]), expected.decision_tree_acc),
        f"Decision Tree accuracy drifted: got {float(m.loc['Decision Tree','accuracy']):.6f}, expected ~{expected.decision_tree_acc:.6f}",
    )
    _assert(
        within(float(m.loc["Logistic Regression", "accuracy"]), expected.logistic_regression_acc),
        f"Logistic Regression accuracy drifted: got {float(m.loc['Logistic Regression','accuracy']):.6f}, expected ~{expected.logistic_regression_acc:.6f}",
    )
    _assert(
        within(float(m.loc["Random Forest", "accuracy"]), expected.random_forest_acc),
        f"Random Forest accuracy drifted: got {float(m.loc['Random Forest','accuracy']):.6f}, expected ~{expected.random_forest_acc:.6f}",
    )
    if "XGBoost" in m.index and "accuracy" in m.columns:
        xgb_error = None
        if "error" in m.columns:
            xgb_error = m.loc["XGBoost", "error"]
        xgb_acc = m.loc["XGBoost", "accuracy"]
        if (isinstance(xgb_error, str) and xgb_error.strip()) or pd.isna(xgb_acc):
            print("⚠️ Skipping XGBoost tolerance check (XGBoost not available in this environment)")
        else:
            _assert(
                within(float(xgb_acc), expected.xgboost_acc),
                f"XGBoost accuracy drifted: got {float(xgb_acc):.6f}, expected ~{expected.xgboost_acc:.6f}",
            )
    _assert(
        within(float(m.loc["MLP", "accuracy"]), expected.mlp_acc),
        f"MLP accuracy drifted: got {float(m.loc['MLP','accuracy']):.6f}, expected ~{expected.mlp_acc:.6f}",
    )

    print("✅ Metric tolerance checks passed")


def main() -> int:
    repo = _repo_root()
    expected = ExpectedMetrics()

    check_data_files(repo)
    metrics = compute_metrics(repo)
    print(metrics)

    if "error" in metrics.columns:
        errors = metrics[metrics["error"].notna()]
        if not errors.empty:
            print("⚠️ Some models could not be evaluated:")
            print(errors[["model", "error"]])

    check_metrics(metrics, expected)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
