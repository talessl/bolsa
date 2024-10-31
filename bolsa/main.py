import requests
from chave import chave_api
import pandas as pd
from io import StringIO
from  texttable import Texttable

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=QETH11.SAO&apikey={chave_api}&datatype=csv'
r = requests.get(url)
# print(r.text)

tabela = pd.read_csv(StringIO(r.text))
