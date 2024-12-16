import tkinter as tk

class Piece:
    def __init__(self, color, symbol):
        self.color = color
        self.symbol = symbol

    def is_valid_move(self, start, end, board):
        raise NotImplementedError("Mouvement non défini pour cette pièce.")


class Pawn(Piece):
    def __init__(self, color):
        symbol = 'p' if color == 'black' else 'P'
        super().__init__(color, symbol)
        self.has_moved = False

    def is_valid_move(self, start, end, board):
        direction = -1 if self.color == 'white' else 1
        dx, dy = end[0] - start[0], end[1] - start[1]

        if dx == direction and dy == 0 and board[end[0]][end[1]] is None:
            return True

        if dx == 2 * direction and dy == 0 and not self.has_moved:
            middle = (start[0] + end[0]) // 2
            if board[middle][start[1]] is None and board[end[0]][end[1]] is None:
                return True

        if dx == direction and abs(dy) == 1 and board[end[0]][end[1]] is not None:
            target_piece = board[end[0]][end[1]]
            if target_piece.color != self.color:
                return True

        return False

    def move(self, start, end):
        self.has_moved = True


class Rook(Piece):
    def __init__(self, color):
        symbol = 'r' if color == 'black' else 'R'
        super().__init__(color, symbol)

    def is_valid_move(self, start, end, board):
        return start[0] == end[0] or start[1] == end[1]


class Knight(Piece):
    def __init__(self, color):
        symbol = 'n' if color == 'black' else 'N'
        super().__init__(color, symbol)

    def is_valid_move(self, start, end, board):
        dx, dy = abs(end[0] - start[0]), abs(end[1] - start[1])
        return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)


class Bishop(Piece):
    def __init__(self, color):
        symbol = 'b' if color == 'black' else 'B'
        super().__init__(color, symbol)

    def is_valid_move(self, start, end, board):
        dx, dy = abs(end[0] - start[0]), abs(end[1] - start[1])
        return dx == dy


class Queen(Piece):
    def __init__(self, color):
        symbol = 'q' if color == 'black' else 'Q'
        super().__init__(color, symbol)

    def is_valid_move(self, start, end, board):
        return Rook(self.color).is_valid_move(start, end, board) or Bishop(self.color).is_valid_move(start, end, board)


class King(Piece):
    def __init__(self, color):
        symbol = 'k' if color == 'black' else 'K'
        super().__init__(color, symbol)

    def is_valid_move(self, start, end, board):
        dx, dy = abs(end[0] - start[0]), abs(end[1] - start[1])
        return dx <= 1 and dy <= 1


class PieceFactory:
    @staticmethod
    def create_piece(char):
        if char == 'p' or char == 'P':
            return Pawn('black' if char == 'p' else 'white')
        elif char == 'r' or char == 'R':
            return Rook('black' if char == 'r' else 'white')
        elif char == 'n' or char == 'N':
            return Knight('black' if char == 'n' else 'white')
        elif char == 'b' or char == 'B':
            return Bishop('black' if char == 'b' else 'white')
        elif char == 'q' or char == 'Q':
            return Queen('black' if char == 'q' else 'white')
        elif char == 'k' or char == 'K':
            return King('black' if char == 'k' else 'white')
        else:
            return None


class Plateau:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=480, height=480)
        self.canvas.pack()

        self.board = self.initialize_board()
        self.selected_piece = None
        self.selected_position = None
        self.current_turn = 'white' 

        self.canvas.bind("<Button-1>", self.on_click)

    def initialize_board(self):
        layout = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],  
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],  
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], 
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],  
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],  
        ]
        return [[PieceFactory.create_piece(char) for char in row] for row in layout]

    def display(self):
        self.canvas.delete("all")  
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
                        text=piece.symbol, font=("Arial", 32), 
                        fill="black"
                    )

        self.canvas.create_text(240, 500, text=f"C'est au tour des {'Blancs' if self.current_turn == 'white' else 'Noirs'}", font=("Arial", 16))

    def on_click(self, event):
        case_size = 60
        x, y = event.x // case_size, event.y // case_size

        if self.selected_piece:
            start = self.selected_position
            end = (y, x)
            piece = self.selected_piece

            if piece.color != self.current_turn:
                return

            try:
                if piece.is_valid_move(start, end, self.board):
                    self.board[end[0]][end[1]] = piece
                    self.board[start[0]][start[1]] = None
                    piece.move(start, end)

                    self.switch_turn()
                    self.selected_piece = None
                    self.selected_position = None
                else:
                    self.show_invalid_move_message()
            except Exception:
                self.show_invalid_move_message()

        else:
            selected_piece = self.board[y][x]
            if selected_piece and selected_piece.color == self.current_turn:
                self.selected_piece = selected_piece
                self.selected_position = (y, x)

        self.display()

    def show_invalid_move_message(self):
        self.canvas.create_text(240, 520, text="Mouvement invalide !", font=("Arial", 12), fill="red")

    def switch_turn(self):
        self.current_turn = 'black' if self.current_turn == 'white' else 'white'


def main():
    root = tk.Tk()
    root.title("Jeu d'échecs")
    plateau = Plateau(root)
    plateau.display()
    root.mainloop()


if __name__ == "__main__":
    main()
