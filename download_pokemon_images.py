import os
import requests
import json
from PIL import Image
from io import BytesIO

# Create a directory to save images
if not os.path.exists('pokemon_images'):
    os.makedirs('pokemon_images')

def fetch_pokemon_image_url(pokemon_name):
    try:
        search_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
        response = requests.get(search_url)
        response.raise_for_status()
        pokemon_data = response.json()
        image_url = pokemon_data["sprites"]["other"]["official-artwork"]["front_default"]
        return image_url
    except Exception as e:
        print(f"ERROR - Could not fetch image URL for {pokemon_name}: {e}")
        return None

def download_image(folder_path, url, file_name):
    try:
        image_content = requests.get(url).content
        image_file = BytesIO(image_content)
        image = Image.open(image_file)
        file_path = os.path.join(folder_path, file_name)

        with open(file_path, "wb") as f:
            image.save(f, "PNG")

        print(f"SUCCESS - saved {url} as {file_path}")
    except Exception as e:
        print(f"ERROR - Could not download {url} - {e}")

def load_pokemon_names_from_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

if __name__ == "__main__":
    pokemon_data = load_pokemon_names_from_json('pokemon_generations.json')
    missing_pokemon = []
    for generation, pokemon_list in pokemon_data.items():
        for pokemon in pokemon_list:
            print(f"Searching for {pokemon} images from {generation}")
            image_url = fetch_pokemon_image_url(pokemon)
            if image_url:
                download_image('pokemon_images', image_url, f"{pokemon}.png")
            else:
                print(f"No image found for {pokemon}")
                missing_pokemon.append(pokemon)

    # Save missing Pokémon names to a text file
    if missing_pokemon:
        with open('missing_pokemon.txt', 'w') as file:
            for pokemon in missing_pokemon:
                file.write(f"{pokemon}\n")
        print("Missing Pokémon names have been saved to missing_pokemon.txt")
    else:
        print("All Pokémon images were successfully downloaded.")
