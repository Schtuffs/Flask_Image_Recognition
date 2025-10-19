"""
Integration tests
"""

# test_integration_happy.py

from io import BytesIO

from conftest import data_check

def test_successful_prediction(client):
    """Test the successful image upload and prediction."""
    # Create a mock image file with minimal valid content
    img_data = BytesIO(b"fake_image_data")
    img_data.name = "test.jpg"

    data_check(client, img_data)
