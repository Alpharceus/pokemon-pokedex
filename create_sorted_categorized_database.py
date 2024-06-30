import json

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to {file_path}")

def create_sorted_categorized_database(sorted_file, categorized_file, output_file):
    sorted_pokemon_data = load_json(sorted_file)
    categorized_pokemon_data = load_json(categorized_file)

    new_categorized_data = {}

    for gen, sorted_pokemons in sorted_pokemon_data.items():
        new_categorized_data[gen] = {"normal": [], "pseudo_legendaries": [], "legendaries": []}

        # Create a dictionary for quick lookup of pokedex numbers
        pokedex_dict = {pokemon['name']: pokemon['pokedex_number'] for pokemon in sorted_pokemons}

        for category in ["normal", "pseudo_legendaries", "legendaries"]:
            pokemons = categorized_pokemon_data[gen][category]
            # Attach pokedex numbers to the pokemons
            pokemons_with_pokedex = [
                {**pokemon, "pokedex_number": pokedex_dict[pokemon["name"]]}
                for pokemon in pokemons if pokemon["name"] in pokedex_dict
            ]
            # Sort the pokemons by their pokedex numbers
            sorted_pokemons_with_pokedex = sorted(pokemons_with_pokedex, key=lambda x: x["pokedex_number"])
            # Remove the pokedex number from the final output
            final_sorted_pokemons = [{k: v for k, v in pokemon.items() if k != "pokedex_number"} for pokemon in sorted_pokemons_with_pokedex]

            new_categorized_data[gen][category] = final_sorted_pokemons

    save_json(new_categorized_data, output_file)

if __name__ == "__main__":
    create_sorted_categorized_database('sorted_pokemon_by_pokedex.json', 'categorized_pokemon2.json', 'final_sorted_categorized_pokemon.json')
