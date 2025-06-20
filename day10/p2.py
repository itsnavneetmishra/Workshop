import requests
# Making a POST request
r = requests.post('https://httpbin.org/post', data={'key': 'value'})
# Check status code
print("Status code:", r.status_code)
# Print content of response (parsed as JSON)
print(r.json())