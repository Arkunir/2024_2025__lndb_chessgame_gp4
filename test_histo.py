import tkinter as tk

class HistoriqueCoupApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Historique des Coups")

        self.coups = []

        # Liste pour afficher l'historique des coups
        self.historique_listbox = tk.Listbox(root, width=50, height=10)
        self.historique_listbox.pack(pady=10)

        # Choix de la pièce
        self.piece_var = tk.StringVar(value="Pion")
        self.piece_label = tk.Label(root, text="Choisissez une pièce:")
        self.piece_label.pack()
        self.piece_menu = tk.OptionMenu(root, self.piece_var, 'Pion', 'Cavalier', 'Fou', 'Tour', 'Dame', 'Roi')
        self.piece_menu.pack()

        # Choix de la position de départ
        self.depart_var = tk.StringVar(value="E2")
        self.depart_label = tk.Label(root, text="Position de départ:")
        self.depart_label.pack()
        self.depart_entry = tk.Entry(root)
        self.depart_entry.pack()

        # Choix de la position d'arrivée
        self.arrivee_var = tk.StringVar(value="E4")
        self.arrivee_label = tk.Label(root, text="Position d'arrivée:")
        self.arrivee_label.pack()
        self.arrivee_entry = tk.Entry(root)
        self.arrivee_entry.pack()

        # Case à cocher pour indiquer une capture
        self.capture_var = tk.BooleanVar()
        self.capture_checkbox = tk.Checkbutton(root, text="Capture", variable=self.capture_var)
        self.capture_checkbox.pack()

        # Case à cocher pour indiquer un échec
        self.echec_var = tk.BooleanVar()
        self.echec_checkbox = tk.Checkbutton(root, text="Échec", variable=self.echec_var)
        self.echec_checkbox.pack()

        # Case à cocher pour indiquer un échec et mat
        self.mat_var = tk.BooleanVar()
        self.mat_checkbox = tk.Checkbutton(root, text="Échec et Mat", variable=self.mat_var)
        self.mat_checkbox.pack()

        # Case à cocher pour indiquer un pat
        self.pat_var = tk.BooleanVar()
        self.pat_checkbox = tk.Checkbutton(root, text="Pat", variable=self.pat_var)
        self.pat_checkbox.pack()

        # Case à cocher pour indiquer un rock
        self.pat_var = tk.BooleanVar()
        self.pat_checkbox = tk.Checkbutton(root, text="rock", variable=self.rock_var)
        self.pat_checkbox.pack()

        # Bouton pour jouer le coup
        self.jouer_button = tk.Button(root, text="Jouer le coup", command=self.jouer_coup)
        self.jouer_button.pack(pady=10)

    def jouer_coup(self):
        piece = self.piece_var.get()
        depart = self.depart_entry.get()
        arrivee = self.arrivee_entry.get()

        # Créer le coup de base
        if self.capture_var.get():
            coup = f"{piece} capture à {arrivee} depuis {depart}"
        else:
            coup = f"{piece} déplace de {depart} vers {arrivee}"

        # Ajouter les indications d'échec, d'échec et mat, ou de pat
        if self.echec_var.get():
            coup += " (Échec)"
        if self.mat_var.get():
            coup += " (Échec et Mat)"
        if self.pat_var.get():
            coup += " (Pat)"

        # Ajouter le coup à l'historique
        self.coups.append(coup)
        self.historique_listbox.insert(tk.END, coup)

        # Réinitialiser les entrées et les cases à cocher
        self.depart_entry.delete(0, tk.END)
        self.arrivee_entry.delete(0, tk.END)
        self.capture_var.set(False)
        self.echec_var.set(False)
        self.mat_var.set(False)
        self.pat_var.set(False)
        self.rock_var.set(False)

if __name__ == "__main__":
    root = tk.Tk()
    app = HistoriqueCoupApp(root)
    root.mainloop()