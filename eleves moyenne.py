eleves = {
    "Jaquesson Michel": {
        "Maths": [11.5, 8, 4.5, 12.75, 7],
        "Français": [8.75, 9.5]
    },
    "Bidant Joé": {
        "Maths": [13, 15, 16.25, 17, 18.5, 19],
        "Français": [13, 14, 15.5, 16.25]
    },
    "Mandela Nelson": {
        "Maths": [18, 15.5, 19.25, 20, 17.75, 18.25],
        "Français": [14, 16.25, 13.75, 18]
    }
}

def moyenne(eleve, matiere):
    notes = eleves[eleve][matiere]
    return sum(notes) / len(notes)

def meilleur_eleve(matiere):
    best_eleve = None
    best_moyenne = -1

    for eleve in eleves:
        moy = moyenne(eleve, matiere)
        if moy > best_moyenne:
            best_moyenne = moy
            best_eleve = eleve

    return best_eleve, best_moyenne

matiere = "Maths"
print(f"{meilleur_eleve(matiere)[0]} avec une moyenne de {meilleur_eleve(matiere)[1]:.2f}")