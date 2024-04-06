import requests

URL = 'https://api.pokemonbattle.me/v2'
HEADERS = {'Content-Type' : 'application/json' , 'trainer_token' : '36092d975e5d61f74193d73c94213814'}
TOKEN = '36092d975e5d61f74193d73c94213814'


body_pokeball = {
    "pokemon_id": "15315"
}

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADERS, json = body_pokeball)

print(response_pokeball.text)
