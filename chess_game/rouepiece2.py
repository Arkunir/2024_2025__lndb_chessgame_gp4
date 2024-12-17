import tkinter as tk
import random

# Liste des pièces d'échecs avec des poids pour augmenter les chances de choisir un pion
pieces = ["Roi", "Reine", "Tour", "Fou", "Cavalier", "Pion"]
# On répète le pion 5 fois pour augmenter ses chances
pieces_biaisees = pieces + ["Pion"] * 5

# Variable pour mémoriser la pièce choisie précédemment
derniere_piece = None

# Fonction pour sélectionner une pièce au hasard
def choisir_piece():
    global derniere_piece  # Utiliser la variable globale pour la pièce précédente
    derniere_piece = random.choice(pieces_biaisees)
    label_resultat.config(text=f"Pièce choisie : {derniere_piece}")
    btn_relancer.config(state=tk.NORMAL)  # Active le bouton "Refaire le coup"

# Fonction pour relancer le choix, en évitant de revenir à la même pièce
def relancer_choix():
    global derniere_piece  # Utiliser la variable globale pour la pièce précédente
    piece_choisie = random.choice(pieces_biaisees)
    
    # On vérifie que la nouvelle pièce est différente de la précédente
    while piece_choisie == derniere_piece:
        piece_choisie = random.choice(pieces_biaisees)
        
    # Mettre à jour la dernière pièce choisie
    derniere_piece = piece_choisie
    label_resultat.config(text=f"Pièce choisie : {piece_choisie}")

# Créer la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Roulette des pièces d'échecs")
fenetre.geometry("300x250")

# Titre de la fenêtre
label_titre = tk.Label(fenetre, text="Choisissez une pièce d'échecs", font=("Arial", 14))
label_titre.pack(pady=20)

# Bouton pour choisir une pièce
btn_choisir = tk.Button(fenetre, text="Choisir", command=choisir_piece, font=("Arial", 12))
btn_choisir.pack(pady=10)

# Bouton pour relancer le choix (ne peut pas faire le coup), initialement désactivé
btn_relancer = tk.Button(fenetre, text="Ne peut pas faire le coup", command=relancer_choix, font=("Arial", 12), state=tk.DISABLED)
btn_relancer.pack(pady=10)

# Label pour afficher la pièce choisie
label_resultat = tk.Label(fenetre, text="", font=("Arial", 12))
label_resultat.pack(pady=10)

# Lancer l'interface graphique
fenetre.mainloop()
