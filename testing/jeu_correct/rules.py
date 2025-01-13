import tkinter as tk
from tkinter import messagebox

# Fonction pour afficher les règles dans une nouvelle fenêtre
def open_rules():
    # Créer une nouvelle fenêtre pour les règles
    rules_window = tk.Toplevel()
    rules_window.title("Règles du Jeu d'Échecs")
    rules_window.geometry("800x600")  # Taille de la fenêtre
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
    rules_frame.pack(pady=10, padx=20, fill="both", expand=True)

    # Texte des règles
    rules_text = """
    **Règles de Base du Jeu d'Échecs**

    1. **Objectif** : Le but du jeu est de mettre le roi adverse en échec et mat.
    2. **Déplacement des Pièces** :
       - Pion : Avance d'une case, capture en diagonale.
       - Tour : Se déplace horizontalement et verticalement.
       - Cavalier : Se déplace en "L".
       - Fou : Se déplace en diagonale.
       - Reine : Combine les mouvements de la tour et du fou.
       - Roi : Se déplace d'une case dans toutes les directions.
    3. **Échec et Mat** : Le roi est en échec et mat s'il ne peut pas échapper à une attaque.
    4. **Pat** : Si le roi n'est pas en échec mais qu'aucun mouvement légal n'est possible, c'est un match nul.
    5. **Roque** : Mouvement spécial impliquant le roi et la tour.
    6. **Promotion** : Un pion qui atteint la dernière rangée peut être promu en une autre pièce (sauf roi).
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

    # Bouton pour fermer la fenêtre
    close_button = tk.Button(
        rules_window,
        text="Fermer",
        font=("Arial", 16),
        fg="#ecf0f1",
        bg="#e74c3c",
        activeforeground="#ecf0f1",
        activebackground="#c0392b",
        command=rules_window.destroy
    )
    close_button.pack(pady=20)

# Fonctions pour les actions des boutons
def start_game():
    messagebox.showinfo("Nouvelle Partie", "Démarrage d'une nouvelle partie...")
    # Ajouter ici la logique pour démarrer une nouvelle partie

def open_options():
    messagebox.showinfo("Options", "Ouverture des options...")
    # Ajouter ici la logique pour ouvrir les options

def quit_game():
    if messagebox.askyesno("Quitter", "Êtes-vous sûr de vouloir quitter le jeu ?"):
        root.destroy()

def toggle_fullscreen():
    """Bascule entre le mode plein écran et le mode fenêtré."""
    is_fullscreen = root.attributes('-fullscreen')
    root.attributes('-fullscreen', not is_fullscreen)
    update_fullscreen_button_text()

def update_fullscreen_button_text():
    """Met à jour le texte du bouton en fonction de l'état de la fenêtre."""
    is_fullscreen = root.attributes('-fullscreen')
    if is_fullscreen:
        fullscreen_button.config(text="Quitter le mode plein écran")
    else:
        fullscreen_button.config(text="Mettre en plein écran")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Jeu d'Échecs - Menu Principal")
root.configure(bg="#2 c3e50")  # Couleur de fond

# Création des boutons du menu principal
start_button = tk.Button(
    root,
    text="Démarrer une Partie",
    font=("Arial", 16),
    fg="#ecf0f1",
    bg="#3498db",
    activeforeground="#ecf0f1",
    activebackground="#2980b9",
    command=start_game
)
start_button.pack(pady=10)

options_button = tk.Button(
    root,
    text="Options",
    font=("Arial", 16),
    fg="#ecf0f1",
    bg="#3498db",
    activeforeground="#ecf0f1",
    activebackground="#2980b9",
    command=open_options
)
options_button.pack(pady=10)

rules_button = tk.Button(
    root,
    text="Règles du Jeu",
    font=("Arial", 16),
    fg="#ecf0f1",
    bg="#3498db",
    activeforeground="#ecf0f1",
    activebackground="#2980b9",
    command=open_rules
)
rules_button.pack(pady=10)

fullscreen_button = tk.Button(
    root,
    text="Mettre en plein écran",
    font=("Arial", 16),
    fg="#ecf0f1",
    bg="#3498db",
    activeforeground="#ecf0f1",
    activebackground="#2980b9",
    command=toggle_fullscreen
)
fullscreen_button.pack(pady=10)

quit_button = tk.Button(
    root,
    text="Quitter",
    font=("Arial", 16),
    fg="#ecf0f1",
    bg="#e74c3c",
    activeforeground="#ecf0f1",
    activebackground="#c0392b",
    command=quit_game
)
quit_button.pack(pady=10)

# Lancement de la boucle principale
root.mainloop()