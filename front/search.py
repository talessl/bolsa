import requests
from key import chave_api

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = f'https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords=nvdc34&apikey={chave_api}'
r = requests.get(url)
data = r.json()

print(data)

# NVDC34.SAO