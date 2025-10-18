from flask import Flask, jsonify
from datetime import datetime as dt, timezone
import requests
from flask_cors import CORS
import logging

# Initialize flask app
app = Flask(__name__)

# Enables CORS for all routes
CORS(app)

# Configure logging
logging.basicConfig(
    level = logging.INFO,
    format = '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
)
logger = logging.getLogger(__name__)

catapi_url = "https://catfact.ninja/fact"

@app.route('/')
def health_status():
    return jsonify({"status": "OK"}), 200

# the view function for the function is located at endpoint /me
@app.route('/me')
def profile_details():
    
    try:
        logger.info("Fetching cat fact from external API...")
        response = requests.get(catapi_url, timeout = 2)
        response.raise_for_status()
        cat_fact = response.json()
        logger.info("Cat fact fetched successfully.")
        
    # catches request timeout error
    except requests.exceptions.Timeout:
        logger.error("The request in Cat Facts API timed out.")
        return jsonify({
            "error": "The request timed out, please try again later."
        }), 504
        
    # catches httpError if the requests returns an unsuccessful status code
    except requests.exceptions.HTTPError as http_error:
        logger.error(f"http error occured: {http_error}")
        return jsonify({
            "error": f"http error occured: {http_error}"
        }), 502
        
    # catches any other error encountered
    except Exception as err:
        logger.exception(f"Unexpected error: {err}")
        return jsonify({"error": f"other error occured: {err}"}), 500
    
    
    expected_response = {
        "status": "success",
        "user": {
            "email": "adefioye.ayomidej@gmail.com",
            "name": "Adefioye Ayomide James",
            "stack": "Python/Flask"
        },
        
        # timestamp in ISO format
        "timestamp": dt.now(timezone.utc).isoformat(timespec='milliseconds').replace("+00:00", "Z"),
        "fact": cat_fact['fact']
    }
    logger.info("Returning successful response to client.")
    return jsonify(expected_response), 200
    
    
    
if __name__ == "__main__":
    app.run()