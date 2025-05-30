import tkinter as tk
from tkinter import Menu
<<<<<<< HEAD
from Jeu_Principal import main_game
from menu_jouer import open_new_game  # Nous gardons cette fonction pour le menu de jeu
=======
>>>>>>> parent of 86436e0 (wip le menu)

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

    # Exemple d'options pour démarrer une nouvelle partie (sans appel à start_game)
    start_button = tk.Button(
        options_frame,
        text="Commencer",
        font=("Arial", 16),
        fg="#ecf0f1",
        bg="#3498db",
        activeforeground="#ecf0f1",
        activebackground="#2980b9",
    )
    start_button.pack(pady=10)

    # Menu pour changer de skin
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

    # Créer le menu déroulant pour les skins
    skin_menu = Menu(skin_button, tearoff=0)
    skin_button["menu"] = skin_menu

    # Fonction pour changer le type de skin
    def change_skin_type(skin_type):
        skin_button.config(text=skin_type)

    # Ajouter des options au menu déroulant
    skin_menu.add_command(label="Type_1", command=lambda: change_skin_type("Type_1"))
    skin_menu.add_command(label="Type_2", command=lambda: change_skin_type("Type_2"))
    skin_menu.add_command(label="Type_3", command=lambda: change_skin_type("Type_3"))
    skin_menu.add_command(label="Type_4", command=lambda: change_skin_type("Type_4"))

    # Menu pour le mode de jeu
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

    # Créer le menu déroulant pour les modes de jeu
    game_mode_menu = Menu(game_mode_button, tearoff=0)
    game_mode_button["menu"] = game_mode_menu

    # Fonction pour changer le mode de jeu
    def change_game_mode(mode):
        game_mode_button.config(text=mode)

    # Ajouter des options au menu déroulant
    game_mode_menu.add_command(label="Joueur vs Joueur", command=lambda: change_game_mode("Joueur vs Joueur"))
    game_mode_menu.add_command(label="Joueur vs IA", command=lambda: change_game_mode("Joueur vs IA"))
    game_mode_menu.add_command(label="IA vs IA", command=lambda: change_game_mode("IA vs IA"))

    # **Ajout du menu pour la cadence**
    cadence_button = tk.Menubutton(
        options_frame,
        text="Choisir la Cadence",
        font=("Arial", 16),
        fg="#ecf0f1",
        bg="#1abc9c",  # Couleur verte pour la cadence
        activeforeground="#ecf0f1",
        activebackground="#16a085"
    )
    cadence_button.pack(pady=10)

    # Créer le menu déroulant pour les cadences
    cadence_menu = Menu(cadence_button, tearoff=0)
    cadence_button["menu"] = cadence_menu

    # Fonction pour changer la cadence
    def change_cadence(cadence):
        cadence_button.config(text=cadence)

    # Ajouter des options au menu déroulant
    cadence_menu.add_command(label="2/1", command=lambda: change_cadence("2/1"))
    cadence_menu.add_command(label="3/2", command=lambda: change_cadence("3/2"))
    cadence_menu.add_command(label="5/2", command=lambda: change_cadence("5/2"))
    cadence_menu.add_command(label="10/0", command=lambda: change_cadence("10/0"))
    cadence_menu.add_command(label="15/5", command=lambda: change_cadence("15/5"))

    # Bouton pour basculer en plein écran ou quitter le plein écran
    fullscreen_button = tk.Button(
        new_game_window,
        text="Quitter le Plein Écran",
        font=("Arial", 16),
        fg="#ecf0f1",
        bg="#e74c3c",  # Couleur rouge
        activeforeground="#ecf0f1",
        activebackground="#c0392b",  # Rouge foncé au survol
        command=lambda: toggle_fullscreen(new_game_window, fullscreen_button)  # Bascule du plein écran
    )
    fullscreen_button.pack(pady=20)

    # Bouton pour fermer la fenêtre
    exit_button = tk.Button(
        new_game_window,
        text="Fermer",
        font=("Arial", 16),
        fg="#ecf0f1",
        bg="#e74c3c",  # Couleur normale
        activeforeground="#ecf0f1",
        activebackground="#c0392b",  # Rouge foncé au survol
        command=new_game_window.destroy
    )
    exit_button.pack(pady=10)

def toggle_fullscreen(window, button):
    current_state = window.attributes("-fullscreen")
    window.attributes("-fullscreen", not current_state)
    button_text = "Mettre en Plein Écran" if current_state else "Quitter le Plein Écran"
    button.config(text=button_text)
