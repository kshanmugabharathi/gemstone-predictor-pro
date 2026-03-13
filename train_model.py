import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from catboost import CatBoostRegressor
import dill
import os

# Load data
print("Loading data...")
data = pd.read_csv('artifacts/data.csv')

# Separate features and target
X = data.drop('price', axis=1)
y = data['price']

# Identify categorical and numerical columns
numerical_cols = ['carat', 'depth', 'table', 'x', 'y', 'z']
categorical_cols = ['cut', 'color', 'clarity']

# Preprocessing
print("Preprocessing data...")
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_cols),
        ('cat', OneHotEncoder(drop='first', sparse_output=False, handle_unknown='ignore'), categorical_cols)
    ]
)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit preprocessor
X_train_processed = preprocessor.fit_transform(X_train)
X_test_processed = preprocessor.transform(X_test)

# Train model
print("Training CatBoost model...")
model = CatBoostRegressor(
    iterations=100,
    learning_rate=0.1,
    depth=6,
    verbose=False,
    random_state=42
)
model.fit(X_train_processed, y_train)

# Evaluate
train_score = model.score(X_train_processed, y_train)
test_score = model.score(X_test_processed, y_test)
print(f"Train R² Score: {train_score:.4f}")
print(f"Test R² Score: {test_score:.4f}")

# Save preprocessor
print("Saving preprocessor and model...")
os.makedirs('artifacts', exist_ok=True)

with open('artifacts/preprocessor.pkl', 'wb') as f:
    dill.dump(preprocessor, f)

with open('artifacts/model.pkl', 'wb') as f:
    dill.dump(model, f)

print("Model and preprocessor saved successfully!")
print("You can now restart the Flask application.")
