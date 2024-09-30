"""
This module initializes a FastAPI application and defines a single route.

Routes:
    Returns a welcome message.

Functions:
    read_root()
    Handles GET requests to the root URL and returns a JSON response with a welcome message.
"""

# Import FastAPI from the fastapi package
from fastapi import FastAPI

# Create an instance of the FastAPI class
app = FastAPI()

# Define a route for the root URL ('/')
@app.get("/")
def read_root():
    # Return a JSON response with a welcome message
    return {"message": "Hello from FastAPI!"}
