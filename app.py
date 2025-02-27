import os

import tensorflow as tf
from flask import Flask, request

from classifire import classify

app = Flask(__name__)

STATIC_FOLDER = "static"
UPLOAD_FOLDER = "static/uploads/"

cnn_model = tf.keras.models.load_model(STATIC_FOLDER + "/models/" + "save_at_49.keras")


@app.route("/")
def home():
    img_name = "/static/images/cat-dog.jpg"
    return (''
            f'<body style="background-image: url({img_name});>'
            '<p">Hello world!</p>'
            '')


@app.post("/classify")
def upload_file():
    file = request.files["image"]
    upload_image_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(upload_image_path)

    label, prob = classify(cnn_model, upload_image_path)

    prob = round((float(prob) * 100), 2)

    return {
        "label": label,
        "probability": prob
    }


if __name__ == "__main__":
    app.debug = True
    app.run(debug=True)
