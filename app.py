"""
Website routes
"""

import sys
from PIL import UnidentifiedImageError
from flask import Flask, render_template, request
from model import preprocess_img, predict_result
from werkzeug.exceptions import BadRequestKeyError

# Instantiating flask app
app = Flask(__name__)


# Home route
@app.route("/")
def main():
    """Main"""
    return render_template("index.html")


# Prediction route
@app.route('/prediction', methods=['POST'])
def predict_image_file():
    """Image predict"""
    try:
        if request.method == 'POST':
            img = preprocess_img(request.files['file'].stream)
            pred = predict_result(img)
            return render_template("result.html", predictions=str(pred))

    except UnidentifiedImageError:
        error = "File cannot be processed."
        return render_template("result.html", err=error)
    except FileNotFoundError:
        error = "File cannot be processed."
        return render_template("result.html", err=error)
    except BadRequestKeyError:
        error = "File cannot be processed."
        return render_template("result.html", err=error)
    return render_template("result.html")


# Driver code
if __name__ == "__main__":
    app.run(port=9000, debug=True)
