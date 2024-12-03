from pieces import Piece, Roi, Pion

class Plateau:
    def __init__(self):
        self.grille = self.initialiser_plateau()
        self.tour_blanc = True

    def initialiser_plateau(self):
        # Création d'un plateau de 8x8 avec des pièces aux positions initiales
        grille = [[None for _ in range(8)] for _ in range(8)]

        # Pions
        for i in range(8):
            grille[1][i] = Pion(False)  # Pions noirs
            grille[6][i] = Pion(True)   # Pions blancs

        # Rois
        grille[0][4] = Roi(False)  # Roi noir
        grille[7][4] = Roi(True)   # Roi blanc

        return grille

    def est_fini(self):
        # Fin si un des rois est capturé
        roi_blanc, roi_noir = False, False
        for ligne in self.grille:
            for piece in ligne:
                if isinstance(piece, Roi):
                    if piece.est_blanc:
                        roi_blanc = True
                    else:
                        roi_noir = True
        return not (roi_blanc and roi_noir)

    def deplacer_piece(self, source, destination):
        x1, y1 = source
        x2, y2 = destination

        piece = self.grille[x1][y1]
        if not piece or piece.est_blanc != self.tour_blanc:
            return False

        if piece.peut_se_deplacer(source, destination, self.grille):
            self.grille[x2][y2] = piece
            self.grille[x1][y1] = None
            self.tour_blanc = not self.tour_blanc
            return True

        return False
