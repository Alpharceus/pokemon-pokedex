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
    git clone https://github.com/Alpharceus/pokemon-pokedex.git
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
```
### Step 2: Fetching and Sorting by Pokédex Numbers

We created a script to fetch Pokédex numbers and sort Pokémon within each generation:

```python
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

    sorted_pokemons = sorted(pokemons_with_numbers, key=lambda x: x["pokedex_number"])
    sorted_pokemon_data[gen] = sorted_pokemons

# Save sorted data to a new JSON file
with open('sorted_pokemon_by_pokedex.json', 'w') as file:
    json.dump(sorted_pokemon_data, file, indent=4)
```

### Step 3: Categorizing Pokémon into Sections

We created a script to categorize Pokémon into normal, pseudo-legendaries, and legendaries:

```python
import json

# Define lists for pseudo-legendaries and legendaries
pseudo_legendaries = [
    "Dragonite", "Tyranitar", "Salamence", "Metagross", "Garchomp",
    "Hydreigon", "Goodra", "Kommo-o", "Dragapult"
]

legendaries = [
    "Articuno", "Zapdos", "Moltres", "Mewtwo", "Raikou", "Entei", "Suicune",
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

# Load Pokémon data from categorized_pokemon2.json
with open('categorized_pokemon2.json', 'r') as file:
    pokemon_data = json.load(file)

categorized_data = {}
for gen, categories in pokemon_data.items():
    categorized_data[gen] = {"normal": [], "pseudo_legendaries": [], "legendaries": []}
    for category, pokemons in categories.items():
        for pokemon in pokemons:
            name = pokemon["name"].capitalize()
            if name in legendaries:
                categorized_data[gen]["legendaries"].append(pokemon)
            elif name in pseudo_legendaries:
                categorized_data[gen]["pseudo_legendaries"].append(pokemon)
            else:
                categorized_data[gen]["normal"].append(pokemon)

# Save categorized data to a new JSON file
with open('final_sorted_categorized_pokemon.json', 'w') as file:
    json.dump(categorized_data, file, indent=4)

```

Step 4: Creating the Pokédex Interface

We created a Tkinter-based graphical interface to display the Pokémon data:

```python
import os
import tkinter as tk
from tkinter import Button, Label, Canvas, Scrollbar, Frame
from PIL import Image, ImageTk
import json

# Directory containing the images
image_dir = "pokemon_images"

# Define type colors
type_colors = {
    "Flying": "skyblue",
    "Fire": "red",
    "Ice": "turquoise",
    "Water": "blue",
    "Normal": "grey",
    "Electric": "yellow",
    "Grass": "green",
    "Psychic": "purple",
    "Poison": "purple4",
    "Ground": "sienna",
    "Rock": "saddlebrown",
    "Bug": "chartreuse",
    "Ghost": "indigo",
    "Steel": "lightsteelblue",
    "Dragon": "blueviolet",
    "Dark": "darkslategray",
    "Fairy": "pink",
    "Fighting": "orangered",
}

def fetch_pokemon_image(name):
    file_name = name.lower() + ".png"
    image_path = os.path.join(image_dir, file_name)
    if os.path.exists(image_path):
        image = Image.open(image_path)
        image.thumbnail((100, 100), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(image)
    return None

def create_type_button(parent, type_name):
    color = type_colors.get(type_name, "white")
    button = Button(parent, text=type_name, bg=color, width=10)
    button.pack(side="left", padx=2)
    return button

def toggle_highlight(button):
    if button.config('bg')[-1] == 'yellow':
        button.config(bg=button.original_bg)
    else:
        button.config(bg='yellow')

def create_pokedex(root):
    global canvas
    canvas = Canvas(root)
    scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    row = 0

    # Load Pokémon data from final_sorted_categorized_pokemon.json
    with open('final_sorted_categorized_pokemon.json', 'r') as file:
        pokemon_data = json.load(file)

    for gen, categories in pokemon_data.items():
        gen_label = Label(scrollable_frame, text=gen, font=("Helvetica", 20, "bold"))
        gen_label.grid(row=row, column=0, columnspan=4, pady=10)
        row += 1

        for category, pokemons in categories.items():
            category_label = Label(scrollable_frame, text=category.replace("_", " ").capitalize(), font=("Helvetica", 16, "italic"))
            category_label.grid(row=row, column=0, columnspan=4, pady=5)
            row += 1
            col = 0

            for pokemon in pokemons:
                image = fetch_pokemon_image(pokemon["name"])
                button_text = f"{pokemon['name']}"
                button = Button(scrollable_frame, text=button_text, image=image, compound="top")
                button.image = image  # Keep a reference to avoid garbage collection
                button.original_bg = 'green' if category == 'normal' else ('red' if category == 'pseudo_legendaries' else 'blue')
                button.config(bg=button.original_bg, command=lambda b=button: toggle_highlight(b))
                button.grid(row=row, column=col, padx=5, pady=5)

                type_frame = Frame(scrollable_frame)
                type_frame.grid(row=row+1, column=col, padx=5, pady=5)
                for type_name in pokemon["type"]:
                    create_type_button(type_frame, type_name)

                col += 1
                if col == 4:
                    col = 0
                    row += 2
            row += 2

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Bind mouse wheel events to the canvas
    canvas.bind_all("<MouseWheel>", on_mouse_wheel)

def on_mouse_wheel(event):
    global canvas
    canvas.yview_scroll(-1 * int(event.delta / 120), "units")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Pokédex")
    create_pokedex(root)
    root.mainloop()

```

## Manual Image Download Process

For Pokémon images that could not be fetched from the library, we manually downloaded the images:

1. **Search for the Pokémon images** on Google or any preferred website.
2. **Save the images** in the `pokemon_images` directory.
3. **Ensure the images are named correctly** (all lowercase, with `.png` extension).

## Conclusion

This project provides a comprehensive Pokémon Pokédex application with a detailed graphical interface. Future updates aim to include mythical Pokémon, enhanced graphical features, and more detailed Pokémon information. This README details each step involved in creating the Pokédex, making it easier to understand and follow the process.

Feel free to contribute and enhance the Pokédex application further!

## First Application: Legendaries in Pokémon Sword and Shield

The first application we built focused on the legendaries in Pokémon Sword and Shield. This application specifically highlighted the legendary Pokémon available in these games, categorized by their presence in Sword (SW) and Shield (SH). The application featured:

- **Categorization by Version**: Pokémon were categorized based on their availability in Pokémon Sword or Shield.
- **Highlighting Functionality**: Users could click on a Pokémon to highlight it, with different colors indicating different categories.
- **Image Display**: Pokémon images were fetched and displayed alongside their names and types.
- **Type Buttons**: Color-coded buttons were used to indicate Pokémon types, enhancing the visual appeal and usability of the application.

This initial application laid the groundwork for the comprehensive Pokédex project, incorporating essential features such as image fetching, type display, and user interaction.

### Key Features of the First Application

- **Version-Specific Categorization**: Clear differentiation between Pokémon available in Sword and Shield.
- **Interactive Interface**: Users could interact with the Pokémon entries, highlighting their selections.
- **Type Display**: Visual representation of Pokémon types using color-coded buttons.

The development of this initial application provided valuable insights and a solid foundation for expanding the project to include all generations and categories of Pokémon.

### Future Enhancements for the First Application

- **Include Mythical Pokémon**: Add mythical Pokémon available in Sword and Shield.
- **Improve Graphical Interface**: Enhance the UI for a better user experience.
- **Additional Details**: Display Pokémon stats, abilities, and other relevant information.
- **Version Variants**: Show different forms of Pokémon specific to Sword and Shield.

By building on the initial application, we aim to create a more detailed and user-friendly experience for Pokémon enthusiasts.
