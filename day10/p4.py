import requests

res=requests.delete('https://httpbin.org/delete', data={'key': 'value'})

print("Status code:", res.status_code)
# Print content of response (parsed as JSON)
print(res.json()) 