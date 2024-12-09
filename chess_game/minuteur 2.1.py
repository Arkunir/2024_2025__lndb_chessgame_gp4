import tkinter as tk
from tkinter import messagebox

class Timer:
    def __init__(self, root):
        self.root = root
        self.root.title("Minuteur de Jeu d'Échecs ")

        self.time_player_1 = 0
        self.time_player_2 = 0
        self.bonus_player_1 = 0
        self.bonus_player_2 = 0
        self.is_running = False
        self.current_player = 1  
        self.timer_active = None
        self.is_paused = False  

        self.label_player_1 = tk.Label(root, text="00:00", font=("Helvetica", 30), width=10)
        self.label_player_1.pack(side=tk.LEFT, padx=20)

        self.label_player_2 = tk.Label(root, text="00:00", font=("Helvetica", 30), width=10)
        self.label_player_2.pack(side=tk.RIGHT, padx=20)

        self.cadence_var = tk.StringVar(value="3/2")  
        self.cadence_menu = tk.OptionMenu(root, self.cadence_var, "2/1", "3/2", "5/2", "10/0", "15/5")
        self.cadence_menu.pack(pady=10)
        
        self.cadence_var.trace("w", self.on_cadence_change)

      
        self.start_button = tk.Button(root, text="Démarrer", font=("Helvetica", 15), command=self.start)
        self.start_button.pack(pady=10)

        self.switch_button = tk.Button(root, text="Passer au joueur suivant", font=("Helvetica", 15), command=self.switch_player)
        self.switch_button.pack(pady=10)

        self.pause_button = tk.Button(root, text="Pause", font=("Helvetica", 15), command=self.toggle_pause)
        self.pause_button.pack(pady=10)

        self.reset_button = tk.Button(root, text="Réinitialiser", font=("Helvetica", 15), command=self.reset)
        self.reset_button.pack(pady=10)

    def on_cadence_change(self, *args):
        """Réinitialise le temps des joueurs si la cadence change pendant la partie."""
        if self.is_running:
            self.time_player_1 = 0
            self.time_player_2 = 0
            self.update_display()

    def start(self):
        """Démarre ou relance le minuteur en fonction de la cadence choisie."""
        if not self.is_running:
            cadence = self.cadence_var.get()

            if cadence == "2/1":
                self.time_player_1 = 120  
                self.time_player_2 = 120  
                self.bonus_player_1 = 1   
                self.bonus_player_2 = 1   
            elif cadence == "3/2":
                self.time_player_1 = 180 
                self.time_player_2 = 180  
                self.bonus_player_1 = 2   
                self.bonus_player_2 = 2  
            elif cadence == "5/2":
                self.time_player_1 = 300  
                self.time_player_2 = 300  
                self.bonus_player_1 = 2   
                self.bonus_player_2 = 2   
            elif cadence == "10/0":
                self.time_player_1 = 600  
                self.time_player_2 = 600  
                self.bonus_player_1 = 0   
                self.bonus_player_2 = 0   
            elif cadence == "15/5":
                self.time_player_1 = 900  
                self.time_player_2 = 900  
                self.bonus_player_1 = 5   
                self.bonus_player_2 = 5  

            self.is_running = True
            self.update_time()
            self.start_button.config(state=tk.DISABLED)
            self.switch_button.config(state=tk.NORMAL)

    def switch_player(self):
        """Change de joueur et ajoute le bonus au temps du joueur courant."""
        if self.is_running and not self.is_paused:
            if self.current_player == 1:
                self.time_player_1 += self.bonus_player_1  
                self.current_player = 2
            else:
                self.time_player_2 += self.bonus_player_2  
                self.current_player = 1

            
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
            
           
            if self.time_player_1 <= 0 or self.time_player_2 <= 0:
                self.is_running = False
                self.start_button.config(state=tk.NORMAL)
                self.switch_button.config(state=tk.DISABLED)
                winner = "Joueur 2" if self.time_player_1 <= 0 else "Joueur 1"
            else:
                self.root.after(1000, self.update_time)  

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
                self.is_paused = False
                self.pause_button.config(text="Pause")
                self.update_time()  
            else:
                self.is_paused = True
                self.pause_button.config(text="Reprendre")

    def reset(self):
        """Réinitialise le jeu, remet les temps et réinitialise les variables."""
        self.time_player_1 = 0
        self.time_player_2 = 0
        self.bonus_player_1 = 0
        self.bonus_player_2 = 0
        self.is_running = False
        self.current_player = 1
        self.is_paused = False

        self.update_display()

        self.cadence_var.set("3/2") 

        self.start_button.config(state=tk.NORMAL)
        self.switch_button.config(state=tk.DISABLED)
        self.pause_button.config(text="Pause")
        

root = tk.Tk()
timer = Timer(root)

root.mainloop()
