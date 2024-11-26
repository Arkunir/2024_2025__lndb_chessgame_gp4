import tkinter as tk
import time

class Chronometre:
    def __init__(self, root):
        self.root = root
        self.root.title("Chronomètre")
        
        self.is_running = False
        self.time_elapsed = 0.0
        
        self.label = tk.Label(root, text="0.0", font=("Helvetica", 30), width=10)
        self.label.pack()

        self.start_button = tk.Button(root, text="Démarrer", font=("Helvetica", 15), command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.stop_button = tk.Button(root, text="Arrêter", font=("Helvetica", 15), command=self.stop)
        self.stop_button.pack(side=tk.LEFT, padx=10)

        self.reset_button = tk.Button(root, text="Réinitialiser", font=("Helvetica", 15), command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=10)

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.update_time()
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)

    def stop(self):
        self.is_running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def reset(self):
        self.is_running = False
        self.time_elapsed = 0.0
        self.label.config(text=f"{self.time_elapsed:.1f}")
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

    def update_time(self):
        if self.is_running:
            self.time_elapsed += 0.1
            self.label.config(text=f"{self.time_elapsed:.1f}")
            self.root.after(100, self.update_time)  # Met à jour toutes les 100ms

# Création de la fenêtre principale
root = tk.Tk()
chronometre = Chronometre(root)

# Démarrage de l'interface graphique
root.mainloop()
