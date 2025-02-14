import tkinter as tk
from tkinter import Menu
from Jeu_Principal import start_game  # Import the start_game function

def open_new_game(selected_skin, selected_mode):
    # Directly call the start_game function with the selected mode
    start_game(selected_mode)

    # Create a new window for starting a new game
    new_game_window = tk.Toplevel()
    new_game_window.title("Nouvelle Partie")
    new_game_window.attributes("-fullscreen", True)  # Fullscreen mode
    new_game_window.configure(bg="#2c3e50")  # Background color

    # Title of the new game
    title_label = tk.Label(
        new_game_window,
        text="Démarrer une Nouvelle Partie",
        font=("Arial", 24, "bold"),
        fg="#ecf0f1",
        bg="#2c3e50"
    )
    title_label.pack(pady=20)

    # Container for new game options
    options_frame = tk.Frame(new_game_window, bg="#2c3e50")
    options_frame.pack(pady=15, padx=20, fill="both", expand=True)

    # Example options for starting a new game
    start_button = tk.Button(
        options_frame,
        text="Commencer",
        font=("Arial", 16),
        fg="#ecf0f1",
        bg="#3498db",
        activeforeground="#ecf0f1",
        activebackground="#2980b9",
        command=lambda: print("Nouvelle partie commencée!")  # Placeholder action
    )
    start_button.pack(pady=10)

    # Menu for changing skin
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

    # Create the dropdown menu for skins
    skin_menu = Menu(skin_button, tearoff=0)
    skin_button["menu"] = skin_menu

    # Function to change the button text based on selection
    def change_skin_type(skin_type):
        skin_button.config(text=skin_type)

    # Add options to the dropdown menu
    skin_menu.add_command(label="Type_1", command=lambda: change_skin_type("Type_1"))
    skin_menu.add_command(label="Type_2", command=lambda: change_skin_type("Type_2"))

    # Menu for game mode
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

    # Create the dropdown menu for game modes
    game_mode_menu = Menu(game_mode_button, tearoff=0)
    game_mode_button["menu"] = game_mode_menu

    # Function to change the button text based on selection
    def change_game_mode(mode):
        game_mode_button.config(text=mode)

    # Add options to the dropdown menu
    game_mode_menu.add_command(label="Joueur vs Joueur", command=lambda: change_game_mode("Joueur vs Joueur"))
    game_mode_menu.add_command(label="Joueur vs IA", command=lambda: change_game_mode("Joueur vs IA"))
    game_mode_menu.add_command(label="IA vs IA", command=lambda: change_game_mode("IA vs IA"))

    # Button to toggle fullscreen or exit fullscreen
    fullscreen_button = tk.Button(
        new_game_window,
        text="Quitter le Plein Écran",
        font=("Arial", 16),
        fg="#ecf0f1",
        bg="#e74c3c",  # Red color
        activeforeground="#ecf0f1",
        activebackground="#c0392b",  # Dark red on hover
        command=lambda: toggle_fullscreen(new_game_window, fullscreen_button)  # Toggle fullscreen
    )
    fullscreen_button.pack(pady=20)

    # Button to close the window
    exit_button = tk.Button(
        new_game_window,
        text="Fermer",
        font=("Arial", 16),
        fg="#ecf0f1",
        bg="#e74c3c",  # Normal color
        activeforeground="#ecf0f1",
        activebackground="#c0392b",  # Dark red on hover
        command=new_game_window.destroy
    )
    exit_button.pack(pady=10)

def toggle_fullscreen(window, button):
    current_state = window.attributes("-fullscreen")
    window.attributes("-fullscreen", not current_state)
    button_text = "Mettre en Plein Écran" if current_state else "Quitter le Plein Écran"
    button.config(text=button_text)
