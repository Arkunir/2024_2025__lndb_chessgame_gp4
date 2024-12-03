import pygame
import chess

# Initialisation de Pygame
pygame.init()

# Dimensions
WIDTH, HEIGHT = 800, 800  # Taille de la fenêtre
ROWS, COLS = 8, 8  # Dimensions de l'échiquier
SQUARE_SIZE = WIDTH // COLS  # Taille d'une case

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BROWN = (240, 217, 181)
DARK_BROWN = (181, 136, 99)

# Chargement des images des pièces
PIECES = {}
for piece in ['P', 'N', 'B', 'R', 'Q', 'K', 'p', 'n', 'b', 'r', 'q', 'k']:
    PIECES[piece] = pygame.transform.scale(
        pygame.image.load(f'assets/{piece}.png'),
        (SQUARE_SIZE, SQUARE_SIZE)
    )

# Configuration initiale de l'échiquier
board = chess.Board()

# Créer la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu d'échecs")

# Dessiner l'échiquier
def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            color = LIGHT_BROWN if (row + col) % 2 == 0 else DARK_BROWN
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Dessiner les pièces
def draw_pieces():
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            col = chess.square_file(square)  # Colonne de la case
            row = chess.square_rank(square)  # Ligne de la case
            image = PIECES[piece.symbol()]
            screen.blit(image, (col * SQUARE_SIZE, (7 - row) * SQUARE_SIZE))

# Traduire un clic en coordonnées d'échiquier
def get_square_under_mouse(pos):
    x, y = pos
    col = x // SQUARE_SIZE
    row = 7 - (y // SQUARE_SIZE)
    return chess.square(col, row)

# Main loop
running = True
selected_square = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            clicked_square = get_square_under_mouse(pos)

            # Sélectionner une case ou effectuer un déplacement
            if selected_square is None:
                if board.piece_at(clicked_square):
                    selected_square = clicked_square
            else:
                move = chess.Move(selected_square, clicked_square)
                if move in board.legal_moves:
                    board.push(move)
                selected_square = None

    # Dessiner l'échiquier et les pièces
    draw_board()
    draw_pieces()

    # Mettre à jour l'écran
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
