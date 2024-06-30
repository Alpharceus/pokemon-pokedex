import requests
import json

# Define the API endpoint for fetching Pokémon by generation
generation_api_url = "https://pokeapi.co/api/v2/generation/"

def fetch_pokemon_by_generation():
    generations = {}
    
    # There are currently 8 generations in the PokéAPI
    for gen_id in range(1, 9):
        response = requests.get(f"{generation_api_url}{gen_id}")
        response.raise_for_status()
        data = response.json()
        
        generation_name = data['name'].replace('generation-', 'Generation ').capitalize()
        pokemon_species = data['pokemon_species']
        pokemon_names = [species['name'] for species in pokemon_species]
        
        generations[generation_name] = sorted(pokemon_names)

    return generations

def save_generations_to_json(generations, file_path):
    with open(file_path, 'w') as file:
        json.dump(generations, file, indent=4)
    print(f"Pokémon generations database saved to {file_path}")

if __name__ == "__main__":
    generations = fetch_pokemon_by_generation()
    save_generations_to_json(generations, 'pokemon_generations.json')
