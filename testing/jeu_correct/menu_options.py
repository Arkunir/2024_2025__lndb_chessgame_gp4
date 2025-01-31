import tkinter as tk

def open_rules():
    # Créer une nouvelle fenêtre pour les règles
    rules_window = tk.Toplevel()
    rules_window.title("Règles du Jeu d'Échecs")
    rules_window.attributes("-fullscreen", True)  # Mode plein écran
    rules_window.configure(bg="#2c3e50")  # Couleur de fond

    # Titre des règles
    title_label = tk.Label(
        rules_window,
        text="Règles du Jeu d'Échecs",
        font=("Arial", 24, "bold"),
        fg="#ecf0f1",
        bg="#2c3e50"
    )
    title_label.pack(pady=20)

    # Conteneur pour le texte des règles
    rules_frame = tk.Frame(rules_window, bg="#2c3e50")
    rules_frame.pack(pady=15, padx=20, fill="both", expand=True)

    # Texte des règles
    rules_text = """
    Règles de Base du Jeu d'Échecs

    1. Objectif : Le but du jeu est de mettre le roi adverse en échec et mat.
    2. Déplacement des Pièces :
       - Pion : Avance d'une case, capture en diagonale.
       - Tour : Se déplace horizontalement et verticalement.
       - Cavalier : Se déplace en "L".
       - Fou : Se déplace en diagonale.
       - Reine : Combine les mouvements de la tour et du fou.
       - Roi : Se déplace d'une case dans toutes les directions.
    3. Échec et Mat : Le roi est en échec et mat s'il ne peut pas échapper à une attaque.
    4. Pat : Si le roi n'est pas en échec mais qu'aucun mouvement légal n'est possible, c'est un match nul.
    5. Roque : Mouvement spécial impliquant le roi et la tour.
    6. Promotion : Un pion qui atteint la dernière rangée peut être promu en une autre pièce (sauf roi).
    """

    # Affichage du texte des règles
    rules_label = tk.Label(
        rules_frame,
        text=rules_text,
        font=("Arial", 14),
        fg="#ecf0f1",
        bg="#2c3e50",
        justify="left"
    )
    rules_label.pack(pady=10, padx=10, fill="both", expand=True)

    # Bouton pour mettre en plein écran ou quitter le plein écran
    fullscreen_button = tk.Button(
        rules_window,
        text="Quitter le Plein Écran",
        font=("Arial", 16),
        fg="#ecf0f1",
        bg="#e74c3c",
        activeforeground="#ecf0f1",
        activebackground="#c0392b",
        command=lambda: toggle_fullscreen(rules_window, fullscreen_button)  # Toggle fullscreen
    )
    fullscreen_button.pack(pady=20)

    # Bouton pour fermer la fenêtre
    exit_button = tk.Button(
        rules_window,
        text="Fermer",
        font=("Arial", 16),
        fg="#ecf0f1",
        bg="#e74c3c",
        activeforeground="#ecf0f1",
        activebackground="#c0392b",
        command=rules_window.destroy
    )
    exit_button.pack(pady=10)

def toggle_fullscreen(window, button):
    current_state = window.attributes("-fullscreen")
    window.attributes("-fullscreen", not current_state)
    button_text = "Mettre en Plein Écran" if current_state else "Quitter le Plein Écran"
    button.config(text=button_text)

def open_options():
    # Créer une nouvelle fenêtre pour les options
    options_window = tk.Toplevel()
    options_window.title("Options du Jeu d'Échecs")
    options_window.attributes("-fullscreen", True)  # Mode plein écran
    options_window.configure(bg="#2c3e50")  # Couleur de fond

    # Titre des options
    title_label = tk.Label(
        options_window,
        text="Options du Jeu d'Échecs",
        font=("Arial", 24, "bold"),
        fg="#ecf0f1",
        bg="#2c3e50"
    )
    title_label.pack(pady=20)

    # Conteneur pour les boutons des options
    options_frame = tk.Frame(options_window, bg="#2c3e50")
    options_frame.pack(pady=15, padx=20, fill="both", expand=True)

    # Liste des options
    options = [
        "Choisir le niveau de difficulté",
        "Activer/désactiver les conseils",
        "Personnaliser les couleurs des pièces",
        "Enregistrer les paramètres"
    ]

    # Création des boutons pour chaque option dans une grille 2x2
    for index, option in enumerate(options):
        option_button = tk.Button(
            options_frame,
            text=option,
            font=("Arial", 16),
            fg="#ecf0f1",
            bg="#3498db",
            activeforeground="#ecf0f1",
            activebackground="#2980b9",
            command=lambda opt=option: print(f"Option sélectionnée: {opt}")  # Placeholder action
        )
        row = index // 2  # Determine the row index
        column = index % 2  # Determine the column index
        option_button.grid(row=row, column=column, padx=10, pady=10, sticky="nsew")  # Center the buttons

    # Bouton pour mettre en plein écran ou quitter le plein écran
    fullscreen_button = tk.Button(
        options_window,
        text="Quitter le Plein Écran",
        font=("Arial", 16),
        fg="#ecf0f1",
        bg="#e74c3c",
        activeforeground="#ecf0f1",
        activebackground="#c0392b",
        command=lambda: toggle_fullscreen(options_window, fullscreen_button)  # Toggle fullscreen
    )
    fullscreen_button.pack(pady=20)

    # Bouton pour fermer la fenêtre
    exit_button = tk.Button(
        options_window,
        text="Fermer",
        font=("Arial", 16),
        fg="#ecf0f1",
        bg="#e74c3c",
        activeforeground="#ecf0f1",
        activebackground="#c0392b",
        command=options_window.destroy
    )
    exit_button.pack(pady=10)

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

    # Bouton pour quitter la fenêtre
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
