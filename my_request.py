import requests

url = 'https://rickandmortyapi.com/api/character'

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

#print(response.json())
respuesta_json = response.json()
info = respuesta_json['info']
personajes = respuesta_json['results']

for name in respuesta_json['results']:

    print(name['name'])

    for personaje in personajes:
        print(f"The character {personaje['name']} is {personaje['status']}")