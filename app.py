from flask import Flask
from routes.track import track_bp
from routes.predict import predict_bp
from routes.recommend import recommend_bp
 
app = Flask(__name__)
 
# Register blueprints
app.register_blueprint(track_bp)
app.register_blueprint(predict_bp)
app.register_blueprint(recommend_bp)
 
@app.route("/")
def home():
    return {"status": "Behavioral Engagement AI is running"}
 
if __name__ == "__main__":
    app.run(debug=True)