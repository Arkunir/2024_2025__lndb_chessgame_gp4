from tkinter import Canvas
from pieces import PieceFactory

class Plateau:
    def __init__(self, root):
        self.root = root
        self.canvas = Canvas(root, width=480, height=480)
        self.canvas.pack()

        # Initialiser l'échiquier
        self.board = self.initialize_board()
        self.selected_piece = None

    def initialize_board(self):
        layout = [
            ['t', 'c', 'f', 'd', 'r', 'f', 'c', 't'],  # Noirs
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],  # Blancs
            ['T', 'C', 'F', 'D', 'R', 'F', 'C', 'T']
        ]

        return [[PieceFactory.create_piece(char) for char in row] for row in layout]

    def display(self):
        case_size = 60
        for i in range(8):
            for j in range(8):
                color = "#F5F5DC" if (i + j) % 2 == 0 else "#6F4F28"
                x1, y1 = j * case_size, i * case_size
                x2, y2 = (j + 1) * case_size, (i + 1) * case_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

                piece = self.board[i][j]
                if piece:
                    self.canvas.create_text(
                        x1 + case_size / 2, y1 + case_size / 2,
                        text=piece.symbol, font=("Arial", 24), fill=piece.color
                    )
