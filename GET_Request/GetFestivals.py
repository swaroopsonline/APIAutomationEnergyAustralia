import requests
import json
import jsonpath

# API URL
url = "https://eacp.energyaustralia.com.au/codingtest/api/v1/festivals"

# Send Get Request
response = requests.get(url)

# Display the response code
print(response)

# Display response Content
print(response.content)

# Display Response header
print(response.headers)

# Parse response to Json format
json_response = json.loads(response.text)
print(json_response)





