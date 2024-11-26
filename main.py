import tkinter as tk
from tkinter import messagebox

class Interface:
    def __init__(self, master):
        self.master = master
        self.master.title("Jeu d'échecs")
        self.create_board()
        self.setup_pieces()

    def create_board(self):
        columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        
        # Configuration des colonnes pour qu'elles aient la même taille
        for col in range(8):
            self.master.grid_columnconfigure(col + 1, weight=1)

        # Configuration des lignes pour qu'elles aient la même taille
        for row in range(8):
            self.master.grid_rowconfigure(row + 1, weight=1)

        for col in range(8):
            label = tk.Label(self.master, text=columns[col], width=4, height=2)
            label.grid(row=0, column=col + 1)

        for col in range(8):
            label = tk.Label(self.master, text=columns[col], width=4, height=2)
            label.grid(row=9, column=col + 1)

        for row in range(8):
            label = tk.Label(self.master, text=str(8 - row), width=4, height=2)
            label.grid(row=row + 1, column=0)

        for row in range(8):
            label = tk.Label(self.master, text=str(8 - row), width=4, height=2)
            label.grid(row=row + 1, column=9)

        self.buttons = {}
        for row in range(8):
            for col in range(8):
                color = "#D2B48C" if (row + col) % 2 == 0 else "#FFFACD"
                button = tk.Button(self.master, bg=color, command=lambda r=row, c=col: self.on_square_click(r, c))
                button.grid(row=row + 1, column=col + 1, sticky="nsew")
                self.buttons[(row, col)] = button
                button.config(text=" ")  # Définir une case vide avec un espace

    def setup_pieces(self):
        pieces = {
            'r': '♖', 'n': '♘', 'b': '♗', 'q': '♕', 'k': '♔', 'p': '♙',
            'R': '♜', 'N': '♞', 'B': '♝', 'Q': '♛', 'K': '♚', 'P': '♟'
        }
        font_size = 32  # Ajustez la taille de la police pour qu'elle remplisse 80% de la case
        font = ('Arial', font_size)

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
        piece = self.buttons[(row, col)].cget("text")
        if piece.strip():  # Vérifie si une pièce est présente (non vide)
            messagebox.showinfo("Pièce sélectionnée", f"Vous avez sélectionné la pièce: {piece}")
        else:
            messagebox.showinfo("Case vide", "Cette case est vide.")

if __name__ == "__main__":
    root = tk.Tk()
    app = Interface(root)
    root.mainloop()
    from tkinter import *

def toggle_fullscreen(event=None):
    global fullscreen
    fullscreen = not fullscreen
    root.attributes('-fullscreen', fullscreen)

def end_fullscreen(event=None):
    global fullscreen
    fullscreen = False
    root.attributes('-fullscreen', False)

fullscreen = True
root = Tk()

# Lier les événements pour activer/désactiver le plein écran
root.bind("<F11>", toggle_fullscreen)  # Appuyer sur F11 pour basculer en plein écran
root.bind("<Escape>", end_fullscreen)   # Appuyer sur Échap pour quitter le plein écran

# Configuration de la fenêtre
root.attributes('-fullscreen', fullscreen)

# Exemple de contenu
label = Label(root, text="Appuyez sur F11 pour basculer en plein écran\nAppuyez sur Échap pour quitter", font=('Arial', 24))
label.pack(expand=True)

root.mainloop()