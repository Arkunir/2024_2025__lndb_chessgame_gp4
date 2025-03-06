import tkinter as tk
from tkinter import messagebox
from menu_regles import open_rules
from menu_options import open_options
import pygame  # Importation de pygame pour l'audio

# Initialiser pygame pour l'audio
pygame.mixer.init()

def play_background_music():
    """Lance la musique de fond en boucle."""
    pygame.mixer.music.load("Premium_chess/assets/Audio/main_music.mp3")  # Chemin du fichier MP3
    pygame.mixer.music.play(-1)  # -1 signifie lecture en boucle infinie

def quit_game():
    """Quitte le jeu après confirmation."""
    if messagebox.askyesno("Quitter", "Êtes-vous sûr de vouloir quitter le jeu ?"):
        pygame.mixer.music.stop()  # Arrêter la musique avant de quitter
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

def open_new_game():
    """Importe et ouvre dynamiquement le module Jeu_Principal et cache la fenêtre principale."""
    from Jeu_Principal import open_new_game
    root.withdraw()  # Cacher la fenêtre principale
    open_new_game()

# Création de la fenêtre principale
root = tk.Tk()
root.title("Jeu d'Échecs - Menu Principal")
root.configure(bg="#2c3e50")

# Mettre la fenêtre en plein écran par défaut
root.attributes('-fullscreen', True)

# Lancer la musique de fond
play_background_music()

# Titre du jeu
title_label = tk.Label(
    root,
    text="Premium Chess",
    font=("Arial", 48, "bold"),
    fg="#ecf0f1",
    bg="#2c3e50"
)
title_label.pack(pady=50)

# Conteneur pour les boutons
button_frame = tk.Frame(root, bg="#2c3e50")
button_frame.pack(pady=20)

# Boutons du menu
buttons = [
    ("Nouvelle Partie", open_new_game),
]

for text, command in buttons:
    button = tk.Button(
        button_frame,
        text=text,
        font=("Arial", 24),
        fg="#ecf0f1",
        bg="#3498db",
        activeforeground="#ecf0f1",
        activebackground="#2980b9",
        width=25,
        command=command
    )
    button.pack(pady=15)

# Bouton pour afficher les règles
rules_button = tk.Button(
    button_frame,
    text="Règles du Jeu",
    font=("Arial", 24),
    fg="#ecf0f1",
    bg="#3498db",
    activeforeground="#ecf0f1",
    activebackground="#2980b9",
    width=25,
    command=open_rules
)
rules_button.pack(pady=15)

# Bouton pour les options
options_button = tk.Button(
    button_frame,
    text="Options",
    font=("Arial", 24),
    fg="#ecf0f1",
    bg="#3498db",
    activeforeground="#ecf0f1",
    activebackground="#2980b9",
    width=25,
    command=open_options
)
options_button.pack(pady=15)

# Bouton pour mettre en plein écran ou quitter le plein écran
fullscreen_button = tk.Button(
    button_frame,
    text="Quitter le mode plein écran",
    font=("Arial", 24),
    fg="#ecf0f1",
    bg="#3498db",
    activeforeground="#ecf0f1",
    activebackground="#2980b9",
    width=25,
    command=toggle_fullscreen
)
fullscreen_button.pack(pady=15)

# Bouton "Quitter"
quit_button = tk.Button(
    root,
    text="Quitter",
    font=("Arial", 24),
    fg="#ecf0f1",
    bg="#e74c3c",
    activeforeground="#ecf0f1",
    activebackground="#c0392b",
    width=25,
    command=quit_game
)
quit_button.pack(pady=20)

# Lancer la boucle principale de Tkinter
root.mainloop()
