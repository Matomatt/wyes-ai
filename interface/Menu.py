import tkinter as tk
from PIL import Image, ImageTk
from Controle import Controle
from Mouvements import Mouvements
import global_variables as gv
import TrainMouv as rm

class Menu(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.configure(bg='white')
        self.pack(fill=tk.BOTH)
        self.menupr()

    def menupr(self):
        print("taille master menu = " + str(self.master.winfo_width()) + "x" + str(self.master.winfo_height()))

        photo = ImageTk.PhotoImage(Image.open("Images/button.png").resize((460, 630), Image.ANTIALIAS))
        self.can1 = tk.Canvas(self, bg='white')
        self.b1 = tk.Button(self, text="Prendre le contrôle", image=photo, command=self.cont)
        self.item = self.can1.create_image(460, 630, image=photo)
        self.can1.image = photo
        self.b1.configure(fg='white', bg='white', overrelief=tk.FLAT, relief=tk.FLAT, compound='center',
                          font='Montserrat')

        photo2 = ImageTk.PhotoImage(Image.open("Images/button.png").resize((460, 630), Image.ANTIALIAS))
        self.can2 = tk.Canvas(self, bg='white')
        self.b2 = tk.Button(self, text="Mouvements définis", image=photo2, command=self.mouv)
        self.item2 = self.can2.create_image(460, 630, image=photo2)
        self.can2.image = photo2
        self.b2.configure(fg='white', bg='white', overrelief=tk.FLAT, relief=tk.FLAT, compound='center',
                          font='Montserrat')

        self.b1.pack(in_=self, side=tk.LEFT, padx=20, pady=10)
        self.b2.pack(in_=self, side=tk.RIGHT, padx=20, pady=10)

    def cont(self):
        # supression des widgets présents sur la fenêtre
        for widget in self.winfo_children():
            widget.pack_forget()
        Controle(self)

    def mouv(self):
        # supression des widgets présents sur la fenêtre
        for widget in self.winfo_children():
            widget.pack_forget()
        Mouvements(self)

    def trainModel(self):
        for widget in self.winfo_children():
            widget.pack_forget()
        tp = rm.TrMouv(self)
        tp.newmouv()
