import requests

r = requests.get('https://randomuser.me/api/?results=5')

data = r.json()['results']

for i in data:
    print(i['name'])