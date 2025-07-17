import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

def train_model():
    X = np.array([[45, 28, 120, 90], [55, 35, 140, 160], [65, 30, 135, 100]])
    y_diabetes = [0, 1, 0]
    y_heart = [1, 1, 0]
    y_cancer = [0, 0, 1]

    scaler = StandardScaler().fit(X)
    X_scaled = scaler.transform(X)

    models = {
        "diabetes": LogisticRegression().fit(X_scaled, y_diabetes),
        "heart": LogisticRegression().fit(X_scaled, y_heart),
        "cancer": LogisticRegression().fit(X_scaled, y_cancer),
    }

    return models, scaler

def predict(models, scaler, features):
    features_scaled = scaler.transform([features])
    return {
        disease: model.predict_proba(features_scaled)[0][1]
        for disease, model in models.items()
    }
