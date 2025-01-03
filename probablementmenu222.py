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
    
    if level == 1:
        return random.choice(legal_moves)  # Niveau facile (choix totalement aléatoire)
    
    # Niveau 2-5 (on peut ajouter plus de sophistication dans les niveaux plus élevés)
    return random.choice(legal_moves)

# Fonction IA
def play_with_ai():
    global board, game_over
    game_over = False
    turn = True  # True: White's turn, False: Black's turn

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                square = get_square_under_mouse(event.pos)
                if square != -1:
                    piece = board.piece_at(square)
                    if piece is not None and piece.color == (chess.WHITE if turn else chess.BLACK):
                        selected_square = square
                    elif selected_square != -1:
                        move = chess.Move(selected_square, square)
                        if move in board.legal_moves:
                            board.push(move)
                            selected_square = -1
                            turn = not turn

        # Si c'est le tour de l'IA, effectuer un mouvement avec délai et en fonction du niveau
        if not turn:
            move = random_move(ai_white_level)
            board.push(move)
            pygame.time.delay(200)  # Délai de 0,2 seconde (200 millisecondes)
            turn = not turn

        check_game_over()  # Vérification si la partie est terminée
        draw_board()
        draw_pieces()
        pygame.display.flip()

# Nouveau mode : 2 IA s'affrontent
def play_with_two_ais():
    global board, game_over
    game_over = False
    turn = True  # True: White's turn, False: Black's turn

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Si c'est le tour de l'IA blanche, effectuer un mouvement avec son niveau
        if turn:
            move = random_move(ai_white_level)
            board.push(move)
            pygame.time.delay(200)  # Délai de 0,2 seconde (200 millisecondes)
            turn = not turn
        # Si c'est le tour de l'IA noire, effectuer un mouvement avec son niveau
        else:
            move = random_move(ai_black_level)
            board.push(move)
            pygame.time.delay(200)  # Délai de 0,2 seconde (200 millisecondes)
            turn = not turn

        check_game_over()  # Vérification si la partie est terminée
        draw_board()
        draw_pieces()
        pygame.display.flip()

# Création de la fenêtre Tkinter pour le menu
def menu_window():
    window = tk.Tk()
    window.title("Menu du jeu d'échecs")
    
    tk.Label(window, text="Choisissez un mode de jeu", font=("Arial", 24)).pack(pady=20)

    def on_mode_select(mode):
        window.destroy()  # Fermer la fenêtre Tkinter
        if mode in ["AI", "2 Players", "2 AI"]:  # Si le mode implique l'IA
            level_selection_window(mode)  # Afficher la fenêtre de sélection de niveau
        else:
            start_game(mode)  # Lancer le jeu pour les autres modes

    tk.Button(window, text="Contre l'IA", font=("Arial", 16), command=lambda: on_mode_select("AI")).pack(pady=10)
    tk.Button(window, text="2 Joueurs", font=("Arial", 16), command=lambda: on_mode_select("2 Players")).pack(pady=10)
    tk.Button(window, text="2 IA", font=("Arial", 16), command=lambda: on_mode_select("2 AI")).pack(pady=10)

    window.mainloop()  # Lancer la boucle Tkinter

def level_selection_window(mode):
    window = tk.Tk()
    window.title("Sélection du niveau de l'IA")
    
    tk.Label(window, text="Choisissez le niveau de l'IA pour les blancs", font=("Arial", 18)).pack(pady=20)
    
    def on_white_level_select(level):
        global ai_white_level
        ai_white_level = level
        level_selection_for_black(window)

    for level in range(1, 6):
        tk.Button(window, text=f"Niveau {level}", font=("Arial", 16), command=lambda level=level: on_white_level_select(level)).pack(pady=10)
    
    window.mainloop()  # Lancer la fenêtre Tkinter

def level_selection_for_black(previous_window):
    previous_window.destroy()  # Fermer la fenêtre précédente

    window = tk.Tk()
    window.title("Sélection du niveau de l'IA")
    
    tk.Label(window, text="Choisissez le niveau de l'IA pour les noirs", font=("Arial", 18)).pack(pady=20)
    
    def on_black_level_select(level):
        global ai_black_level
        ai_black_level = level
        start_game("AI", ai_white_level, ai_black_level)

    for level in range(1, 6):
        tk.Button(window, text=f"Niveau {level}", font=("Arial", 16), command=lambda level=level: on_black_level_select(level)).pack(pady=10)
    
    window.mainloop()  # Lancer la fenêtre Tkinter

# Démarrer la fenêtre de menu
menu_window()