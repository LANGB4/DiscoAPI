import requests


BASE = 'http://127.0.0.1:5000/'


data = [{'name': 'Bundeshaus', 'text': 'sch schono schoen so', 'zip': 3012},
        {'name': 'KIndlifresserbrunnen', 'text': 'Hmmm.. chindli', 'zip': 3001},
        {'name': 'Rosengarten', 'text': 'Guns n rosengardens', 'zip': 3082},]

for i in range(len(data)):
    response = requests.put(BASE + 'sight/'+str(i), data[i])
    print('RESPONSE, PUT---->', response.json())

input('press enter to delete')
response = requests.delete(BASE + 'video/1')
print('RESPONSE, DELETE---->', response)

input('press enter to get')
response = requests.get(BASE + 'sight/1')
print('RESPONSE, GET---->', response.json())
