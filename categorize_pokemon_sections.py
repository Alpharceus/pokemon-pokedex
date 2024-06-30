import json

# Define lists for pseudo-legendaries and legendaries
pseudo_legendaries = [
    "Dratini", "Dragonair","Dragonite", "Larvitar", "Pupitar","Tyranitar", "Bagon", "Shelgon","Salamence", "Beldum", "Metang","Metagross", "Gible", "Gabite","Garchomp",
    "Deino", "Zweilous", "Hydreigon", "Goomy", "Sliggoo", "Goodra", "Jangmo-o", "Hakamo-o","Kommo-o", "Dreepy", "Drakloak"," Dragapult"
]

legendaries = [
    "Articuno", "Zapdos", "Moltres", "Mewtwo", "Raikou", "Entei", "Suicune",
    "Lugia", "Ho-oh", "Celebi", "Regirock", "Regice", "Registeel", "Latias",
    "Latios", "Kyogre", "Groudon", "Rayquaza", "Jirachi", "Deoxys", "Uxie",
    "Mesprit", "Azelf", "Dialga", "Palkia", "Heatran", "Regigigas", "Giratina",
    "Cresselia", "Tornadus", "Thundurus", "Landorus", "Reshiram", "Zekrom",
    "Kyurem", "Genesect", "Xerneas", "Yveltal", "Zygarde", "Tapu Koko",
    "Tapu Lele", "Tapu Bulu", "Tapu Fini", "Cosmog", "Cosmoem","Solgaleo", "Lunala", "Nihilego",
    "Buzzwole", "Pheromosa", "Xurkitree", "Celesteela", "Kartana", "Guzzlord",
    "Necrozma", "Magearna", "Marshadow", "Blacephalon", "Zacian", "Zamazenta",
    "Eternatus", "Kubfu", "Urshifu", "Regieleki", "Regidrago", "Glastrier",
    "Spectrier", "Calyrex"
]

def categorize_pokemon():
    # Load Pokémon data from categorized_pokemon.json
    with open('categorized_pokemon.json', 'r') as file:
        pokemon_data = json.load(file)

    categorized_data = {}
    for gen, categories in pokemon_data.items():
        categorized_data[gen] = {"normal": [], "pseudo_legendaries": [], "legendaries": []}
        for category, pokemons in categories.items():
            for pokemon in pokemons:
                if pokemon["name"].capitalize() in legendaries:
                    categorized_data[gen]["legendaries"].append(pokemon)
                elif pokemon["name"].capitalize() in pseudo_legendaries:
                    categorized_data[gen]["pseudo_legendaries"].append(pokemon)
                else:
                    categorized_data[gen]["normal"].append(pokemon)
    
    return categorized_data

def save_categorized_data(categorized_data, file_path):
    with open(file_path, 'w') as file:
        json.dump(categorized_data, file, indent=4)
    print(f"Categorized Pokémon data saved to {file_path}")

if __name__ == "__main__":
    # Categorize Pokémon by sections
    categorized_data = categorize_pokemon()

    # Save categorized data to the same JSON file
    save_categorized_data(categorized_data, 'categorized_pokemon2.json')
