"""
This module sets up a basic Flask web application.

Routes:
    /: Returns a JSON response with a greeting message.

Functions:
    hello(): Handles the root route and returns a JSON response.

Usage:
    Run this module directly to start the Flask web server on host '0.0.0.0' and port '5000'.
"""

# Import Flask and jsonify from the flask package
from flask import Flask, jsonify

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL ('/')
@app.route('/')
def hello():
    # Return a JSON response with a greeting message
    return jsonify(message="Hello from Flask!")

# Check if the script is run directly (and not imported as a module)
if __name__ == '__main__':
    # Run the Flask web server on host '0.0.0.0' and port '5000'
    app.run(host='0.0.0.0', port=5000)
