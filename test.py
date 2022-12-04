import requests


BASE = 'http://127.0.0.1:5000/'


data = [{'name': 'Bundeshaus', 'text': 'sch schono schoen so', 'zip': 3012},
        {'name': 'KIndlifresserbrunnen', 'text': 'Hmmm.. chindli', 'zip': 3001},
        {'name': 'Rosengarten', 'text': 'Guns n rosengardens', 'zip': 3082},]

response = requests.patch(BASE + 'sight/2', {'text': 'Guguguns n rosengardens', 'zip': 9999})
print('PATCH---->',response.json())

response = requests.get(BASE + 'sight/2')
print('GET---->',response.json())

response = requests.patch(BASE + 'sight/2', {'text': 'Guns n rosengardens', 'zip': 3000})
print('PATCH---->',response.json())


response = requests.get(BASE + 'sight/2')
print('GET---->',response.json())


for i in range(5):
    response = requests.get(BASE + 'sight/'+str(i))
    print('RESPONSE, GET---->','id: ',i, response.json())