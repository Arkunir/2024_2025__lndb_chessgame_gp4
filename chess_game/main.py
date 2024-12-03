from plateau import Plateau
from utils import afficher_plateau, demander_deplacement

def main():
    plateau = Plateau()
    afficher_plateau(plateau)

    while not plateau.est_fini():
        print(f"Tour du joueur {'blanc' if plateau.tour_blanc else 'noir'}")
        source, destination = demander_deplacement()

        if plateau.deplacer_piece(source, destination):
            afficher_plateau(plateau)
        else:
            print("Déplacement invalide, essayez à nouveau.")

    print("Partie terminée !")
    print("Gagnant :", "Blancs" if plateau.tour_blanc else "Noirs")

if __name__ == "__main__":
    main()
