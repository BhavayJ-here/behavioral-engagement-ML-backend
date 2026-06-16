from flask import Blueprint, request, jsonify
import pickle
import pandas as pd
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from utils.features import engineer_features, get_feature_columns

predict_bp = Blueprint("predict", __name__)

with open("ml/models/engagement_model.pkl", "rb") as f:
    model = pickle.load(f)

@predict_bp.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()

    df = pd.DataFrame([data])
    df = engineer_features(df)

    score = model.predict_proba(df[get_feature_columns()])[0][1]

    return jsonify({
        "user_id": data.get("user_id"),
        "content_id": data.get("content_id"),
        "engagement_score": round(score, 3),
        "label": "engaged" if score > 0.5 else "not_engaged"
    })