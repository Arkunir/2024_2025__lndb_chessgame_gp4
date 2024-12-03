def afficher_plateau(plateau):
    for ligne in plateau.grille:
        for case in ligne:
            if case is None:
                print('.', end=' ')
            else:
                print(case.__class__.__name__[0], end=' ')
        print()
    print()

def demander_deplacement():
    try:
        source = input("Entrez la position de départ (format: x y) : ")
        destination = input("Entrez la position d'arrivée (format: x y) : ")
        x1, y1 = map(int, source.split())
        x2, y2 = map(int, destination.split())
        return (x1, y1), (x2, y2)
    except ValueError:
        print("Format invalide, veuillez réessayer.")
        return demander_deplacement()
