class Piece:
    def __init__(self, est_blanc):
        self.est_blanc = est_blanc

    def peut_se_deplacer(self, source, destination, grille):
        raise NotImplementedError("Cette méthode doit être implémentée par les sous-classes.")

class Roi(Piece):
    def peut_se_deplacer(self, source, destination, grille):
        x1, y1 = source
        x2, y2 = destination
        dx, dy = abs(x2 - x1), abs(y2 - y1)
        return dx <= 1 and dy <= 1

class Pion(Piece):
    def peut_se_deplacer(self, source, destination, grille):
        x1, y1 = source
        x2, y2 = destination
        direction = -1 if self.est_blanc else 1

        if y1 == y2:  # Avancer tout droit
            if x2 == x1 + direction and not grille[x2][y2]:
                return True
        return False
