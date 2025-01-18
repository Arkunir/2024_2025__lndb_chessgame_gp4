import tkinter as tk

def open_options():
    # Créer une nouvelle fenêtre pour les options
    options_window = tk.Toplevel()
    options_window.title("Options du Jeu")
    options_window.geometry("950x600")  # Taille de la fenêtre
    options_window.configure(bg="#2c3e50")  # Couleur de fond

    # Titre des options
    title_label = tk.Label(
        options_window,
        text="Options du Jeu",
        font=("Arial", 24, "bold"),
        fg="#ecf0f1",
        bg="#2c3e50"
    )
    title_label.pack(pady=20)

    # Conteneur pour le texte des options
    options_frame = tk.Frame(options_window, bg="#2c3e50")
    options_frame.pack(pady=15, padx=20, fill="both", expand=True)

    # Texte des options
    options_text = """
    Options de Configuration du Jeu

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

    # Affichage du texte des options
    options_label = tk.Label(
        options_frame,
        text=options_text,
        font=("Arial", 14),
        fg="#ecf0f1",
        bg="#2c3e50",
        justify="left"
    )
    options_label.pack(pady=10, padx=10, fill="both", expand=True)

    # Bouton pour fermer la fenêtre
    close_button = tk.Button(
        options_window,
        text="Fermer",
        font=("Arial", 16),
        fg="#ecf0f1",
        bg="#e74c3c",
        activeforeground="#ecf0f1",
        activebackground="#c0392b",
        command=options_window.destroy
    )
    close_button.pack(pady=20)
