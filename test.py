import requests

r = requests.get('https://api.google.com/data')
if r.status_code == 200:
    data = r.json()
    print(data)
