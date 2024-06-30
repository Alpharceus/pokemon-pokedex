import requests
import json

# Define lists for pseudo-legendaries and legendaries
pseudo_legendaries = [
    "Dragonite", "Tyranitar", "Salamence", "Metagross", "Garchomp",
    "Hydreigon", "Goodra", "Kommo-o", "Dragapult"
]

legendaries = [
    "Articuno", "zapdos", "Moltres", "Mewtwo", "Raikou", "Entei", "Suicune",
    "Lugia", "Ho-oh", "Celebi", "Regirock", "Regice", "Registeel", "Latias",
    "Latios", "Kyogre", "Groudon", "Rayquaza", "Jirachi", "Deoxys", "Uxie",
    "Mesprit", "Azelf", "Dialga", "Palkia", "Heatran", "Regigigas", "Giratina",
    "Cresselia", "Tornadus", "Thundurus", "Landorus", "Reshiram", "Zekrom",
    "Kyurem", "Genesect", "Xerneas", "Yveltal", "Zygarde", "Tapu Koko",
    "Tapu Lele", "Tapu Bulu", "Tapu Fini", "Solgaleo", "Lunala", "Nihilego",
    "Buzzwole", "Pheromosa", "Xurkitree", "Celesteela", "Kartana", "Guzzlord",
    "Necrozma", "Magearna", "Marshadow", "Blacephalon", "Zacian", "Zamazenta",
    "Eternatus", "Kubfu", "Urshifu", "Regieleki", "Regidrago", "Glastrier",
    "Spectrier", "Calyrex"
]

def fetch_pokemon_types(pokemon_name):
    try:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}")
        response.raise_for_status()
        data = response.json()
        types = [t['type']['name'].capitalize() for t in data['types']]
        return types
    except Exception as e:
        print(f"Error fetching types for {pokemon_name}: {e}")
        return None

def manual_type_input(pokemon_name):
    print(f"Could not fetch types for {pokemon_name}.")
    is_dual_type = input("Is this Pokémon a dual type? (yes/no): ").strip().lower()
    if is_dual_type == 'yes':
        type1 = input(f"Enter the first type for {pokemon_name}: ").strip().capitalize()
        type2 = input(f"Enter the second type for {pokemon_name}: ").strip().capitalize()
        return [type1, type2]
    else:
        type1 = input(f"Enter the type for {pokemon_name}: ").strip().capitalize()
        return [type1]

def categorize_pokemon(pokemon_names):
    categorized_data = {}
    for gen, names in pokemon_names.items():
        categorized_data[gen] = {"normal": [], "pseudo_legendaries": [], "legendaries": []}
        for name in names:
            types = fetch_pokemon_types(name)
            if not types:
                types = manual_type_input(name)
            pokemon_entry = {"name": name, "type": types}
            if name in legendaries:
                categorized_data[gen]["legendaries"].append(pokemon_entry)
            elif name in pseudo_legendaries:
                categorized_data[gen]["pseudo_legendaries"].append(pokemon_entry)
            else:
                categorized_data[gen]["normal"].append(pokemon_entry)
    return categorized_data

def save_categorized_data(categorized_data, file_path):
    with open(file_path, 'w') as file:
        json.dump(categorized_data, file, indent=4)
    print(f"Categorized Pokémon data saved to {file_path}")

if __name__ == "__main__":
    # Load Pokémon names from pokemon_generations.json
    with open('pokemon_generations.json', 'r') as file:
        pokemon_names = json.load(file)

    # Categorize Pokémon by types and sections
    categorized_data = categorize_pokemon(pokemon_names)

    # Save categorized data to a new JSON file
    save_categorized_data(categorized_data, 'categorized_pokemon.json')
