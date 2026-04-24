"""
Flask server for the EmotionDetection package.
Provides an endpoint to analyze emotions in text.
"""

from flask import Flask, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """
    Analyze text using the emotion_detector function.
    Returns formatted emotion scores or an error message for invalid input.
    """
    text_to_analyze = request.args.get("text", "")

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant = result["dominant_emotion"]

    response = (
        f"For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )

    return response


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
