import requests

base_url = "https://pokeapi.co/api/v2/"

def get_poke_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")

pokemon_name = input("Enter a pokemon: ")
pokemon_info = get_poke_info(pokemon_name)

if pokemon_info:
    print(f"{pokemon_info["height"]}")