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

        # Choix d'une action additionnelle
        self.action_additionnelle_var = tk.StringVar(value="")
        self.action_additionnelle_label = tk.Label(root, text="Choisissez une action additionnelle:")
        self.action_additionnelle_label.pack()
        self.action_additionnelle_menu = tk.OptionMenu(root, self.action_additionnelle_var, 'Aucune', 'Capture', 'Échec', 'Échec et Mat', 'Pat', 'Rock')
        self.action_additionnelle_menu.pack()

        # Bouton pour jouer le coup
        self.jouer_button = tk.Button(root, text="Jouer le coup", command=self.jouer_coup)
        self.jouer_button.pack(pady=10)

    def jouer_coup(self):
        piece = self.piece_var.get()
        depart = self.depart_entry.get()
        arrivee = self.arrivee_entry.get()

        # Créer le coup de base
        coup = f"{piece} déplace de {depart} vers {arrivee}"

        # Ajouter l'action additionnelle si sélectionnée
        action_additionnelle = self.action_additionnelle_var.get()
        if action_additionnelle != 'Aucune':
            coup += f" ({action_additionnelle})"

        # Ajouter le coup à l'historique
        self.coups.append(coup)
        self.historique_listbox.insert(tk.END, coup)

        # Réinitialiser les entrées et le menu déroulant
        self.depart_entry.delete(0, tk.END)
        self.arrivee_entry.delete(0, tk.END)
        self.action_additionnelle_var.set('Aucune')  # Reset the additional action menu

if __name__ == "__main__":
    root = tk.Tk()
    app = HistoriqueCoupApp(root)
    root.mainloop()