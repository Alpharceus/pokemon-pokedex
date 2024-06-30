import os
import tkinter as tk
from tkinter import Button, Label, Canvas, Scrollbar, Frame
from PIL import Image, ImageTk

# List of Pokémon by generation with SW and SH annotations
pokemon = {
    "Gen I": ["Articuno", "Zapdos", "Moltres", "Mewtwo"],
    "Gen II": ["Raikou", "Entei", "Suicune", "Lugia (SH)", "Ho-oh (SW)", "Celebi"],
    "Gen III": ["Regirock", "Regice", "Registeel", "Latias (SW)", "Latios (SH)", "Kyogre (SW)", "Groudon", "Rayquaza (SW)", "Jirachi", "Deoxys"],
    "Gen IV": ["Uxie", "Mesprit", "Azelf", "Dialga (SH)", "Palkia (SH)", "Heatran (SW)", "Regigigas", "Giratina (SH)", "Cresselia (SH)"],
    "Gen V": ["Tornadus (SW)", "Thundurus (SH)", "Landorus (SH)", "Reshiram (SH)", "Zekrom (SH)", "Kyurem (SW)", "Genesect"],
    "Gen VI": ["Xerneas", "Yveltal (SH)", "Zygarde (SH)"],
    "Gen VII": ["Tapu Koko (SH)", "Tapu Lele (SW)", "Tapu Bulu (SW)", "Tapu Fini (SW)", "Solgaleo", "Lunala", "Nihilego", "Buzzwole", "Pheromosa", "Xurkitree", "Celesteela (SH)", "Kartana", "Guzzlord", "Necrozma", "Magearna", "Marshadow", "Blacephalon"],
    "Gen VIII": ["Zacian", "Zamazenta", "Eternatus", "Kubfu", "Urshifu", "Regieleki", "Regidrago", "Glastrier", "Spectrier", "Calyrex"]
}

# Directory containing the images
image_dir = "pokemon_images_SWSH_legends"

def toggle_highlight(button):
    if button.config('bg')[-1] == 'yellow':
        if " (SW)" in button.cget("text"):
            button.config(bg='red')
        elif " (SH)" in button.cget("text"):
            button.config(bg='blue')
        else:
            button.config(bg='green')
    else:
        button.config(bg='yellow')

def fetch_pokemon_image(name):
    file_name = name.lower().replace(' (sw)', '').replace(' (sh)', '') + ".png"
    image_path = os.path.join(image_dir, file_name)
    if os.path.exists(image_path):
        image = Image.open(image_path)
        image.thumbnail((100, 100), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(image)
    return None

def create_buttons(root):
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
    for gen, names in pokemon.items():
        label = Label(scrollable_frame, text=gen, font=("Helvetica", 16))
        label.grid(row=row, column=0, columnspan=4, pady=10)
        row += 1
        col = 0
        for name in names:
            image = fetch_pokemon_image(name)
            if image:
                button = Button(scrollable_frame, text=name, image=image, compound="top")
                if " (SW)" in name:
                    button.config(bg='red')
                elif " (SH)" in name:
                    button.config(bg='blue')
                else:
                    button.config(bg='green')
                button.config(command=lambda b=button: toggle_highlight(b))
                button.image = image  # Keep a reference to avoid garbage collection
                button.grid(row=row, column=col, padx=5, pady=5)
                col += 1
                if col == 4:
                    col = 0
                    row += 1
            else:
                print(f"Image not found for {name}")
        row += 1

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Bind mouse wheel events to the canvas
    canvas.bind_all("<MouseWheel>", on_mouse_wheel)

def on_mouse_wheel(event):
    global canvas
    canvas.yview_scroll(-1 * int(event.delta / 120), "units")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Pokémon Button Highlighter")
    create_buttons(root)
    root.mainloop()
