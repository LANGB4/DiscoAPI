import requests


BASE = 'http://127.0.0.1:5000/'


'''data = [{'name': 'Bundeshaus', 'text': 'sch schono schoen so', 'zip': 3012},
        {'name': 'KIndlifresserbrunnen', 'text': 'Hmmm.. chindli', 'zip': 3001},
        {'name': 'Rosengarten', 'text': 'Guns n rosengardens', 'zip': 3082},]

for i in range(len(data)):
    response = requests.put(BASE + 'sight/'+str(i), data[i])
    print('RESPONSE, PUT---->', response.json())



input('press enter to get')
for i in range(len(data)):
    response = requests.get(BASE + 'sight/'+str(i))
    print('RESPONSE, GET---->','id: ',i, response.json())


input('find inexistent id press enter')
response = requests.get(BASE + 'sight/28')
print('RESPONSE, GET---->', response.json())'''



response = requests.patch(BASE + 'sight/2', {'text': 'Guguguns n rosengardens', 'zip': 9999})
print('PATCH---->',response.json())


response = requests.get(BASE + 'sight/2')
print('GET---->',response.json())


response = requests.patch(BASE + 'sight/2', {})
print('PATCH---->',response.json())


response = requests.get(BASE + 'sight/2')
print('GET---->',response.json())