import pygame
import chess

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
WIDTH, HEIGHT = 800, 800  # Taille de la fenêtre
ROWS, COLS = 8, 8  # Dimensions de l'échiquier
SQUARE_SIZE = WIDTH // COLS  # Taille d'une case

# Couleurs de l'échiquier
LIGHT_BROWN = (240, 217, 181)
DARK_BROWN = (181, 136, 99)

# Chemin des fichiers de pièces
ASSETS_PATH = "game_chess/assets/"  # Dossier contenant les fichiers PNG des pièces
PIECE_FILES = {
    'P': "P.png", 'N': "N.png", 'B': "B.png", 'R': "R.png", 'Q': "Q.png", 'K': "K.png",  # Pièces noires
    'p': "wP.png", 'n': "wN.png", 'b': "wB.png", 'r': "wR.png", 'q': "wQ.png", 'k': "wK.png"   # Pièces blanches
}

# Fonction pour charger les images des pièces
def load_pieces():
    pieces = {}
    for piece, filename in PIECE_FILES.items():
        image = pygame.image.load(ASSETS_PATH + filename)  # Mise à jour du chemin d'accès
        image = pygame.transform.scale(image, (SQUARE_SIZE, SQUARE_SIZE))  # Redimensionner à la taille de la case
        pieces[piece] = image
    return pieces

# Chargement des pièces
PIECES = load_pieces()

# Configuration initiale de l'échiquier
board = chess.Board()

# Créer la fenêtre Pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu d'échecs")

# Dessiner l'échiquier
def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            color = LIGHT_BROWN if (row + col) % 2 == 0 else DARK_BROWN
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Dessiner les pièces sur l'échiquier
def draw_pieces():
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            col = chess.square_file(square)  # Colonne de la case
            row = chess.square_rank(square)  # Ligne de la case
            image = PIECES[piece.symbol()]
            # Placer l'image de la pièce dans la bonne case
            screen.blit(image, (col * SQUARE_SIZE, (7 - row) * SQUARE_SIZE))  # 7-row pour inverser la ligne

# Traduire un clic en coordonnées d'échiquier
def get_square_under_mouse(pos):
    x, y = pos
    col = x // SQUARE_SIZE
    row = 7 - (y // SQUARE_SIZE)  # Inverser la ligne pour s'adapter à la notation des échecs
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

    # Dessiner l'échiquier et les pièces à chaque boucle
    draw_board()
    draw_pieces()

    # Mettre à jour l'écran
    pygame.display.flip()

# Quitter Pygame
pygame.quit()
