import tkinter as tk

root = tk.Tk()
root.title("Ma Première Interface Tkinter")

label = tk.Label(root, text="Bonjour, Tkinter!")
label.pack()

button = tk.Button(root, text="Clique moi", command=root.destroy)
button.pack()

root.mainloop()


