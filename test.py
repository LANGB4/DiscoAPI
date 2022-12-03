import requests


BASE = 'http://127.0.0.1:5000/'

response = requests.put(BASE + 'sight/1', {'name': 'Bundeshaus'})#, 'text': 'sch schono schön so', 'zip': 3012})



print('RESPONSE---->', response.json())

