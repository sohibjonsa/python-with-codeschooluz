import requests
from pprint import pprint

def currency_RUB(a,b):
    for i in range(a, b):
        parameters = f'{i+1}-12-31?symbols=RUB'
        url = f"https://api.exchangeratesapi.io/{parameters}"
        r = requests.get(url)

        data = r.json()
       
    return data
    
p = currency_RUB(1998, 2021)

pprint(p)
