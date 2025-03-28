# app/server.py
from flask import Flask, request, jsonify, render_template
from app.emotion_detector import analyze_emotion

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    """API endpoint to analyze text for emotions."""
    data = request.get_json()
    
    if "text" not in data or not data["text"].strip():
        return jsonify({"error": "Invalid input. Please provide text."}), 400

    emotions = analyze_emotion(data["text"])
    return jsonify(emotions)

if __name__ == "__main__":
    app.run(debug=True)
