import tkinter as tk
from tkinter import messagebox

class Interface:
    def __init__(self, master):
        self.master = master
        self.master.title("Jeu d'échecs")
        
        # Initialiser le mode plein écran
        self.fullscreen = True
        self.master.attributes('-fullscreen', self.fullscreen)

        # Lier les événements pour activer/désactiver le plein écran
        self.master.bind("<F11>", self.toggle_fullscreen)  # Appuyer sur F11 pour basculer en plein écran
        self.master.bind("<Escape>", self.end_fullscreen)   # Appuyer sur Échap pour quitter le plein écran

        self.buttons = {}
        self.create_board()

    def create_board(self):
        # Créer le plateau d'échecs
        for row in range(8):
            for col in range(8):
                color = 'white' if (row + col) % 2 == 0 else 'black'
                button = tk.Button(self.master, bg=color, width=8, height=4,
                                   command=lambda r=row, c=col: self.on_square_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[(row, col)] = button

        self.setup_pieces()

    def setup_pieces(self):
        pieces = {
            'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔', 'P': '♙',
            'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♟', 'p': '♟'
        }
        font = ('Arial', 32)

        # Placer les pièces blanches
        self.buttons[(0, 0)].config(text=pieces['R'], font=font)
        self.buttons[(0, 1)].config(text=pieces['N'], font=font)
        self.buttons[(0, 2)].config(text=pieces['B'], font=font)
        self.buttons[(0, 3)].config(text=pieces['Q'], font=font)
        self.buttons[(0, 4)].config(text=pieces['K'], font=font)
        self.buttons[(0, 5)].config(text=pieces['B'], font=font)
        self.buttons[(0, 6)].config(text=pieces['N'], font=font)
        self.buttons[(0, 7)].config(text=pieces['R'], font=font)
        for col in range(8):
            self.buttons[(1, col)].config(text=pieces['P'], font=font)

        # Placer les pièces noires
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

    def toggle_fullscreen(self, event=None):
        self.fullscreen = not self.fullscreen
        self.master.attributes('-fullscreen', self.fullscreen)

    def end_fullscreen(self, event=None):
        self.fullscreen = False
        self.master.attributes('-fullscreen', False)

if __name__ == "__main__":
    root = tk.Tk()
    app = Interface(root)
    root.mainloop()