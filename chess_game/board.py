import tkinter as tk

# Fonction pour afficher l'échiquier
def afficher_echiquier():
    # Liste représentant l'échiquier avec les pièces (normalement en bas les pièces blanches et en haut les pièces noires)
    echiquier = [
        ['T', 'C', 'F', 'D', 'R', 'F', 'C', 'T'],  # Lignes des pièces blanches
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],  # Lignes des pièces noires
        ['t', 'c', 'f', 'd', 'r', 'f', 'c', 't']
    ]

    # Créer la fenêtre principale
    root = tk.Tk()
    root.title("Jeu d'échecs")

    # Dimensions de chaque case
    case_size = 60

    # Créer un canevas pour l'échiquier
    canvas = tk.Canvas(root, width=8 * case_size, height=8 * case_size)
    canvas.pack()

    # Dessiner l'échiquier avec les couleurs modifiées
    for i in range(8):
        for j in range(8):
            # Alterner les couleurs beige clair et marron
            if (i + j) % 2 == 0:
                color = "#F5F5DC"  # Beige clair
            else:
                color = "#6F4F28"  # Marron
            x1, y1 = j * case_size, i * case_size
            x2, y2 = (j + 1) * case_size, (i + 1) * case_size
            canvas.create_rectangle(x1, y1, x2, y2, fill=color)

            # Ajouter la pièce correspondante, mais en inversant l'ordre des lignes
            piece = echiquier[7 - i][j]  # Inverser l'ordre des lignes
            if piece != ' ':
                canvas.create_text(x1 + case_size / 2, y1 + case_size / 2, text=piece, font=("Arial", 24))

    # Lancer la boucle principale de Tkinter
    root.mainloop()

# Appeler la fonction pour afficher l'échiquier
afficher_echiquier()
