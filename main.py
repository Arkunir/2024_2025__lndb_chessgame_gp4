import tkinter as tk
from tkinter import messagebox

class Interface:
    def __init__(self, master):
        self.master = master
        self.master.title("Jeu d'échecs")
        self.create_board()
        self.setup_pieces()

    def create_board(self):
        # Création des coordonnées des colonnes
        columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        
        # Affichage des coordonnées des colonnes en haut
        for col in range(8):
            label = tk.Label(self.master, text=columns[col], width=4, height=2)
            label.grid(row=0, column=col + 1)  # Décalage d'une colonne pour le numéro de ligne

        # Affichage des coordonnées des colonnes en bas
        for col in range(8):
            label = tk.Label(self.master, text=columns[col], width=4, height=2)
            label.grid(row=9, column=col + 1)  # Ligne 9 pour le bas du plateau

        # Affichage des coordonnées des lignes à gauche
        for row in range(8):
            label = tk.Label(self.master, text=str(8 - row), width=4, height=2)
            label.grid(row=row + 1, column=0)  # Décalage d'une ligne pour les lettres de colonne

        # Affichage des coordonnées des lignes à droite
        for row in range(8):
            label = tk.Label(self.master, text=str(8 - row), width=4, height=2)
            label.grid(row=row + 1, column=9)  # Décalage d'une ligne pour les lettres de colonne

        # Création du plateau d'échecs
        self.buttons = {}
        for row in range(8):
            for col in range(8):
                # Changer les couleurs des cases
                color = "#D2B48C" if (row + col) % 2 == 0 else "#FFFACD"  # Marron clair et blanc
                button = tk.Button(self.master, bg=color, width=8, height=4, command=lambda r=row, c=col: self.on_square_click(r, c))
                button.grid(row=row + 1, column=col + 1)  # Décalage d'une ligne et d'une colonne
                self.buttons[(row, col)] = button  # Stocker le bouton pour y accéder plus tard

    def setup_pieces(self):
        # Configuration des pièces sur le plateau
        pieces = {
            'r': '♖', 'n': '♘', 'b': '♗', 'q': '♕', 'k': '♔', 'p': '♙',  # Blanc
            'R': '♜', 'N': '♞', 'B': '♝', 'Q': '♛', 'K': '♚', 'P': '♟'   # Noir
        }

        # Définir la taille de la police pour les pièces
        font_size = 24  # Taille de police souhaitée
        font = ('Arial', font_size)

        # Placer les pièces blanches
        for col in range(8):
            self.buttons[(1, col)].config(text=pieces['P'], font=font)  # Pions blancs
        self.buttons[(0, 0)].config(text=pieces['R'], font=font)
        self.buttons[(0, 1)].config(text=pieces['N'], font=font)
        self.buttons[(0, 2)].config(text=pieces['B'], font=font)
        self.buttons[(0, 3)].config(text=pieces['Q'], font=font)
        self.buttons[(0, 4)].config(text=pieces['K'], font=font)
        self.buttons[(0, 5)].config(text=pieces['B'], font=font)
        self.buttons[(0, 6)].config(text=pieces['N'], font=font)
        self.buttons[(0, 7)].config(text=pieces['R'], font=font)

        
        # Placer les pièces noires
        for col in range(8):
            self.buttons[(6, col)].config(text=pieces['p'], font=font)  # Pions noirs
        self.buttons[(7, 0)].config(text=pieces['r'], font=font)
        self.buttons[(7, 1)].config(text=pieces['n'], font=font)
        self.buttons[(7, 2)].config(text=pieces['b'], font=font)
        self.buttons[(7, 3)].config(text=pieces['q'], font=font)
        self.buttons[(7, 4)].config(text=pieces['k'], font=font)
        self.buttons[(7, 5)].config(text=pieces['b'], font=font)
        self.buttons[(7, 6)].config(text=pieces['n'], font=font)
        self.buttons[(7, 7)].config(text=pieces['r'], font=font)

    def on_square_click(self, row, col):
        # Fonction qui sera appelée lors du clic sur une case
        piece = self.buttons[(row, col)].cget("text")
        if piece:  # Si une pièce est présente
            messagebox.showinfo("Pièce sélectionnée", f"Vous avez sélectionné la pièce: {piece}")
        else:
            messagebox.showinfo("Case vide", "Cette case est vide.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Interface(root)
    root.mainloop()