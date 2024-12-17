import pygame
import chess
import random  # Importer la bibliothèque random

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

def load_pieces():
    pieces = {}
    for piece, filename in PIECE_FILES.items():
        image = pygame.image.load(ASSETS_PATH + filename)
        image = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))
        pieces[piece] = image
    return pieces

PIECES = load_pieces()
board = chess.Board()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu d'échecs")

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

# Fonction IA (joue un coup aléatoire)
def play_random_ai_move():
    legal_moves = list(board.legal_moves)
    if legal_moves:
        move = random.choice(legal_moves)
        if board.is_legal(move):
            board.push(move)

def reset_game():
    global board, game_over
    board = chess.Board()  # Reset the board to the initial state
    game_over = False  # Set game_over flag to False

# Main loop
running = True
selected_square = None
game_over = False  # Flag to check if the game is over
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over and board.turn == chess.WHITE:
            pos = pygame.mouse.get_pos()
            clicked_square = get_square_under_mouse(pos)
            if selected_square is None:
                if board.piece_at(clicked_square):
                    selected_square = clicked_square
            else:
                move = chess.Move(selected_square, clicked_square)
                if move in board.legal_moves:
                    piece = board.piece_at(selected_square)
                    if piece.symbol().lower() == 'p' and (chess.square_rank(clicked_square) == 0 or chess.square_rank(clicked_square) == 7):
                        # Promotion logic
                        promotion = promote_pawn()  # Call the promote_pawn function for user input
                        move.promotion = chess.Piece.from_symbol(promotion).piece_type
                    board.push(move)
                selected_square = None

    # Vérification de la fin de partie
    if board.is_checkmate():
        winner = "Les blancs" if board.turn == chess.BLACK else "Les noirs"
        game_over = True
        if display_winner(winner) == "replay":
            reset_game()
    elif board.is_stalemate():
        game_over = True
        if display_draw("Match nul! (Pat)") == "replay":
            reset_game()
    elif board.is_repetition(3):
        game_over = True
        if display_draw("Match nul! (Trois répétitions)") == "replay":
            reset_game()

    # Si c'est le tour de l'IA (joue les noirs)
    if not game_over and board.turn == chess.BLACK:
        play_random_ai_move()

    draw_board()
    draw_pieces()
    pygame.display.flip()

pygame.quit()
