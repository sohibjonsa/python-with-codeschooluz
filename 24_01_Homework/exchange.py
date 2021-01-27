import requests
from pprint import pprint

def currency_RUB(a,b):
    for i in range(a, b):
        parameters = f'{i+1}-12-31?symbols=RUB'
        url = f"https://api.exchangeratesapi.io/{parameters}"
        r = requests.get(url)

        data1 = r.json()
        pprint(data1)
currency_RUB(1998, 2021)


