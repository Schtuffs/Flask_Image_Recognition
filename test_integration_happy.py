"""
Integration tests
"""

# test_integration_happy.py

from io import BytesIO
import pytest
from test_acceptance_happy import data_check

@pytest.fixture
def test_successful_prediction(client):
    """Test the successful image upload and prediction."""
    # Create a mock image file with minimal valid content
    img_data = BytesIO(b"fake_image_data")
    img_data.name = "test.jpg"

    data_check(client, img_data)
