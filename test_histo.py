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
        self.depart_label = tk.Label(root, text="Position de départ (ex: E2):")
        self.depart_label.pack()
        self.depart_entry = tk.Entry(root)
        self.depart_entry.pack()

        # Choix de la position d'arrivée
        self.arrivee_label = tk.Label(root, text="Position d'arrivée (ex: E4):")
        self.arrivee_label.pack()
        self.arrivee_entry = tk.Entry(root)
        self.arrivee_entry.pack()

        # Choix de l'action effectuée
        self.action_var = tk.StringVar(value="Déplacement")
        self.action_label = tk.Label(root, text="Choisissez une action:")
        self.action_label.pack()
        self.action_menu = tk.OptionMenu(root, self.action_var, 'Déplacement', 'Rock', 'Pat', 'Echec', 'Echec Et Mat', 'Prend une piece', 'Promotions')
        self.action_menu.pack()

        # Choix d'une action additionnelle
        self.action_additionnelle_var = tk.StringVar(value="Aucune")
        self.action_additionnelle_label = tk.Label(root, text="Choisissez une action additionnelle:")
        self.action_additionnelle_label.pack()
        self.action_additionnelle_menu = tk.OptionMenu(root, self.action_additionnelle_var, 'Aucune', 'Capture', 'Échec', 'Échec et Mat', 'Pat', 'Rock')
        self.action_additionnelle_menu.pack()

        # Bouton pour jouer le coup
        self.jouer_button = tk.Button(root, text="Jouer le coup", command=self.jouer_coup)
        self.jouer_button.pack(pady=10)

        # Vérifier la validité des coordonnées au démarrage
        self.verifier_coordonnees()

        # Lier la vérification des coordonnées à la modification des champs
        self.depart_entry.bind("<KeyRelease>", lambda event: self.verifier_coordonnees())
        self.arrivee_entry.bind("<KeyRelease>", lambda event: self.verifier_coordonnees())

    def est_coordonnees_valides(self, coord):
        """Vérifie si les coordonnées sont valides (ex: E2)."""
        if len(coord) != 2:
            return False
        colonne, ligne = coord[0].upper(), coord[1]
        return colonne in 'ABCDEFGH' and ligne in '12345678'

    def verifier_coordonnees(self):
        """Vérifie les coordonnées et active/désactive le bouton Jouer."""
        depart = self.depart_entry.get()
        arrivee = self.arrivee_entry.get()

        if self.est_coordonnees_valides(depart) and self.est_coordonnees_valides(arrivee):
            self.jouer_button.config(state='normal')  # Activer le bouton
        else:
            self.jouer_button.config(state='disabled')  # Désactiver le bouton

    def jouer_coup(self):
        piece = self.piece_var.get()
        depart = self.depart_entry.get()
        arrivee = self.arrivee_entry.get()
        action = self.action_var.get()
        action_additionnelle = self.action_additionnelle_var.get()

        # Créer le coup de base
        coup = f"{piece} {action} de {depart} vers {arrivee}"

        # Ajouter l'action additionnelle si sélectionnée
        if action_additionnelle != 'Aucune':
            coup += f" ({action_additionnelle})"

        # Ajouter le coup à l'historique
        self.coups.append(coup)
        self.historique_listbox.insert(tk.END, coup)

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
        self.depart_label = tk.Label(root, text="Position de départ (ex: E2):")
        self.depart_label.pack()
        self.depart_entry = tk.Entry(root)
        self.depart_entry.pack()

        # Choix de la position d'arrivée
        self.arrivee_label = tk.Label(root, text="Position d'arrivée (ex: E4):")
        self.arrivee_label.pack()
        self.arrivee_entry = tk.Entry(root)
        self.arrivee_entry.pack()

        # Choix de l'action effectuée
        self.action_var = tk.StringVar(value="Déplacement")
        self.action_label = tk.Label(root, text="Choisissez une action:")
        self.action_label.pack()
        self.action_menu = tk.OptionMenu(root, self.action_var, 'Déplacement', 'Rock', 'Pat', 'Echec', 'Echec Et Mat', 'Prend une piece', 'Promotions')
        self.action_menu.pack()

        # Choix d'une action additionnelle
        self.action_additionnelle_var = tk.StringVar(value="Aucune")
        self.action_additionnelle_label = tk.Label(root, text="Choisissez une action additionnelle:")
        self.action_additionnelle_label.pack()
        self.action_additionnelle_menu = tk.OptionMenu(root, self.action_additionnelle_var, 'Aucune', 'Échec', 'Échec et Mat', 'Pat')
        self.action_additionnelle_menu.pack()

        # Bouton pour jouer le coup
        self.jouer_button = tk.Button(root, text="Jouer le coup", command=self.jouer_coup)
        self.jouer_button.pack(pady=10)

        # Vérifier la validité des coordonnées au démarrage
        self.verifier_coordonnees()

        # Lier la vérification des coordonnées à la modification des champs
        self.depart_entry.bind("<KeyRelease>", lambda event: self.verifier_coordonnees())
        self.arrivee_entry.bind("<KeyRelease>", lambda event: self.verifier_coordonnees())

    def est_coordonnees_valides(self, coord):
        """Vérifie si les coordonnées sont valides (ex: E2)."""
        if len(coord) != 2:
            return False
        colonne, ligne = coord[0].upper(), coord[1]
        return colonne in 'ABCDEFGH' and ligne in '12345678'

    def verifier_coordonnees(self):
        """Vérifie les coordonnées et active/désactive le bouton Jouer."""
        depart = self.depart_entry.get()
        arrivee = self.arrivee_entry.get()

        if self.est_coordonnees_valides(depart) and self.est_coordonnees_valides(arrivee):
            self.jouer_button.config(state='normal')  # Activer le bouton
        else:
            self.jouer_button.config(state='disabled')  # Désactiver le bouton

    def jouer_coup(self):
        piece = self.piece_var.get()
        depart = self.depart_entry.get()
        arrivee = self.arrivee_entry.get()
        action = self.action_var.get()
        action_additionnelle = self.action_additionnelle_var.get()

        # Créer le coup de base
        coup = f"{piece} fait {action} de {depart} vers {arrivee}"

        # Ajouter l'action additionnelle si sélectionnée
        if action_additionnelle != 'Aucune':
            coup += f" ({action_additionnelle})"

        # Ajouter le coup à l'historique
        self.coups.append(coup)
        self.historique_listbox.insert(tk.END, coup)

        # Réinitialiser les champs après avoir joué le coup
        self.depart_entry.delete(0, tk.END)
        self.arrivee_entry.delete(0, tk.END)
        # Ne pas réinitialiser à une valeur par défaut
        self.verifier_coordonnees()  # Vérifier à nouveau les coordonnées

# Création de la fenêtre principale
if __name__ == "__main__":
    root = tk.Tk()
    app = HistoriqueCoupApp(root)
    root.mainloop()