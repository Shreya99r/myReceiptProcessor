from flask import Flask, request, jsonify
import sys
print(sys.path)
sys.path.append("D:\Fetch_Receipt_Processor\myReceiptProcessor")
import uuid
from utils import calculate_retailer_points
from input_validation import validate_receipt

# app = Flask(_name_)
app = Flask(__name__)

# Dictionary to store receipt IDs and their corresponding points
receipts = {}


@app.route("/receipts/process", methods=["POST"])
def handle_receipt_submission():
    # Retrieve JSON data from the request
    receipt_data = request.get_json()

    # Validate the received receipt data
    validation = validate_receipt(receipt_data)

    # If the receipt data is invalid, return an error response
    if not validation.is_valid:
        return jsonify({"error": "Receipt validation failed", "details": validation.message}), 400

    # Generate a unique receipt ID and calculate points
    receipt_id = str(uuid.uuid4())
    points = calculate_retailer_points(receipt_data)

    # Store the receipt ID and its points in the dictionary
    receipts[receipt_id] = points

    # Return the generated receipt ID with a success status
    return jsonify({"id": receipt_id}), 201


@app.route("/receipts/<receipt_id>/points", methods=["GET"])
def retrieve_receipt_points(receipt_id):
    # Check if the requested receipt ID exists in the store
    if receipt_id not in receipts:
        return jsonify({"error": "Receipt ID does not exist"}), 404

    # Return the points associated with the requested receipt ID
    return jsonify({"points": receipts[receipt_id]}), 200


if __name__ == "__main__":
    # Start the Flask application on all available network interfaces at port 5000
    app.run(host="0.0.0.0",port=5000)