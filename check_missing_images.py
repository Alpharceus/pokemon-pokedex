import os
import json

def load_pokemon_names_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def check_missing_images(pokemon_data, image_folder):
    missing_pokemon = []
    for generation, pokemon_list in pokemon_data.items():
        for pokemon in pokemon_list:
            image_path = os.path.join(image_folder, f"{pokemon}.png")
            if not os.path.exists(image_path):
                print(f"Image missing for {pokemon}")
                missing_pokemon.append(pokemon)
    return missing_pokemon

def save_missing_pokemon(missing_pokemon, file_path):
    with open(file_path, 'w') as file:
        for pokemon in missing_pokemon:
            file.write(f"{pokemon}\n")
    print(f"Missing Pokémon names have been saved to {file_path}")

if __name__ == "__main__":
    pokemon_data = load_pokemon_names_from_json('pokemon_generations.json')
    missing_pokemon = check_missing_images(pokemon_data, 'pokemon_images')

    if missing_pokemon:
        save_missing_pokemon(missing_pokemon, 'missing_images.txt')
    else:
        print("All Pokémon images are present.")
