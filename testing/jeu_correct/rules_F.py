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

    # Bouton pour quitter le mode plein écran
    close_button = tk.Button(
        rules_window,
        text="Quitter le Plein Écran",
        font=("Arial", 16),
        fg="#ecf0f1",
        bg="#e74c3c",
        activeforeground="#ecf0f1",
        activebackground="#c0392b",
        command=lambda: rules_window.attributes("-fullscreen", False)  # Désactive le plein écran
    )
    close_button.pack(pady=20)

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

# Exemple de fenêtre principale
root = tk.Tk()
root.title("Jeu d'Échecs")
root.geometry("400x200")

rules_button = tk.Button(
    root,
    text="Ouvrir les Règles",
    font=("Arial", 16),
    command=open_rules
)
rules_button.pack(pady=50)

root.mainloop()
