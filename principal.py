import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Dimensions de l'échiquier
WIDTH, HEIGHT = 800, 800
SQUARE_SIZE = WIDTH // 8

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)

# Classe de base pour les pièces
class Piece:
    def __init__(self, color):
        self.color = color

    def valid_move(self, start, end, board):
        raise NotImplementedError("Cette méthode doit être implémentée par les sous-classes.")

# Sous-classes pour chaque type de pièce
class King(Piece):
    def valid_move(self, start, end, board):
        return abs(start[0] - end[0]) <= 1 and abs(start[1] - end[1]) <= 1

class Queen(Piece):
    def valid_move(self, start, end, board):
        return (start[0] == end[0] or start[1] == end[1] or
                abs(start[0] - end[0]) == abs(start[1] - end[1]))

class Rook(Piece):
    def valid_move(self, start, end, board):
        if start[0] == end[0]:  # Mouvement horizontal
            step = 1 if end[1] > start[1] else -1
            for col in range(start[1] + step, end[1], step):
                if board[start[0]][col] is not None:
                    return False
            return True
        elif start[1] == end[1]:  # Mouvement vertical
            step = 1 if end[0] > start[0] else -1
            for row in range(start[0] + step, end[0], step):
                if board[row][start[1]] is not None:
                    return False
            return True
        return False

class Bishop(Piece):
    def valid_move(self, start, end, board):
        if abs(start[0] - end[0]) == abs(start[1] - end[1]):  # Mouvement diagonal
            step_row = 1 if end[0] > start[0] else -1
            step_col = 1 if end[1] > start[1] else -1
            row, col = start[0] + step_row, start[1] + step_col
            while (row != end[0] and col != end[1]):
                if board[row][col] is not None:
                    return False
                row += step_row
                col += step_col
            return True
        return False

class Knight(Piece):
    def valid_move(self, start, end, board):
        return (abs(start[0] - end[0]), abs(start[1] - end[1])) in [(2, 1), (1, 2)]

class Pawn(Piece):
    def valid_move(self, start, end, board):
        direction = 1 if self.color == 'white' else -1
        start_row = 6 if self.color == 'white' else 1
        
        # Mouvement normal d'une case
        if start[1] == end[1]:  # Mouvement vertical
            if end[0] - start[0] == direction and board[end[0]][end[1]] is None:
                return True
            # Mouvement de deux cases depuis la position de départ
            if start[0] == start_row and end[0] - start[0] == 2 * direction and board[end[0]][end[1]] is None and board[start[0] + direction][start[1]] is None:
                return True
        # Capture
        elif abs(start[1] - end[1]) == 1 and end[0] - start[0] == direction:  
            if board[end[0]][end[1]] is not None and board[end[0]][end[1]].color != self.color:
                return True
        return False

class ChessGame:
    def __init__(self):
        self.board = self.create_board()
        self.current_turn = 'white'
        self.history = []

    def create_board(self):
        # Créez l'échiquier avec des pièces
        board = [[None for _ in range(8)] for _ in range(8)]
        board[0][0] = Rook('black')
        board[0][1] = Knight('black')
        board[0][2] = Bishop('black')
        board[0][3] = Queen('black')
        board[0][4] = King('black')
        board[0][5] = Bishop('black')
        board[0][6] = Knight('black')
        board[0][7] = Rook('black')
        for i in range(8):
            board[1][i] = Pawn('black')
        for i in range(8):
            board[6][i] = Pawn('white')
        board[7][0] = Rook('white')
        board[7][1] = Knight('white')
        board[7][2] = Bishop('white')
        board[7][3] = Queen('white')
        board[7][4] = King('white')
        board[7][5] = Bishop('white')
        board[7][6] = Knight('white')
        board[7][7] = Rook('white')
        return board

    def move_piece(self, start, end):
        piece = self.board[start[0]][start[1]]
        if piece and piece.color == self.current_turn and piece.valid_move(start, end, self.board):
            self.history.append((start, end))
            self.board[end[0]][end[1]] = piece
            self.board[start[0]][start[1]] = None
            self.current_turn = 'black' if self.current_turn == 'white' else 'white'

    def draw_board(self, screen):
        for row in range(8):
            for col in range(8):
                color = LIGHT_GRAY if (row + col) % 2 == 0 else DARK_GRAY
                pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                piece = self.board[row][col]
                if piece:
                    self.draw_piece(screen, piece, col, row)

    def draw_piece(self, screen, piece, col, row):
        font = pygame.font.Font(None, 74)
        text = font.render(piece.__class__.__name__[0].upper() if piece.color == 'white' else piece.__class__.__name__[0].lower(), True, BLACK)
        screen.blit(text, (col * SQUARE_SIZE + SQUARE_SIZE // 4, row * SQUARE_SIZE + SQUARE_SIZE // 4))

# Boucle principale du jeu
def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Échecs")
    game = ChessGame()

    selected_piece = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                col = pos[0] // SQUARE_SIZE
                row = pos[1] // SQUARE_SIZE
                if selected_piece:
                    # Si une pièce est déjà sélectionnée, essayez de déplacer
                    start = selected_piece
                    end = (row, col)
                    game.move_piece(start, end)
                    selected_piece = None  # Désélectionner après le mouvement
                else:
                    # Sélectionner une pièce
                    if game.board[row][col] is not None and game.board[row][col].color == game.current_turn:
                        selected_piece = (row, col)

        # Dessiner l'échiquier et les pièces
        screen.fill(WHITE)
        game.draw_board(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()