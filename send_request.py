import requests

url = 'http://127.0.0.1:5000/predict'  # Replace with your actual URL

# Sample data for prediction
data = {'data': [{'budget': 10000000, 'popularity': 50}]}

# Send POST request with JSON data
response = requests.post(url, json=data)

try:
    # Try to parse the response JSON
    json_response = response.json()
    print(json_response)
except Exception as e:
    # Print the raw response content if JSON parsing fails
    print(f"Error: {e}")
    print("Raw Response:")
    print(response.text)
