import tkinter as tk
from tkinter import Menu
from Jeu_Principal import main_game

def open_new_game():
    new_game_window = tk.Toplevel()
    new_game_window.title("Nouvelle Partie")
    new_game_window.attributes("-fullscreen", True)
    new_game_window.configure(bg="#2c3e50")

    title_label = tk.Label(
        new_game_window,
        text="Démarrer une Nouvelle Partie",
        font=("Arial", 24, "bold"),
        fg="#ecf0f1",
        bg="#2c3e50"
    )
    title_label.pack(pady=20)

    options_frame = tk.Frame(new_game_window, bg="#2c3e50")
    options_frame.pack(pady=15, padx=20, fill="both", expand=True)

    def start_game():
        main_game()
        new_game_window.destroy()

    start_button = tk.Button(
        options_frame,
        text="Commencer",
        font=("Arial", 16),
        fg="#ecf0f1",
        bg="#3498db",
        activeforeground="#ecf0f1",
        activebackground="#2980b9",
        command=start_game
    )
    start_button.pack(pady=10)

    skin_button = tk.Menubutton(
        options_frame,
        text="Changer de Skin",
        font=("Arial", 16),
        fg="#ecf0f1",
        bg="#f39c12",
        activeforeground="#ecf0f1",
        activebackground="#e67e22"
    )
    skin_button.pack(pady=10)

    skin_menu = Menu(skin_button, tearoff=0)
    skin_button["menu"] = skin_menu

    def change_skin_type(skin_type):
        skin_button.config(text=skin_type)

    for skin in ["Type_1", "Type_2", "Type_3", "Type_4"]:
        skin_menu.add_command(label=skin, command=lambda s=skin: change_skin_type(s))

    game_mode_button = tk.Menubutton(
        options_frame,
        text="Mode De Jeu",
        font=("Arial", 16),
        fg="#ecf0f1",
        bg="#8e44ad",
        activeforeground="#ecf0f1",
        activebackground="#732d91"
    )
    game_mode_button.pack(pady=10)

    game_mode_menu = Menu(game_mode_button, tearoff=0)
    game_mode_button["menu"] = game_mode_menu

    def change_game_mode(mode):
        game_mode_button.config(text=mode)

    for mode in ["Joueur vs Joueur", "Joueur vs IA", "IA vs IA"]:
        game_mode_menu.add_command(label=mode, command=lambda m=mode: change_game_mode(m))

    cadence_button = tk.Menubutton(
        options_frame,
        text="Choisir la Cadence",
        font=("Arial", 16),
        fg="#ecf0f1",
        bg="#1abc9c",
        activeforeground="#ecf0f1",
        activebackground="#16a085"
    )
    cadence_button.pack(pady=10)

    cadence_menu = Menu(cadence_button, tearoff=0)
    cadence_button["menu"] = cadence_menu

    def change_cadence(cadence):
        cadence_button.config(text=cadence)

    for cadence in ["2/1", "3/2", "5/2", "10/0", "15/5"]:
        cadence_menu.add_command(label=cadence, command=lambda c=cadence: change_cadence(c))

    fullscreen_button = tk.Button(
        new_game_window,
        text="Quitter le Plein Écran",
        font=("Arial", 16),
        fg="#ecf0f1",
        bg="#e74c3c",
        activeforeground="#ecf0f1",
        activebackground="#c0392b",
        command=lambda: toggle_fullscreen(new_game_window, fullscreen_button)
    )
    fullscreen_button.pack(pady=20)

    exit_button = tk.Button(
        new_game_window,
        text="Fermer",
        font=("Arial", 16),
        fg="#ecf0f1",
        bg="#e74c3c",
        activeforeground="#ecf0f1",
        activebackground="#c0392b",
        command=new_game_window.destroy
    )
    exit_button.pack(pady=10)

def toggle_fullscreen(window, button):
    current_state = window.attributes("-fullscreen")
    window.attributes("-fullscreen", not current_state)
    button.config(text="Mettre en Plein Écran" if current_state else "Quitter le Plein Écran")
