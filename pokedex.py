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
