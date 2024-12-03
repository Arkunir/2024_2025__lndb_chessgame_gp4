class Piece:
    def __init__(self, color, symbol):
        self.color = color
        self.symbol = symbol

    def is_valid_move(self, start, end, board):
        raise NotImplementedError("Mouvement non défini pour cette pièce.")

class Pawn(Piece):
    def is_valid_move(self, start, end, board):
        # Implémentation simplifiée des mouvements du pion
        direction = -1 if self.color == "white" else 1
        dx, dy = end[0] - start[0], end[1] - start[1]
        return (dx == direction and dy == 0)

class Rook(Piece):
    def is_valid_move(self, start, end, board):
        return start[0] == end[0] or start[1] == end[1]

class PieceFactory:
    @staticmethod
    def create_piece(piece_char):
        color = "white" if piece_char.isupper() else "black"
        symbol_map = {
            'P': ('P', Pawn), 'T': ('T', Rook),
            # Ajouter d'autres pièces ici
        }
        symbol = piece_char.upper()
        return symbol_map.get(symbol, (None, None))[1](color, symbol) if symbol in symbol_map else None
