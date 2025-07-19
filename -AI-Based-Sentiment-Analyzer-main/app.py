from flask import Flask, request, jsonify, render_template
from sentiment_analysis_new import analyze_sentiment
from db_operations import Database
import logging

app = Flask(__name__)
db = Database()  # Initialize the database connection

# Set up logging
logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    return render_template("index.html")  # Serve the HTML file

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    
    # Check if 'text' is provided in the request data and is a valid string
    if "text" not in data or not isinstance(data["text"], str) or not data["text"].strip():
        return jsonify({"error": "Invalid or missing 'text' key in the request data."}), 400
    
    logging.info(f"Received data: {data}")  # Log the incoming data

    try:
        # Analyze sentiment
        result = analyze_sentiment(data["text"])
        
        # Check if the result is valid
        if not isinstance(result, dict) or "label" not in result or "score" not in result:
            raise ValueError("Invalid sentiment analysis result structure.")
        
        logging.info(f"Sentiment analysis result: {result}")  # Log the result

        # Debug log for backend
        print(f"Returning result: {result}")  # Print result for debugging
        
        # Insert into the database (simulated)
        db.insert_review(data["text"], result)

        # Return the result to the client
        return jsonify(result)

    except Exception as e:
        logging.error(f"Error during analysis: {e}")
        return jsonify({"error": "An error occurred during analysis."}), 500

@app.route('/favicon.ico')
def favicon():
    return '', 204

if __name__ == "__main__":
    app.run(debug=True)