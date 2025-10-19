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
