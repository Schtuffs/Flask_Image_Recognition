"""
These are the custom test cases for our assignment
"""

from app import app
from model import preprocess_img
from PIL import UnidentifiedImageError

def test_empty_image():
    """Basic: This tests an empty image"""
    try:
        preprocess_img('./test_images/0/empty.jpeg')
        assert False

    except UnidentifiedImageError:
        assert True
    
def test_index_endpoint():
    """Basic: Index route returns 200"""
    assert app.test_client().get('/').status_code == 200
