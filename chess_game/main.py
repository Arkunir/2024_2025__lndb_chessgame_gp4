# main.py
import tkinter as tk
from board import Board

def main():
    # Créer la fenêtre principale Tkinter
    root = tk.Tk()
    root.title("Jeu d'échecs")

    # Créer l'échiquier et l'afficher
    board = Board(root)
    board.display()

    # Lancer la boucle Tkinter
    root.mainloop()

if __name__ == "__main__":
    main()
