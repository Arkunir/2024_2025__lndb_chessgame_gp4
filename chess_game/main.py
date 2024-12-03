import tkinter as tk
from Plateau import Plateau  # Assurez-vous que le nom correspond

def main():
    # Créer une fenêtre principale Tkinter
    root = tk.Tk()
    root.title("Jeu d'échecs")

    # Initialiser et afficher l'échiquier
    plateau = Plateau(root)
    plateau.display()

    root.mainloop()

if __name__ == "__main__":
    main()
