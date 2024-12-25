from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    print('In webhook')
    data = request.json  # Parse the JSON payload
    print(data)  # Log the data for debugging
    # Process data and push to BigQuery
    return "Received", 200

if __name__ == "__main__":
    app.run(port=5000)