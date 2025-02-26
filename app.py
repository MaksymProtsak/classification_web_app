from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return "<p>Hello world!</p>"


@app.post("/classify")
def upload_file():
    return {
        "label": "*CAT*",
        "probability": 0.95
    }
