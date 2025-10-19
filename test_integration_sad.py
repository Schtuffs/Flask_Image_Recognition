"""
Integration tests
"""

# test_integration_sad.py

from app import app

def test_missing_file(clnt):
    """Test the prediction route with a missing file."""
    response = clnt.post("/prediction", data={}, content_type="multipart/form-data")
    assert response.status_code == 200
    assert b"File cannot be processed." in response.data  # Check if the error message is displayed
