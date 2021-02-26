import tkinter as tk
from Connexion import Application


def main(root):
    # apparence fenêtre
    root.configure(bg='#f0f0f0')
    root.geometry("800x550")
    root.wm_iconbitmap("Images/icone.ico")

    # objets fenêtre
    t1 = tk.Label(root, text="Bienvenue sur votre logiciel de contrôle", justify=tk.CENTER, font=('Consolas', 25))
    t1.configure(fg='goldenrod', bg='#f0f0f0')
    t2 = tk.Label(root, text="Cliquez sur n'importe quelle touche pour continuer", justify=tk.CENTER)
    t2.configure(fg='goldenrod', bg='#f0f0f0', font='Consolas')
    t1.pack(pady=120)
    t2.pack()

    # fonctionnalités fenêtre
    root.bind('<Key>', touche)

def touche(event):
    # supression des widgets présents sur la fenêtre
    for widget in root.winfo_children():
        widget.pack_forget()
    Application(root)

if __name__ == '__main__':
    root = tk.Tk(className='When your eyes speak')
    main(root)
    root.mainloop()