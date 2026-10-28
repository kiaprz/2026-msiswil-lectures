import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    roc_auc_score
)

# Wczytanie danych
df = pd.read_csv("datasets/ai4i2020.csv")

# Usunięcie identyfikatorów
X = df.drop(columns=[
    "Machine failure",
    "UDI",
    "Product ID"])

y = df["Machine failure"]

# Zmienne kategoryczne i numeryczne
categorical_features = ["Type"]
numerical_features = [c for c in X.columns if c not in categorical_features]

# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
        ("num", "passthrough", numerical_features)
    ]
)

# Model
model = RandomForestClassifier(
    n_estimators=300,
    max_depth=10,
    class_weight="balanced",
    random_state=42
)

pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("model", model)
])

# Podział danych
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

# Trenowanie
pipeline.fit(X_train, y_train)

# Predykcja
y_pred = pipeline.predict(X_test)
y_prob = pipeline.predict_proba(X_test)[:, 1]

# Ocena
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
print("ROC AUC =", roc_auc_score(y_test, y_prob))
