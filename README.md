# myReceiptProcessor

Build a webservice that fulfils the documented API. The API is described below. A formal definition is provided in the api.yml file. We will use the described API to test your solution.

Provide any instructions required to run your application.

Data does not need to persist when your application stops. It is sufficient to store information in memory. There are too many different database solutions, we will not be installing a database on our system when testing your application.

Language Selection
You can assume our engineers have Go and Docker installed to run your application. Go is our preferred language, but choosing it will not give you an advantage in the evaluation. If you are not using Go, include a Dockerized setup to run the code. You should also provide detailed instructions if your Docker file requires any additional configuration to run the application.

Summary of API Specification:

The Fetch Rewards Receipt Processor is a Flask-based API that processes digital receipts and calculates reward points based on specific rules. It provides endpoints to submit receipts and retrieve the associated reward points, offering a streamlined way to manage and track digital transactions.

Features
📥 Receipt Submission: Accepts receipt data in JSON format.

🎯 Points Calculation: Computes reward points based on purchase details.

📊 Retrieve Points: Allows users to fetch points for a given receipt ID.

🚀 Dockerized Deployment: Easily deployable using Docker.

Endpoints
1. Process a Receipt
URL: /receipts/process

Method: POST

Request Body Example:

json
Copy
Edit
{
  "retailer": "Walmart",
  "purchaseDate": "2025-03-27",
  "items": [
    {"name": "Milk", "price": 3.99},
    {"name": "Eggs", "price": 2.99}
  ]
}
Response:

json
Copy
Edit
{ "id": "123e4567-e89b-12d3-a456-426614174000" }
2. Retrieve Receipt Points
URL: /receipts/<receipt_id>/points

Method: GET

Response Example:

json
Copy
Edit
{ "points": 50 }
Tech Stack
🐍 Python (Flask)

🐳 Docker (Containerized deployment)

🔥 Postman (API Testing)

Setup & Running Locally
Clone the repo:

git clone https://github.com/your-username/fetch-rewards-receipt-processor.git
cd fetch-rewards-receipt-processor
Install dependencies:

For Requirements.txt
pip install -r requirements.txt

Run the Flask app:
python server_main.py
Test with Postman using http://localhost:5000/receipts/process.
