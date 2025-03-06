import tkinter as tk
import pygame

def open_options():
    # Créer une nouvelle fenêtre pour les options
    options_window = tk.Toplevel()
    options_window.title("Options")
    options_window.attributes("-fullscreen", True)  # Mode plein écran
    options_window.configure(bg="#2c3e50")

    # Titre des options
    title_label = tk.Label(
        options_window,
        text="Options",
        font=("Arial", 24, "bold"),
        fg="#ecf0f1",
        bg="#2c3e50"
    )
    title_label.pack(pady=20)

    # Fonction pour couper le son
    def mute():
        pygame.mixer.music.pause()

    # Fonction pour réactiver le son
    def unmute():
        pygame.mixer.music.unpause()

    # Bouton Mute
    mute_button = tk.Button(
        options_window,
        text="Mute",
        font=("Arial", 16),
        fg="#ecf0f1",
        bg="#3498db",
        activeforeground="#ecf0f1",
        activebackground="#2980b9",
        command=mute
    )
    mute_button.pack(pady=20)

    # Bouton Unmute
    unmute_button = tk.Button(
        options_window,
        text="Unmute",
        font=("Arial", 16),
        fg="#ecf0f1",
        bg="#3498db",
        activeforeground="#ecf0f1",
        activebackground="#2980b9",
        command=unmute
    )
    unmute_button.pack(pady=20)

    # Bouton pour quitter le plein écran
    fullscreen_button = tk.Button(
        options_window,
        text="Quitter le Plein Écran",
        font=("Arial", 16),
        fg="#ecf0f1",
        bg="#e74c3c",
        activeforeground="#ecf0f1",
        activebackground="#c0392b",
        command=lambda: toggle_fullscreen(options_window, fullscreen_button)
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

# Fonction pour basculer en plein écran
def toggle_fullscreen(window, button):
    current_state = window.attributes("-fullscreen")
    window.attributes("-fullscreen", not current_state)
    button_text = "Mettre en Plein Écran" if current_state else "Quitter le Plein Écran"
    button.config(text=button_text)
