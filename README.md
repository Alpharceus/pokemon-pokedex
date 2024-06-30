# pokemon-pokedex

# Pokémon Pokédex Application

## Overview

This project aims to create a comprehensive Pokémon Pokédex application. The application displays Pokémon images, types, and other relevant information, categorized by generation, pseudo-legendaries, legendaries, and normal Pokémon. The project involves fetching data from the PokéAPI, sorting and categorizing Pokémon, and creating a user-friendly graphical interface using Tkinter.

## Features

- Display Pokémon by generation
- Categorize Pokémon into normal, pseudo-legendaries, and legendaries
- Fetch and display Pokémon images
- Highlight Pokémon when selected
- Show Pokémon types with color-coded buttons

### Future Updates

- Include mythical Pokémon
- Enhance the graphical interface
- Display Pokémon stats
- Include different versions of Pokémon (e.g., Alolan, Galarian forms)
- Fetch and display Pokémon evolutions
- Add search functionality
- Improve image fetching and handling

## Prerequisites

- Python 3.x
- Requests library: `pip install requests`
- Pillow library: `pip install pillow`
- Tkinter (usually included with Python installations)

## Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/pokemon-pokedex.git
    cd pokemon-pokedex
    ```

2. **Install the required libraries**:
    ```bash
    pip install requests pillow
    ```

3. **Ensure you have the following files**:
    - `pokemon_generations.json`
    - `categorized_pokemon2.json`
    - `final_sorted_categorized_pokemon.json`
    - `pokemon_images` directory with Pokémon images

## Steps and Accomplishments

### Step 1: Fetching Pokémon Types

We created a script to fetch Pokémon types from the PokéAPI and manually input types if not found:

```python
import requests
import json

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

# Load Pokémon names from pokemon_generations.json
with open('pokemon_generations.json', 'r') as file:
    pokemon_names = json.load(file)

categorized_data = {}
for gen, names in pokemon_names.items():
    categorized_data[gen] = {"normal": [], "pseudo_legendaries": [], "legendaries": []}
    for name in names:
        types = fetch_pokemon_types(name)
        if not types:
            types = manual_type_input(name)
        categorized_data[gen]["normal"].append({"name": name, "type": types})

# Save categorized data to a new JSON file
with open('categorized_pokemon2.json', 'w') as file:
    json.dump(categorized_data, file, indent=4)
