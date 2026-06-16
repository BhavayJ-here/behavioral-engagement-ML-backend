from flask import Blueprint, request, jsonify
import pandas as pd
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from utils.features import engineer_features

recommend_bp = Blueprint("recommend", __name__)

@recommend_bp.route("/recommend", methods=["GET"])
def recommend():
    user_id = request.args.get("user_id", type=int)
    if not user_id:
        return jsonify({"error": "user_id required"}), 400

    df = pd.read_csv("data/sessions.csv")
    user_df = df[df["user_id"] == user_id]

    if user_df.empty:
        return jsonify({"error": "No history for this user"}), 404

    user_df = engineer_features(user_df)

    top_content = (
        user_df.groupby("content_id")["engagement_signal"]
        .mean()
        .sort_values(ascending=False)
        .head(5)
        .reset_index()
        .rename(columns={"engagement_signal": "score"})
    )

    return jsonify({
        "user_id": user_id,
        "recommendations": top_content.to_dict(orient="records")
    })