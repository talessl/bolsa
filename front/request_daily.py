import requests
from key import chave_api
import pandas as pd
from io import StringIO

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=NVDC34.SAO&apikey={chave_api}&datatype=csv'
r = requests.get(url)

tabela = pd.read_csv(StringIO(r.text))
print(tabela)