from flask import Flask, request, jsonify
from app.emotion_detector import analyze_emotion  # Importing the function

app = Flask(__name__)

@app.route('/detect-emotion', methods=['POST'])
def detect_emotion():
    data = request.get_json()  # Get input text from request
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    result = analyze_emotion(text)  # Call the function from emotion_detector.py
    return jsonify(result)  # Return the detected emotion as JSON

if __name__ == '__main__':
    app.run(debug=True)
