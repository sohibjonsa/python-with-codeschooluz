import requests

r = requests.get('https://randomuser.me/api/?results=5&gender=male&nat=us')

data = r.json()['results']

for i in data:
    print(i['name']['first'], i['gender'], i['nat'])