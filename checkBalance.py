import requests
import json

api_access_token = 'fdca749516f6fde2f5df9da2c0109c20' # токен можно получить здесь https://qiwi.com/api
my_login = '+79788264777' # номер QIWI Кошелька в формате +79991112233

s = requests.Session()
s.headers['authorization'] = 'Bearer ' + api_access_token
parameters = {'rows': '10'}
h = s.get('https://edge.qiwi.com/funding-sources/v1/accounts/current')
parsed = json.loads(h.text)
print(parsed['accounts'][0]['balance'])
