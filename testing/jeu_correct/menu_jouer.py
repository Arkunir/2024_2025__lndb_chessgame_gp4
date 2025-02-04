import tkinter as tk
from tkinter import Menu

def open_new_game():
    # Créer une nouvelle fenêtre pour démarrer une nouvelle partie
    new_game_window = tk.Toplevel()
    new_game_window.title("Nouvelle Partie")
    new_game_window.attributes("-fullscreen", True)  # Mode plein écran
    new_game_window.configure(bg="#2c3e50")  # Couleur de fond

    # Titre de la nouvelle partie
    title_label = tk.Label(
        new_game_window,
        text="Démarrer une Nouvelle Partie",
        font=("Arial", 24, "bold"),
        fg="#ecf0f1",
        bg="#2c3e50"
    )
    title_label.pack(pady=20)

    # Conteneur pour les options de la nouvelle partie
    options_frame = tk.Frame(new_game_window, bg="#2c3e50")
    options_frame.pack(pady=15, padx=20, fill="both", expand=True)

    # Exemple d'options pour démarrer une nouvelle partie
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

    # Menu déroulant pour le changement de skin
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

    # Création du menu déroulant pour les skins
    skin_menu = Menu(skin_button, tearoff=0)
    skin_button["menu"] = skin_menu

    # Fonction pour changer le texte du bouton en fonction de la sélection
    def change_skin_type(skin_type):
        skin_button.config(text=skin_type)

    # Ajout des options au menu déroulant
    skin_menu.add_command(label="Type_1", command=lambda: change_skin_type("Type_1"))
    skin_menu.add_command(label="Type_2", command=lambda: change_skin_type("Type_2"))

    # Menu déroulant pour le mode de jeu
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

    # Création du menu déroulant pour le mode de jeu
    game_mode_menu = Menu(game_mode_button, tearoff=0)
    game_mode_button["menu"] = game_mode_menu

    # Fonction pour changer le texte du bouton en fonction de la sélection
    def change_game_mode(mode):
        game_mode_button.config(text=mode)

    # Ajout des options au menu déroulant
    game_mode_menu.add_command(label="Joueur vs Joueur", command=lambda: change_game_mode("Joueur vs Joueur"))
    game_mode_menu.add_command(label="Joueur vs IA", command=lambda: change_game_mode("Joueur vs IA"))
    game_mode_menu.add_command(label="IA vs IA", command=lambda: change_game_mode("IA vs IA"))

    # Bouton pour mettre en plein écran ou quitter le plein écran
    fullscreen_button = tk.Button(
        new_game_window,
        text="Quitter le Plein Écran",
        font=("Arial", 16),
        fg="#ecf0f1",
        bg="#e74c3c",  # Couleur rouge
        activeforeground="#ecf0f1",
        activebackground="#c0392b",
        command=lambda: toggle_fullscreen(new_game_window, fullscreen_button)  # Toggle fullscreen
    )
    fullscreen_button.pack(pady=20)

    # Bouton pour quitter la fenêtre
    exit_button = tk.Button(
        new_game_window,
        text="Fermer",
        font=("Arial", 16),
        fg="#ecf0f1",
        bg="#e74c3c",  # Couleur normale
        activeforeground="#ecf0f1",
        activebackground="#c0392b",
        command=new_game_window.destroy
    )
    exit_button.pack(pady=10)

def toggle_fullscreen(window, button):
    current_state = window.attributes("-fullscreen")
    window.attributes("-fullscreen", not current_state)
    button_text = "Mettre en Plein Écran" if current_state else "Quitter le Plein Écran"
    button.config(text=button_text)
