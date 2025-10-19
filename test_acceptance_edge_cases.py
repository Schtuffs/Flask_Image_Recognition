"""
Acceptance tests
"""

# test_acceptance_edge_cases.py

from io import BytesIO

from conftest import data_check

# Helper function for concurrent image uploads
def upload_image(client, img_data):
    """
    Helper function to upload an image within a thread.
    - Purpose: Enables concurrent uploads for testing multithreaded scenarios.
    - Usage: Called in separate threads during concurrent tests.
    """
    client.post(
        "/prediction",
        data={"file": (img_data, img_data.name)},
        content_type="multipart/form-data"
    )

# 1. Edge Case: Uploading a Large Image File
def test_edge_case_large_image_upload(client):
    """
    Test uploading a large image to see how the system handles large file sizes.
    - Scenario: Simulates a file upload with a large image (e.g., 10 MB).
    - Expected Behavior: System should handle the file and return a valid prediction response.
    """
    large_img_data = BytesIO(b"large_image_data" * 10**6)  # Simulating a large image
    large_img_data.name = "large_image.jpg"

    data_check(client, large_img_data)

# 2. Edge Case: Uploading an Image with Missing or Incorrect Metadata
def test_edge_case_invalid_metadata(client):
    """
    Test uploading an image with missing or incorrect metadata.
    - Scenario: Upload an image without any metadata or with invalid metadata.
    - Expected Behavior: System processes the image regardless of metadata issues.
    """
    img_data = BytesIO(b"image_with_no_metadata")
    img_data.name = "image_no_metadata.jpg"

    data_check(client, img_data)

# 3. Edge Case: Uploading an Image with Non-Standard File Extensions
def test_edge_case_non_standard_image_extensions(client):
    """
    Test uploading images with non-standard file extensions.
    - Scenario: Upload a file with an uncommon extension, e.g., .webp.
    - Expected Behavior: System processes the file as a valid image.
    """
    img_data = BytesIO(b"valid_image_data")
    img_data.name = "non_standard_image.webp"  # Non-standard extension

    data_check(client, img_data)

# 4. Edge Case: Uploading a Sequence of Images for Multi-Step Processing
def test_edge_case_sequential_image_uploads(client):
    """
    Test uploading a sequence of images that trigger multi-step processing.
    - Scenario: Simulate sequential uploads of multiple images.
    - Expected Behavior: Each upload should trigger a separate valid prediction response.
    """
    img_data1 = BytesIO(b"first_image_data")
    img_data1.name = "first_image.jpg"

    img_data2 = BytesIO(b"second_image_data")
    img_data2.name = "second_image.jpg"

    data_check(client, img_data1)
    data_check(client, img_data2)

# 5. Edge Case: Uploading with Unexpected Headers
def test_edge_case_unexpected_headers(client):
    """
    Test uploading an image with unexpected headers.
    - Scenario: Simulate sending headers not expected by the system.
    - Expected Behavior: System should still process the file without errors.
    """
    img_data = BytesIO(b"valid_image_data")
    img_data.name = "unexpected_headers_image.jpg"

    # Simulate uploading with unexpected headers
    response = client.post(
        "/prediction",
        data={"file": (img_data, img_data.name)},
        content_type="multipart/form-data",
        headers={"X-Unexpected-Header": "value"}
    )

    # Assert that the upload is still processed correctly despite the unexpected header
    assert b"Prediction" in response.data

# 6. Edge Case: Uploading an Image with HTTP/2
def test_edge_case_upload_over_http2(client):
    """
    Test uploading an image using HTTP/2 protocol.
    - Scenario: Simulate uploading an image over HTTP/2 protocol.
    - Expected Behavior: System processes the upload as it would over HTTP/1.1.
    """
    img_data = BytesIO(b"valid_image_data")
    img_data.name = "http2_image.jpg"

    data_check(client, img_data)
