"""
Test module
"""

import pytest
from app import app  # This imports the Flask app for testing

@pytest.fixture
def client():
    """Client"""
    with app.test_client() as clnt:
        yield clnt

def data_check(clnt, img_data):
    """Checks for multiple images"""
    response = clnt.post(
        "/prediction",
        data={"file": (img_data, img_data.name)},
        content_type="multipart/form-data"
    )

    assert response.status_code == 200
    assert b"Prediction" in response.data
