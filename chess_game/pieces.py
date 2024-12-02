# pieces.py

class Piece:
    def __init__(self, color, symbol):
        self.color = color
        self.symbol = symbol

    def move(self, start, end):
        raise NotImplementedError("Les mouvements de la pièce doivent être implémentés dans la classe fille.")

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color, 'P' if color == 'white' else 'p')

    def move(self, start, end):
        # Implémenter le mouvement du pion
        pass

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color, 'R' if color == 'white' else 'r')

    def move(self, start, end):
        # Implémenter le mouvement de la tour
        pass

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color, 'C' if color == 'white' else 'c')

    def move(self, start, end):
        # Implémenter le mouvement du cavalier
        pass

# Tu peux définir les autres pièces de manière similaire.
