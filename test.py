import requests


BASE = 'http://127.0.0.1:5000/'


data = [{'name': 'Bundeshaus', 'text': 'sch schono schoen so', 'zip': 3012},
        {'name': 'KIndlifresserbrunnen', 'text': 'Hmmm.. chindli', 'zip': 3001},
        {'name': 'Rosengarten', 'text': 'Guns n rosengardens', 'zip': 3082},]

response = requests.delete(BASE + 'sight/2')
print('PATCH---->',response.json())

for i in range(5):
        response = requests.get(BASE + 'sight/'+str(i))
        print('id:',i,response.json())
