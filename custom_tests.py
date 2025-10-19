"""
These are the custom test cases for our assignment
"""

from werkzeug.exceptions import BadRequestKeyError
from PIL import UnidentifiedImageError
from model import predict_result, preprocess_img

# ----- Basic -----

def test_index_endpoint(client):
    """Basic: Index route returns 200"""
    assert client.get('/').status_code == 200

def test_predictions_post(client):
    """Basic: Test predictions cannot be accessed through GET"""
    assert client.get('/prediction').status_code == 405

# ----- Advanced -----

def test_empty_image():
    """Advanced: This tests an empty image"""
    try:
        preprocess_img('./test_images/0/empty.jpeg')
        assert False
    except UnidentifiedImageError:
        assert True

def test_invalid_file():
    """Advanced: Invalid file is properly disposed of"""
    try:
        predict_result(preprocess_img('fake_file.txt'))
        assert False
    except UnidentifiedImageError:
        assert True
    except FileNotFoundError:
        assert True
    except BadRequestKeyError:
        assert True
    assert True
