import tkinter as tk
import random

pieces = ["Roi", "Reine", "Tour", "Fou", "Cavalier", "Pion"]
pieces_biaisees = pieces + ["Pion"] * 5

derniere_piece = None

def choisir_piece():
    global derniere_piece  
    derniere_piece = random.choice(pieces_biaisees)
    label_resultat.config(text=f"Pièce choisie : {derniere_piece}")
    btn_relancer.config(state=tk.NORMAL) 

def relancer_choix():
    global derniere_piece 
    
    while piece_choisie == derniere_piece:
        piece_choisie = random.choice(pieces_biaisees)
        
    derniere_piece = piece_choisie
    label_resultat.config(text=f"Pièce choisie : {piece_choisie}")

fenetre = tk.Tk()
fenetre.title("Roulette des pièces d'échecs")
fenetre.geometry("300x250")

label_titre = tk.Label(fenetre, text="Choisissez une pièce d'échecs", font=("Arial", 14))
label_titre.pack(pady=20)

btn_choisir = tk.Button(fenetre, text="Choisir", command=choisir_piece, font=("Arial", 12))
btn_choisir.pack(pady=10)

btn_relancer = tk.Button(fenetre, text="Ne peut pas faire le coup", command=relancer_choix, font=("Arial", 12), state=tk.DISABLED)
btn_relancer.pack(pady=10)

label_resultat = tk.Label(fenetre, text="", font=("Arial", 12))
label_resultat.pack(pady=10)

fenetre.mainloop()
