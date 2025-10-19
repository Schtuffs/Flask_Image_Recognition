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

def data_check(client, img_data):
    """Checks for multiple images"""
    response = client.post(
        "/prediction",
        data={"file": (img_data, img_data.name)},
        content_type="multipart/form-data"
    )

    assert b"Prediction" in response.data
