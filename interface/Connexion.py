import tkinter as tk
from Menu import Menu
import global_variables as gv
from CNN.payload import loadData

class Application(tk.Frame):
    def __init__(self, master=None):
        # initialisation de la nouvelle fenêtre
        super().__init__(master)
        self.master = master
        self.pack()
        self.connex()

    def connex(self):
        # connexion aux lunettes
        self.t1 = tk.Label(self, text="Connexion à vos lunettes", justify=tk.CENTER, font=('Consolas', 20))
        self.t1.configure(fg='goldenrod', bg='#f0f0f0')
        self.b1 = tk.Button(self, text="Connexion ->", command=self.testco)
        self.b1.configure(fg='goldenrod', bg='#f0f0f0', overrelief=tk.FLAT)
        self.t1.pack(pady=20)
        self.b1.pack(pady=220)

    def suiv(self):
        # supression des widgets présents sur la fenêtre
        for widget in self.winfo_children():
            widget.pack_forget()

        gv.recordedMovements = loadData("dataset").tolist()

        Menu(self)

    def testco(self):
        # | | | | | | | | | | | | | | |
        # | | | | CODES A MODIF | | | |
        # | | | | | | | | | | | | | | |
        # V V V V V V V V V V V V V V V

        # A A A A A A A A A A A A A A A
        # | | | | | | | | | | | | | | |
        # | | | | CODES A MODIF | | | |
        # | | | | | | | | | | | | | | |
        self.suiv()
