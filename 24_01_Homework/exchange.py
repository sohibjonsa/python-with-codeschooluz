import requests
from pprint import pprint

r = requests.get('https://api.exchangeratesapi.io/latest')

data = r.json()['rates']['USD']
pprint(data)
# for i in data:
#     print(i['name'])