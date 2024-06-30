import requests
import json

def fetch_pokedex_number(pokemon_name):
    try:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}")
        response.raise_for_status()
        data = response.json()
        return data['id']
    except Exception as e:
        print(f"Error fetching Pokédex number for {pokemon_name}: {e}")
        return None

def manual_pokedex_number_input(pokemon_name):
    pokedex_number = input(f"Enter the Pokédex number for {pokemon_name}: ").strip()
    return int(pokedex_number)

def fetch_and_sort_pokemon_by_pokedex():
    # Load Pokémon names from pokemon_generations.json
    with open('pokemon_generations.json', 'r') as file:
        pokemon_names = json.load(file)

    sorted_pokemon_data = {}
    for gen, names in pokemon_names.items():
        pokemons_with_numbers = []
        for name in names:
            pokedex_number = fetch_pokedex_number(name)
            if pokedex_number is None:
                pokedex_number = manual_pokedex_number_input(name)
            pokemons_with_numbers.append({"name": name, "pokedex_number": pokedex_number})

        # Sort Pokémon by their Pokédex numbers
        sorted_pokemons = sorted(pokemons_with_numbers, key=lambda x: x["pokedex_number"])
        sorted_pokemon_data[gen] = sorted_pokemons

    return sorted_pokemon_data

def save_sorted_pokemon_data(sorted_pokemon_data, file_path):
    with open(file_path, 'w') as file:
        json.dump(sorted_pokemon_data, file, indent=4)
    print(f"Sorted Pokémon data saved to {file_path}")

if __name__ == "__main__":
    # Fetch and sort Pokémon by their Pokédex numbers
    sorted_pokemon_data = fetch_and_sort_pokemon_by_pokedex()

    # Save sorted data to a new JSON file
    save_sorted_pokemon_data(sorted_pokemon_data, 'sorted_pokemon_by_pokedex.json')
