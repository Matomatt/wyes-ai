import tkinter as tk
from tkinter import ttk
import Menu
import Mouvements as mn
import time


class TrMouv(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.essai = 0
        self.nummouv = 0
        self.statut = True
        self.pack()

    def newmouv(self):
        if self.essai!=10:
            # supression des widgets présents sur la fenêtre
            for widget in self.winfo_children():
                widget.pack_forget()
            # configuration du Header
            self.t1 = tk.Label(self, text="Training du mouvement " + str(self.nummouv), justify=tk.CENTER, font=('Consolas', 20))
            self.t1.configure(fg='goldenrod', bg='#f0f0f0')
            self.br = tk.Button(self, text="<- Retour", command=self.retour)
            self.br.configure(fg='lightgray', bg='#008080')
            self.t1.pack(side=tk.TOP)
            self.br.pack(side=tk.TOP)

            self.bagain = tk.Button(self, text="Supprimer le mouvement", command=self.menu)
            self.bagain.configure(fg='lightgray', bg='#b30000')
            self.bagain.pack(side=tk.BOTTOM, pady=120)

            if self.statut==True:
                self.btrain = tk.Button(self, text="Training", command=self.training)
                self.btrain.configure(fg='lightgray', bg='#2d8659')
            self.btrain.pack(side=tk.TOP, pady=20)


    def retour(self):
        # supression des widgets présents sur la fenêtre
        for widget in self.winfo_children():
            widget.pack_forget()
        mn.Mouvements(self)

    def menu(self):
        # supression des widgets présents sur la fenêtre
        for widget in self.winfo_children():
            widget.pack_forget()
        Menu.Menu(self)


    def quelmouv(self, idid):
        self.nummouv = idid

    def training(self):
        if self.statut == True:
            self.statut = False
            self.progress = ttk.Progressbar(self, orient="horizontal",
                                            length=240, mode="determinate")
            self.progress.pack()
            self.progress.start()

            for i in range(12):
                self.progress["value"] = i * 9
                self.update()
                time.sleep(0.1)
                if i == 11:
                    self.statut = True
            self.progress.stop()

        # Appel pour lancer un essai
        # | | | | | | | | | | | | | | |
        # | | | | CODES A MODIF | | | |
        # | | | | | | | | | | | | | | |
        # V V V V V V V V V V V V V V V

        # A A A A A A A A A A A A A A A
        # | | | | | | | | | | | | | | |
        # | | | | CODES A MODIF | | | |
        # | | | | | | | | | | | | | | |
        self.newmouv()

