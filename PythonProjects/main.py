import requests

URL = 'https://api.pokemonbattle.me/v2'
HEADERS = {'Content-Type' : 'application/json' , 'trainer_token' : 'ТОКЕН'}
TOKEN = 'ТОКЕН'

body = {
    "name": "Кекушка",
    "photo": "https://dolnikov.ru/pokemons/albums/009.png"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body)

print(response.text)

body_new_pokemon_name = {
    "pokemon_id": "15315",
    "name": "Чебурек",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}

response_pokemon_name = requests.put(url = f'{URL}/pokemons', headers = HEADERS, json = body)

print(response_pokemon_name.text)

body_pokeball = {
    "pokemon_id": "15315"
}

response_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADERS, json = body_pokeball)

print(response_pokeball.text)