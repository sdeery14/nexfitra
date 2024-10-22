import pytest
from app import app

# Define a pytest fixture named 'client' that sets up a test client for the Flask app
@pytest.fixture
def client():
    # Use the Flask app's test client for the duration of the test
    with app.test_client() as client:
        yield client  # Provide the test client to the test functions

# Define a test function that uses the 'client' fixture
def test_hello(client):
    # Send a GET request to the root URL of the Flask app
    response = client.get('/')
    
    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200
    
    # Assert that the response JSON data matches the expected dictionary
    assert response.get_json() == {"message": "Hello from Flask!"}