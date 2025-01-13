import pygame
import chess
import random
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

def reset_game():
    global board, game_over
    board = chess.Board()  # Réinitialiser l'échiquier à l'état initial
    game_over = False  # Remettre le flag de fin de jeu à False

def random_move():
    legal_moves = list(board.legal_moves)
    if not legal_moves:
        return None  # Aucun coup légal n'est possible
    return random.choice(legal_moves)

def handle_pawn_promotion(move):
    """Gère la promotion d'un pion si nécessaire."""
    if board.is_legal(move):
        piece = board.piece_at(move.from_square)
        
        # Vérification si c'est bien un pion
        if piece and piece.symbol().upper() == 'P':
            # Vérification de la rangée où le pion atteint pour promouvoir
            if (piece.color == chess.WHITE and chess.square_rank(move.to_square) == 6) or \
               (piece.color == chess.BLACK and chess.square_rank(move.to_square) == 1):
                
                # Appeler la fenêtre pour choisir la pièce
                promotion_choice = promote_pawn()
                if promotion_choice:
                    # Supprimer le pion de la case d'origine
                    board.remove_piece_at(move.from_square)

                    # Créer la pièce choisie pour la promotion
                    piece_type = None
                    if promotion_choice == 'q':
                        piece_type = chess.QUEEN
                    elif promotion_choice == 'r':
                        piece_type = chess.ROOK
                    elif promotion_choice == 'n':
                        piece_type = chess.KNIGHT
                    elif promotion_choice == 'b':
                        piece_type = chess.BISHOP

                    # Créer la nouvelle pièce et la placer sur la case de promotion
                    promoted_piece = chess.Piece(piece_type, piece.color)
                    board.set_piece_at(move.to_square, promoted_piece)

                    return
            
            # Si pas de promotion, jouer le coup normalement
            board.push(move)
        else:
            # Si ce n'est pas un pion, jouer le coup normalement
            board.push(move)

# Fonction IA
def play_with_ai():
    """Jouer contre l'IA avec gestion correcte des promotions."""
    global board, game_over
    game_over = False
    turn = True  # True: White's turn (Player), False: Black's turn (AI)
    selected_square = -1

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and turn:
                square = get_square_under_mouse(event.pos)
                if square != -1:
                    piece = board.piece_at(square)

                    if selected_square == -1:  # Sélectionner une pièce
                        if piece is not None and piece.color == chess.WHITE:
                            selected_square = square
                    else:  # Déplacer la pièce sélectionnée
                        move = chess.Move(selected_square, square)
                        if move in board.legal_moves:
                            handle_pawn_promotion(move)  # Gérer les promotions correctement
                            turn = not turn  # Passer le tour à l'IA

                        else:
                            selected_square = -1  # Réinitialiser la sélection

        if not turn:
            if board.is_checkmate():
                display_winner("Blanc")
                game_over = True
            elif board.is_stalemate() or board.is_insufficient_material() or board.is_seventyfive_moves():
                display_draw("Match nul!")
                game_over = True
            else:
                move = random_move()  # IA joue un mouvement aléatoire
                if move is not None:
                    handle_pawn_promotion(move)
                    turn = not turn  # Retour au joueur
                else:
                    raise ValueError("Aucun coup légal possible.")

        # Dessin du plateau
        draw_board()
        draw_pieces()
        pygame.display.flip()

        # Conditions de fin de partie
        if board.is_checkmate():
            winner = "Noir" if not turn else "Blanc"
            display_winner(winner)
            game_over = True
        elif board.is_stalemate() or board.is_insufficient_material() or board.is_seventyfive_moves():
            display_draw("Match nul!")
            game_over = True

def play_with_two_players():
    """Mode de jeu pour deux joueurs humains."""
    global board, game_over
    game_over = False
    turn = True  # True: White's turn, False: Black's turn
    selected_square = -1  # Aucune case sélectionnée au départ

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Gestion de la sélection et des mouvements
            elif event.type == pygame.MOUSEBUTTONDOWN:
                square = get_square_under_mouse(event.pos)
                if square != -1:
                    piece = board.piece_at(square)

                    if selected_square == -1:  # Aucune pièce sélectionnée
                        if piece is not None and piece.color == (chess.WHITE if turn else chess.BLACK):
                            selected_square = square
                    else:  # Déplacement d'une pièce
                        move = chess.Move(selected_square, square)
                        if move in board.legal_moves:
                            handle_pawn_promotion(move)  # Gérer les promotions
                            selected_square = -1
                            turn = not turn  # Passer au joueur suivant


        # Dessin du plateau
        draw_board()
        draw_pieces()
        pygame.display.flip()

        # Vérification des conditions de fin de partie
        if board.is_checkmate():
            winner = "Noir" if turn else "Blanc"
            display_winner(winner)
            game_over = True
        elif board.is_stalemate() or board.is_insufficient_material() or board.is_seventyfive_moves():
            display_draw("Match nul!")
            game_over = True

def play_ia_vs_ia():
    global board, game_over
    game_over = False
    turn = True  # True: White's turn, False: Black's turn

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Si c'est le tour de l'IA, effectuer un mouvement après un délai de 0,2 sec
        pygame.time.delay(200)  # Délai de 0,2 seconde pour l'IA

        move = random_move()
        board.push(move)
        turn = not turn

        draw_board()
        draw_pieces()
        pygame.display.flip()

        # Vérifier la victoire ou match nul
        if board.is_checkmate():
            display_winner("Blanc" if turn else "Noir")
            game_over = True
        elif board.is_stalemate() or board.is_insufficient_material() or board.is_seventyfive_moves():
            display_draw("Match nul!")
            game_over = True

def start_game(mode):
    global game_over
    if mode == "AI":
        play_with_ai()
    elif mode == "2 Players":
        play_with_two_players()  # Utiliser la fonction mode 2 joueurs
    elif mode == "IA vs IA":
        play_ia_vs_ia()  # Ajouter ce mode IA contre IA

# Création de la fenêtre Tkinter pour le menu
def menu_window():
    window = tk.Tk()
    window.title("Menu de sélection")

    # Définir une taille minimale pour la fenêtre
    window.geometry("300x200")  # Fixer la taille de la fenêtre à 300x200 pixels
    
    def start_ai_game():
        window.destroy()
        start_game("AI")
        
    def start_two_player_game():
        window.destroy()
        start_game("2 Players")
        
    def start_ia_vs_ia_game():
        window.destroy()
        start_game("IA vs IA")
    
    tk.Button(window, text="Jouer contre l'IA", command=start_ai_game).pack(pady=10)
    tk.Button(window, text="Jouer à 2 joueurs", command=start_two_player_game).pack(pady=10)
    tk.Button(window, text="IA vs IA", command=start_ia_vs_ia_game).pack(pady=10)
    
    window.mainloop()

# Démarrer le menu
menu_window()
