import requests

from pprint import pprint

def currency_RUB(a,b):
    l=[]
    for i in range(a, b):
        parameters = f'{i+1}-12-31?symbols=RUB'
        url = f"https://api.exchangeratesapi.io/{parameters}"
        r = requests.get(url)
        data1 = r.json()
        l.append(data1)
    return l
c = currency_RUB(1998, 2021)

print(c)

