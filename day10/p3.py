import requests

res=requests.put('https://httpbin.org/post', data={'key': 'value'})

print("Status code:", res.status_code)
# Print content of response (parsed as JSON)
print("Response body:",res.content.decode()) 