import requests

r = requests.get('https://github.com/ShivamKr3696')

#r = requests.put('https://github.com/ShivamKr3696')

print("Status code:",r.status_code)

print("Responsen content:",r.content)