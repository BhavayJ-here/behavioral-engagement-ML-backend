import pandas as pd
import pickle
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from utils.features import engineer_features, get_feature_columns

def train():
    df = pd.read_csv("data/sessions.csv")
    df = engineer_features(df)

    X = df[get_feature_columns()]
    y = df["engaged"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    print(classification_report(y_test, model.predict(X_test)))

    os.makedirs("ml/models", exist_ok=True)
    with open("ml/models/engagement_model.pkl", "wb") as f:
        pickle.dump(model, f)

    print("Model saved -> ml/models/engagement_model.pkl")

if __name__ == "__main__":
    train()