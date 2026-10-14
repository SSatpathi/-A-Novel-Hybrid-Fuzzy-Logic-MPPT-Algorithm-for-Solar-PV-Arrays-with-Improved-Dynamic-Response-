import requests

r = requests.get('https://api.example.com/data')
if r.status_code == 200:
    data = r.json()
    print(data)
