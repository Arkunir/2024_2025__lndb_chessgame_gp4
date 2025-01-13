import tkinter as tk
from tkinter import messagebox

# Fonctions pour les actions des boutons
def start_game():
    messagebox.showinfo("Nouvelle Partie", "Démarrage d'une nouvelle partie...")
    # Ajouter ici la logique pour démarrer une nouvelle partie

def open_options():
    messagebox.showinfo("Options", "Ouverture des options...")
    # Ajouter ici la logique pour ouvrir les options

def open_rules():
    messagebox.showinfo("Règles", "Ouverture des règles du jeu...")
    # Ajouter ici la logique pour afficher les règles

def quit_game():
    if messagebox.askyesno("Quitter", "Êtes-vous sûr de vouloir quitter le jeu ?"):
        root.destroy()

# Création de la fenêtre principale
root = tk.Tk()
root.title("Jeu d'Échecs - Menu Principal")
root.configure(bg="#2c3e50")  # Couleur de fond

# Mettre la fenêtre en plein écran
root.attributes('-fullscreen', True)

# Titre du jeu
title_label = tk.Label(
    root,
    text="Jeu d'Échecs",
    font=("Arial", 48, "bold"),  # Taille de police augmentée
    fg="#ecf0f1",
    bg="#2c3e50"
)
title_label.pack(pady=50)  # Espacement augmenté

# Conteneur pour les boutons
button_frame = tk.Frame(root, bg="#2c3e50")
button_frame.pack(pady=20)

# Boutons du menu
buttons = [
    ("Nouvelle Partie", start_game),
    ("Options", open_options),
    ("Règles", open_rules),
    ("Quitter le mode plein écran", lambda: root.attributes('-fullscreen', False))
]

for text, command in buttons:
    button = tk.Button(
        button_frame,
        text=text,
        font=("Arial", 24),  # Taille de police augmentée
        fg="#ecf0f1",
        bg="#3498db",  # Couleur bleue pour tous les boutons sauf "Quitter"
        activeforeground="#ecf0f1",
        activebackground="#2980b9",  # Couleur bleue foncée au survol
        width=25,  # Largeur des boutons augmentée
        command=command
    )
    button.pack(pady=15)  # Espacement entre les boutons augmenté

# Bouton "Quitter" en rouge
quit_button = tk.Button(
    root,
    text="Quitter",
    font=("Arial", 24),  # Taille de police augmentée
    fg="#ecf0f1",
    bg="#e74c3c",  # Couleur rouge pour "Quitter"
    activeforeground="#ecf0f1",
    activebackground="#c0392b",  # Couleur rouge foncée au survol
    width=25,  # Largeur des boutons augmentée
    command=quit_game
)
quit_button.pack(pady=20)

# Lancer la boucle principale de Tkinter
root.mainloop()