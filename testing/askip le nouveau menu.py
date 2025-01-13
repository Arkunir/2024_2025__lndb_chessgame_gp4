import pygame
import chess
import random
import tkinter as tk
from tkinter import messagebox

pygame.init()

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

def promote_pawn():
    promoted_piece = None
    choices = ['Q', 'R', 'N', 'B']

    font = pygame.font.Font(None, 36)
    text = font.render("Choisissez la pièce (Q: Dame, R: Tour, N: Cavalier, B: Fou)", True, (255, 255, 255))
    screen.blit(text, (100, 100))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    promoted_piece = 'Q'
                elif event.key == pygame.K_r:
                    promoted_piece = 'R'
                elif event.key == pygame.K_n:
                    promoted_piece = 'N'
                elif event.key == pygame.K_b:
                    promoted_piece = 'B'

                if promoted_piece:
                    return promoted_piece

        pygame.display.flip()

def display_winner(winner):
    font = pygame.font.Font(None, 72)
    text = font.render(f"Victoire! {winner} ont gagné!", True, (255, 255, 255))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 3))
    
    button_width, button_height = 200, 60
    button_x = WIDTH // 2 - button_width // 2
    button_y = HEIGHT // 2 + 100
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    
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

        screen.fill((0, 0, 0))
        screen.blit(text, text_rect)

        pygame.draw.rect(screen, (255, 255, 255), button_rect)
        button_text = pygame.font.Font(None, 36).render("Rejouer", True, (0, 0, 0))
        screen.blit(button_text, (button_x + (button_width - button_text.get_width()) // 2, button_y + (button_height - button_text.get_height()) // 2))

        pygame.draw.rect(screen, (255, 0, 0), quit_button_rect)
        quit_button_text = pygame.font.Font(None, 36).render("Quitter", True, (255, 255, 255))
        screen.blit(quit_button_text, (button_x + (button_width - quit_button_text.get_width()) // 2, quit_button_y + (button_height - quit_button_text.get_height()) // 2))

        pygame.display.flip()

def display_draw(message):
    font = pygame.font.Font(None, 72)
    text = font.render(message, True, (255, 255, 255))
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    button_width, button_height = 200, 60
    button_x = WIDTH // 2 - button_width // 2
    button_y = HEIGHT // 2 + 100
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    
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

        screen.fill((0, 0, 0))
        screen.blit(text, text_rect)

        pygame.draw.rect(screen, (255, 255, 255), button_rect)
        button_text = pygame.font.Font(None, 36).render("Rejouer", True, (0, 0, 0))
        screen.blit(button_text, (button_x + (button_width - button_text.get_width()) // 2, button_y + (button_height - button_text.get_height()) // 2))

        pygame.draw.rect(screen, (255, 0, 0), quit_button_rect)
        quit_button_text = pygame.font.Font(None, 36).render("Quitter", True, (255, 255, 255))
        screen.blit(quit_button_text, (button_x + (button_width - quit_button_text.get_width()) // 2, quit_button_y + (button_height - quit_button_text.get_height()) // 2))

        pygame.display.flip()

def reset_game():
    global board, game_over
    board = chess.Board()
    game_over = False

def random_move():
    legal_moves = list(board.legal_moves)
    if not legal_moves:
        return None
    return random.choice(legal_moves)

def play_with_ai():
    global board, game_over
    game_over = False
    turn = True
    selected_square = -1

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and turn and not game_over:
                square = get_square_under_mouse(event.pos)
                if square != -1:
                    piece = board.piece_at(square)

                    if selected_square == -1:
                        if piece is not None and piece.color == chess.WHITE:
                            selected_square = square
                    else:
                        move = chess.Move(selected_square, square)

                        if move in board.legal_moves:
                            board.push(move)
                            selected_square = -1
                            turn = not turn

                            if board.piece_at(square) and board.piece_at(square).symbol().upper() == 'P' and \
                               (chess.square_rank(square) == 1 if board.piece_at(square).color == chess.BLACK else chess.square_rank(square) == 6):
                                promotion_piece = promote_pawn()
                                board.push(chess.Move(square, square, promotion=promotion_piece))

                        else:
                            selected_square = -1

        if not turn and not game_over:
            if board.is_checkmate():
                display_winner("Blanc")
                game_over = True
            elif board.is_stalemate() or board.is_insufficient_material() or board.is_seventyfive_moves():
                display_draw("Match nul!")
                game_over = True
            else:
                if not (board.is_checkmate() or board.is_stalemate() or board.is_insufficient_material()):
                    move = random_move()
                    if move is not None:
                        board.push(move)
                        turn = not turn
                    else:
                        raise ValueError("Aucun coup légal n'est possible. Le jeu est terminé.")
                else:
                    game_over = True

        draw_board()
        draw_pieces()
        pygame.display.flip()

        if board.is_checkmate():
            winner = "Noir" if not turn else "Blanc"
            display_winner(winner)
            game_over = True
        elif board.is_stalemate() or board.is_insufficient_material() or board.is_seventyfive_moves():
            display_draw("Match nul!")
            game_over = True

def play_with_two_players():
    global board, game_over
    game_over = False
    turn = True
    selected_square = -1

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                square = get_square_under_mouse(event.pos)
                if square != -1:
                    piece = board.piece_at(square)

                    if selected_square == -1:
                        if piece is not None and piece.color == (chess.WHITE if turn else chess.BLACK):
                            selected_square = square
                    else:
                        move = chess.Move(selected_square, square)

                        if move in board.legal_moves:
                            board.push(move)
                            selected_square = -1
                            turn = not turn

                            if board.piece_at(square) and board.piece_at(square).symbol().upper() == 'P' and \
                               (chess.square_rank(square) == 1 if board.piece_at(square).color == chess.BLACK else chess.square_rank(square) == 6):
                                promotion_piece = promote_pawn()
                                board.push(chess.Move(square, square, promotion=promotion_piece))

                        else:
                            selected_square = -1

        draw_board()
        draw_pieces()
        pygame.display.flip()

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
    turn = True

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.time.delay(200)

        move = random_move()
        board.push(move)
        turn = not turn

        draw_board()
        draw_pieces()
        pygame.display.flip()

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
        play_with_two_players()
    elif mode == "IA vs IA":
        play_ia_vs_ia()

def menu_window():
    window = tk.Tk()
    window.title("Menu de sélection")

    window.geometry("300x200")
    
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

menu_window()
