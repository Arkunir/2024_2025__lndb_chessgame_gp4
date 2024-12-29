import pygame
import chess
import tkinter as tk
from tkinter import messagebox

# Initialisation de pygame
pygame.init()

# Paramètres de la fenêtre
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

LIGHT_BROWN = (240, 217, 181)
DARK_BROWN = (181, 136, 99)

ASSETS_PATH = "game_chess/assets/"
PIECE_FILES = {
    'P': "wP.png", 'N': "wN.png", 'B': "wB.png", 'R': "wR.png", 'Q': "wQ.png", 'K': "wK.png",
    'p': "P.png", 'n': "N.png", 'b': "B.png", 'r': "R.png", 'q': "Q.png", 'k': "K.png"
}

PROMOTION_OPTIONS = ['q', 'r', 'n', 'b']

# Créer la fenêtre Pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu d'échecs")

# Initialisation de l'état de la partie
selected_square = None
game_over = False
ai_white_level = 1  # Niveau de l'IA pour les blancs
ai_black_level = 1  # Niveau de l'IA pour les noirs

def load_pieces():
    pieces = {}
    for piece, filename in PIECE_FILES.items():
        image = pygame.image.load(ASSETS_PATH + filename)
        image = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))
        pieces[piece] = image
    return pieces

PIECES = load_pieces()
board = chess.Board()

# Fonctions pour afficher le plateau et les pièces
def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            color = LIGHT_BROWN if (row + col) % 2 == 0 else DARK_BROWN
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

def draw_pieces():
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            col = chess.square_file(square)
            row = chess.square_rank(square)
            image = PIECES[piece.symbol()]
            screen.blit(image, (col * SQUARE_SIZE, (7 - row) * SQUARE_SIZE))

# Sélectionner un niveau de difficulté dans la fenêtre Tkinter
def level_selection_window(mode):
    window = tk.Tk()
    window.title("Sélection du niveau de l'IA")
    window.configure(bg="#282828")

    tk.Label(window, text="Choisissez le niveau de l'IA pour les blancs", font=("Arial", 18), fg="#FFFFFF", bg="#282828").pack(pady=20)

    def on_white_level_select(level):
        global ai_white_level
        ai_white_level = level
        level_selection_for_black(window)

    # Boutons stylisés pour la sélection du niveau
    for level in range(1, 6):
        btn = tk.Button(window, text=f"Niveau {level}", font=("Arial", 16), bg="#4CAF50", fg="white", 
                        activebackground="#45a049", relief="raised", bd=5, command=lambda level=level: on_white_level_select(level))
        btn.pack(pady=10)

    window.mainloop()

# Sélectionner le niveau pour les noirs après la sélection des blancs
def level_selection_for_black(previous_window):
    previous_window.destroy()  # Fermer la fenêtre précédente

    window = tk.Tk()
    window.title("Sélection du niveau de l'IA")
    window.configure(bg="#282828")

    tk.Label(window, text="Choisissez le niveau de l'IA pour les noirs", font=("Arial", 18), fg="#FFFFFF", bg="#282828").pack(pady=20)

    def on_black_level_select(level):
        global ai_black_level
        ai_black_level = level
        start_game("AI", ai_white_level, ai_black_level)

    # Boutons stylisés pour la sélection du niveau
    for level in range(1, 6):
        btn = tk.Button(window, text=f"Niveau {level}", font=("Arial", 16), bg="#4CAF50", fg="white", 
                        activebackground="#45a049", relief="raised", bd=5, command=lambda level=level: on_black_level_select(level))
        btn.pack(pady=10)

    window.mainloop()

# Démarrer le jeu avec le mode et les niveaux sélectionnés
def start_game(mode, white_level=None, black_level=None):
    global ai_white_level, ai_black_level
    if white_level and black_level:
        ai_white_level = white_level  # Niveau de l'IA pour les blancs
        ai_black_level = black_level  # Niveau de l'IA pour les noirs
    global game_over
    game_over = False
    if mode == "AI":
        play_with_ai()
    elif mode == "2 Players":
        play_with_two_players()
    elif mode == "2 AI":
        play_with_two_ais()  # Nouveau mode où 2 IA s'affrontent

def play_with_ai():
    # Code pour gérer les mouvements de l'IA et du joueur
    pass

# Lancer la fenêtre de menu avec des options de jeu
def menu_window():
    window = tk.Tk()
    window.title("Menu du jeu d'échecs")
    window.geometry("400x400")
    window.configure(bg="#282828")

    tk.Label(window, text="Choisissez un mode de jeu", font=("Arial", 24), fg="#FFFFFF", bg="#282828").pack(pady=20)

    def on_mode_select(mode):
        window.destroy()  # Fermer la fenêtre Tkinter
        if mode in ["AI", "2 Players", "2 AI"]:
            level_selection_window(mode)
        else:
            start_game(mode)

    # Boutons stylisés
    tk.Button(window, text="Contre l'IA", font=("Arial", 16), bg="#4CAF50", fg="white", relief="raised", bd=5, 
              activebackground="#45a049", command=lambda: on_mode_select("AI")).pack(pady=10)
    tk.Button(window, text="2 Joueurs", font=("Arial", 16), bg="#2196F3", fg="white", relief="raised", bd=5, 
              activebackground="#1976D2", command=lambda: on_mode_select("2 Players")).pack(pady=10)
    tk.Button(window, text="2 IA", font=("Arial", 16), bg="#FF5722", fg="white", relief="raised", bd=5, 
              activebackground="#E64A19", command=lambda: on_mode_select("2 AI")).pack(pady=10)

    window.mainloop()

# Démarrer la fenêtre du menu
menu_window()
