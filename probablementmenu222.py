import pygame
import chess
import random
import tkinter as tk
from tkinter import messagebox
import time

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

def load_pieces():
    pieces = {}
    for piece, filename in PIECE_FILES.items():
        image = pygame.image.load(ASSETS_PATH + filename)
        image = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))
        pieces[piece] = image
    return pieces

PIECES = load_pieces()
board = chess.Board()

# Définition des fonctions de dessin du jeu
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

def get_square_under_mouse(pos):
    x, y = pos
    col = x // SQUARE_SIZE
    row = 7 - (y // SQUARE_SIZE)
    return chess.square(col, row)

def promote_pawn(square):
    menu_width, menu_height = 200, 150
    menu_x = WIDTH // 2 - menu_width // 2
    menu_y = HEIGHT // 2 - menu_height // 2
    font = pygame.font.Font(None, 36)
    options = ['Dame', 'Tour', 'Cavalier', 'Fou']
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if menu_x <= mouse_x <= menu_x + menu_width:
                    for i, option in enumerate(options):
                        option_y = menu_y + i * (menu_height // 4)
                        if option_y <= mouse_y <= option_y + menu_height // 4:
                            return PROMOTION_OPTIONS[i]

        pygame.draw.rect(screen, (50, 50, 50), (menu_x, menu_y, menu_width, menu_height))
        for i, option in enumerate(options):
            text = font.render(option, True, (255, 255, 255))
            screen.blit(text, (menu_x + 10, menu_y + i * (menu_height // 4) + 10))
        pygame.display.flip()

def check_game_over():
    global game_over
    if board.is_checkmate():
        winner = "Blancs" if board.turn == chess.BLACK else "Noirs"
        display_winner(winner)
        game_over = True
    elif board.is_stalemate() or board.is_insufficient_material() or board.is_seventyfive_moves() or board.is_variant_draw():
        display_draw("Égalité")
        game_over = True
    elif board.is_check():  # Si il y a échec, on affiche ça en attendant qu'un coup soit joué.
        pass

def display_winner(winner):
    font = pygame.font.Font(None, 72)
    text = font.render(f"Victoire! {winner} ont gagné!", True, (255, 255, 255))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    
    # Create "Rejouer" button
    button_width, button_height = 200, 60
    button_x = WIDTH // 2 - button_width // 2
    button_y = HEIGHT // 2 + 100
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    
    # Create "Quitter" button
    quit_button_y = HEIGHT // 2 + 200
    quit_button_rect = pygame.Rect(button_x, quit_button_y, button_width, button_height)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    return "replay"
                elif quit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    exit()

        screen.fill((0, 0, 0))  # Background black
        screen.blit(text, text_rect)

        # Draw the "Rejouer" button (white with black text)
        pygame.draw.rect(screen, (255, 255, 255), button_rect)  # White button
        button_text = pygame.font.Font(None, 36).render("Rejouer", True, (0, 0, 0))  # Black text
        screen.blit(button_text, (button_x + (button_width - button_text.get_width()) // 2, button_y + (button_height - button_text.get_height()) // 2))

        # Draw the "Quitter" button (red with white text)
        pygame.draw.rect(screen, (255, 0, 0), quit_button_rect)  # Red button
        quit_button_text = pygame.font.Font(None, 36).render("Quitter", True, (255, 255, 255))  # White text
        screen.blit(quit_button_text, (button_x + (button_width - quit_button_text.get_width()) // 2, quit_button_y + (button_height - quit_button_text.get_height()) // 2))

        pygame.display.flip()

def display_draw(message):
    font = pygame.font.Font(None, 72)
    text = font.render(message, True, (255, 255, 255))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    # Create "Rejouer" button
    button_width, button_height = 200, 60
    button_x = WIDTH // 2 - button_width // 2
    button_y = HEIGHT // 2 + 100
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    
    # Create "Quitter" button
    quit_button_y = HEIGHT // 2 + 200
    quit_button_rect = pygame.Rect(button_x, quit_button_y, button_width, button_height)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    reset_game()  # Réinitialiser la partie avant de recommencer
                    return  # Revenir au menu
                elif quit_button_rect.collidepoint(event.pos):
                    pygame.quit()
                    exit()

        screen.fill((0, 0, 0))  # Background black
        screen.blit(text, text_rect)

        # Draw the "Rejouer" button (white with black text)
        pygame.draw.rect(screen, (255, 255, 255), button_rect)  # White button
        button_text = pygame.font.Font(None, 36).render("Rejouer", True, (0, 0, 0))  # Black text
        screen.blit(button_text, (button_x + (button_width - button_text.get_width()) // 2, button_y + (button_height - button_text.get_height()) // 2))

        # Draw the "Quitter" button (red with white text)
        pygame.draw.rect(screen, (255, 0, 0), quit_button_rect)  # Red button
        quit_button_text = pygame.font.Font(None, 36).render("Quitter", True, (255, 255, 255))  # White text
        screen.blit(quit_button_text, (button_x + (button_width - quit_button_text.get_width()) // 2, quit_button_y + (button_height - quit_button_text.get_height()) // 2))

        pygame.display.flip()

def reset_game():
    global board, game_over
    board = chess.Board()  # Reset the board to the initial state
    game_over = False  # Set game_over flag to False

def random_move(level=1):
    # Adjust the randomness of the move selection based on the AI level
    legal_moves = list(board.legal_moves)
    
    if level == 1:  # Niveau très facile (AI facile)
        return random.choice(legal_moves)
    
    elif level == 2:  # Facile
        return random.choice(legal_moves)  # Plus de logique pourrait être ajoutée ici pour rendre l'IA un peu plus intelligente
    
    elif level == 3:  # Moyen
        # Un peu plus intelligent, il pourrait jouer les meilleures pièces
        return random.choice(legal_moves)
    
    elif level == 4:  # Difficile
        # IA avec une évaluation plus avancée
        return random.choice(legal_moves)
    
    elif level == 5:  # Très difficile
        # IA très avancée (par exemple, utiliser un algorithme de recherche de profondeur)
        return random.choice(legal_moves)  # Placez une vraie logique d'IA ici

    return random.choice(legal_moves)

def ai_move():
    move = random_move(ai_white_level if board.turn == chess.WHITE else ai_black_level)
    board.push(move)

def play_with_ai():
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        draw_board()
        draw_pieces()
        check_game_over()

        if not game_over and board.turn == chess.WHITE:
            ai_move()

        pygame.display.flip()

def play_with_two_players():
    global selected_square
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                pos = pygame.mouse.get_pos()
                square = get_square_under_mouse(pos)

                # Sélectionner une case
                if selected_square is None:
                    if board.piece_at(square) is not None and ((board.turn == chess.WHITE and board.piece_at(square).color == chess.WHITE) or (board.turn == chess.BLACK and board.piece_at(square).color == chess.BLACK)):
                        selected_square = square
                else:
                    move = chess.Move(selected_square, square)
                    if move in board.legal_moves:
                        board.push(move)
                    selected_square = None

        draw_board()
        draw_pieces()
        check_game_over()

        pygame.display.flip()

def play_with_two_ais():
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        draw_board()
        draw_pieces()
        check_game_over()

        if not game_over:
            ai_move()

        pygame.display.flip()

def level_selection_window(mode):
    window = tk.Tk()
    window.title("Sélectionner le niveau de l'IA")
    window.geometry("300x300")  # Taille de la fenêtre de niveau améliorée

    # Interface simple avec des boutons plus petits
    tk.Label(window, text="Sélectionner le niveau", font=("Arial", 18)).pack(pady=20)
    tk.Button(window, text="Très Facile", font=("Arial", 12), width=15, height=1, command=lambda: on_level_select(window, mode, 1)).pack(pady=5)
    tk.Button(window, text="Facile", font=("Arial", 12), width=15, height=1, command=lambda: on_level_select(window, mode, 2)).pack(pady=5)
    tk.Button(window, text="Moyenne", font=("Arial", 12), width=15, height=1, command=lambda: on_level_select(window, mode, 3)).pack(pady=5)
    tk.Button(window, text="Difficile", font=("Arial", 12), width=15, height=1, command=lambda: on_level_select(window, mode, 4)).pack(pady=5)
    tk.Button(window, text="Très Difficile", font=("Arial", 12), width=15, height=1, command=lambda: on_level_select(window, mode, 5)).pack(pady=5)

    window.mainloop()

def on_level_select(window, mode, level):
    window.destroy()
    if mode == "AI":
        start_game("AI", white_level=level, black_level=level)
    elif mode == "2 Players":
        start_game("2 Players")

def menu_window():
    window = tk.Tk()
    window.title("Menu Principal")
    window.geometry("400x400")  # Taille réduite

    tk.Label(window, text="Jeu d'échecs", font=("Arial", 18), bg="#f0f0f0").pack(pady=20)
    tk.Button(window, text="Jouer contre IA", font=("Arial", 16), width=20, height=2, command=lambda: level_selection_window("AI")).pack(pady=10)
    tk.Button(window, text="2 Joueurs", font=("Arial", 16), width=20, height=2, command=lambda: start_game("2 Players")).pack(pady=10)
    tk.Button(window, text="2 IA", font=("Arial", 16), width=20, height=2, command=lambda: start_game("2 AI")).pack(pady=10)

    window.mainloop()

# Lancer le menu du jeu
menu_window()
