import tkinter as tk
from Connexion import Application


def main(root):
    # apparence fenêtre
    root.configure(bg='#f0f0f0')
    root.geometry("1000x650")
    # root.wm_iconbitmap("Images/icone.ico")

    # objets fenêtre
    root.update()
    print("taille master start = " + str(root.winfo_width()) + "x" + str(root.winfo_height()))
    t1 = tk.Label(root, text="Bienvenue sur votre logiciel de contrôle", justify=tk.CENTER, font=('Montserrat', 25))
    t1.configure(fg='goldenrod', bg='#f0f0f0')
    t2 = tk.Label(root, text="Cliquez sur n'importe quelle touche pour continuer", justify=tk.CENTER)
    t2.configure(fg='goldenrod', bg='#f0f0f0', font='Montserrat')
    t1.pack(pady=120)
    t2.pack()

    # affichages logos
    root.can1 = tk.Canvas(root, bg='#f0f0f0')
    wyes = tk.PhotoImage(file='Images/wyes.png')
    root.item = root.can1.create_image(100, 100, image=wyes)
    root.can1.image = wyes
    root.can1.pack()
    root.can1.place(x=200, y=400)

    root.can2 = tk.Canvas(root, bg='#f0f0f0')
    ece = tk.PhotoImage(file='Images/ece.png')
    root.item2 = root.can2.create_image(150, 100, image=ece)
    root.can2.image = ece
    root.can2.pack()
    root.can2.place(x=460, y=390)

    # fonctionnalités fenêtre
    root.bind('<Key>', touche)
    root.bind('<Button-1>', touche)
    root.bind('<Button-2>', touche)

def touche(event):
    root.unbind('<Key>')
    root.unbind('<Button-1>')
    root.unbind('<Button-2>')
    # supression des widgets présents sur la fenêtre
    root.can1.delete(root.item)
    root.can2.delete(root.item2)
    for widget in root.winfo_children():
        widget.pack_forget()
    Application(root)

if __name__ == '__main__':
    root = tk.Tk(className='When your eyes speak')
    main(root)
    root.mainloop()
