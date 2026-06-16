from flask import Blueprint, request, jsonify
import pandas as pd
import os

track_bp = Blueprint("track", __name__)

@track_bp.route("/track", methods=["POST"])
def track():
    data = request.get_json()

    required = ["user_id", "content_id", "watch_time", "content_duration", "skips", "rewatches", "time_of_day", "session_length"]
    if not all(k in data for k in required):
        return jsonify({"error": "Missing fields"}), 400

    df = pd.DataFrame([data])
    path = "data/sessions.csv"

    df.to_csv(path, mode="a", header=not os.path.exists(path), index=False)

    return jsonify({"status": "tracked", "session": data})