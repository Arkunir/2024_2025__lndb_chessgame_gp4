import tkinter as tk
from tkinter import messagebox

class Timer:
    def __init__(self, root):
        self.root = root
        self.root.title("Minuteur de Jeu d'Échecs avec Cadences")

        self.time_player_1 = 0
        self.time_player_2 = 0
        self.bonus_player_1 = 0
        self.bonus_player_2 = 0
        self.is_running = False
        self.current_player = 1  # Joueur 1 commence
        self.timer_active = None
        self.is_paused = False  # Variable pour gérer la pause

        # Affichage du temps restant pour chaque joueur
        self.label_player_1 = tk.Label(root, text="00:00", font=("Helvetica", 30), width=10)
        self.label_player_1.pack(side=tk.LEFT, padx=20)

        self.label_player_2 = tk.Label(root, text="00:00", font=("Helvetica", 30), width=10)
        self.label_player_2.pack(side=tk.RIGHT, padx=20)

        # Menu déroulant pour choisir la cadence
        self.cadence_var = tk.StringVar(value="3/2")  # Valeur par défaut
        self.cadence_menu = tk.OptionMenu(root, self.cadence_var, "2/1", "3/2", "5/2", "10/0", "15/5")
        self.cadence_menu.pack(pady=10)

        # Boutons pour démarrer et changer de joueur
        self.start_button = tk.Button(root, text="Démarrer", font=("Helvetica", 15), command=self.start)
        self.start_button.pack(pady=10)

        self.switch_button = tk.Button(root, text="Passer au joueur suivant", font=("Helvetica", 15), command=self.switch_player)
        self.switch_button.pack(pady=10)

        # Bouton Pause/Arrêt
        self.pause_button = tk.Button(root, text="Pause", font=("Helvetica", 15), command=self.toggle_pause)
        self.pause_button.pack(pady=10)

        # Bouton Réinitialiser
        self.reset_button = tk.Button(root, text="Réinitialiser", font=("Helvetica", 15), command=self.reset)
        self.reset_button.pack(pady=10)

    def start(self):
        """Démarre ou relance le minuteur en fonction de la cadence choisie."""
        if not self.is_running:
            cadence = self.cadence_var.get()

            if cadence == "2/1":
                self.time_player_1 = 120  # 2 minutes en secondes
                self.time_player_2 = 120  # 2 minutes en secondes
                self.bonus_player_1 = 1   # 1 seconde par coup
                self.bonus_player_2 = 1   # 1 seconde par coup
            elif cadence == "3/2":
                self.time_player_1 = 180  # 3 minutes en secondes
                self.time_player_2 = 180  # 3 minutes en secondes
                self.bonus_player_1 = 2   # 2 secondes par coup
                self.bonus_player_2 = 2   # 2 secondes par coup
            elif cadence == "5/2":
                self.time_player_1 = 300  # 5 minutes en secondes
                self.time_player_2 = 300  # 5 minutes en secondes
                self.bonus_player_1 = 2   # 2 secondes par coup
                self.bonus_player_2 = 2   # 2 secondes par coup
            elif cadence == "10/0":
                self.time_player_1 = 600  # 10 minutes en secondes
                self.time_player_2 = 600  # 10 minutes en secondes
                self.bonus_player_1 = 0   # Aucun bonus par coup
                self.bonus_player_2 = 0   # Aucun bonus par coup
            elif cadence == "15/5":
                self.time_player_1 = 900  # 15 minutes en secondes
                self.time_player_2 = 900  # 15 minutes en secondes
                self.bonus_player_1 = 5   # 5 secondes par coup
                self.bonus_player_2 = 5   # 5 secondes par coup

            self.is_running = True
            self.update_time()
            self.start_button.config(state=tk.DISABLED)
            self.switch_button.config(state=tk.NORMAL)

    def switch_player(self):
        """Change de joueur et ajoute le bonus au temps du joueur courant."""
        if self.is_running and not self.is_paused:
            if self.current_player == 1:
                self.time_player_1 += self.bonus_player_1  # Ajoute le bonus à joueur 1
                self.current_player = 2
            else:
                self.time_player_2 += self.bonus_player_2  # Ajoute le bonus à joueur 2
                self.current_player = 1

            # Actualisation des labels des joueurs
            self.update_display()

    def update_time(self):
        """Met à jour le temps restant pour le joueur actif."""
        if self.is_running and not self.is_paused:
            if self.current_player == 1 and self.time_player_1 > 0:
                self.time_player_1 -= 1
                self.update_display()
            elif self.current_player == 2 and self.time_player_2 > 0:
                self.time_player_2 -= 1
                self.update_display()
            
            # Vérifie si le temps d'un joueur est écoulé
            if self.time_player_1 <= 0 or self.time_player_2 <= 0:
                self.is_running = False
                self.start_button.config(state=tk.NORMAL)
                self.switch_button.config(state=tk.DISABLED)
                winner = "Joueur 2" if self.time_player_1 <= 0 else "Joueur 1"
                messagebox.showinfo("Temps écoulé", f"{winner} a gagné !")
            else:
                # Continue à mettre à jour le temps chaque seconde
                self.root.after(1000, self.update_time)  # 1000 ms = 1 seconde

    def update_display(self):
        """Met à jour les labels pour afficher le temps restant."""
        minutes_1 = self.time_player_1 // 60
        seconds_1 = self.time_player_1 % 60
        self.label_player_1.config(text=f"{minutes_1:02}:{seconds_1:02}")

        minutes_2 = self.time_player_2 // 60
        seconds_2 = self.time_player_2 % 60
        self.label_player_2.config(text=f"{minutes_2:02}:{seconds_2:02}")

    def toggle_pause(self):
        """Alterne entre pause et reprendre le jeu."""
        if self.is_running:
            if self.is_paused:
                # Reprendre le jeu
                self.is_paused = False
                self.pause_button.config(text="Pause")
                self.update_time()  # Reprend le décompte du temps
            else:
                # Mettre le jeu en pause
                self.is_paused = True
                self.pause_button.config(text="Reprendre")

    def reset(self):
        """Réinitialise le jeu, remet les temps et réinitialise les variables."""
        # Réinitialiser les variables
        self.time_player_1 = 0
        self.time_player_2 = 0
        self.bonus_player_1 = 0
        self.bonus_player_2 = 0
        self.is_running = False
        self.current_player = 1
        self.is_paused = False

        # Réinitialiser les labels
        self.update_display()

        # Réinitialiser le menu déroulant
        self.cadence_var.set("3/2")  # Valeur par défaut

        # Remettre les boutons à leur état initial
        self.start_button.config(state=tk.NORMAL)
        self.switch_button.config(state=tk.DISABLED)
        self.pause_button.config(text="Pause")
        
      

# Création de la fenêtre principale
root = tk.Tk()
timer = Timer(root)

# Démarrage de l'interface graphique
root.mainloop()
