import tkinter as tk
from Controle import Controle
from Mouvements import Mouvements
from MouvTraining import MouvTraining
import global_variables as gv
import TrainMouv as rm

class Menu(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.menupr()

    def menupr(self):
        self.t1 = tk.Label(self, text="Bienvenue sur le menu", justify=tk.CENTER, font=('Consolas', 20))
        self.t1.configure(fg='goldenrod', bg='#f0f0f0')
        self.t1.pack(pady=20)

        #if(Mouvements.nbMouv(self)==3):
        self.b1 = tk.Button(self, text="Prendre le contrôle", width=int((self.master.winfo_width()/10)), height=45, command=self.cont)
        self.b1.configure(fg='white', bg='#008080', activebackground='#009999', overrelief=tk.FLAT, relief=tk.FLAT)
        # else:
        #     self.b1 = tk.Button(self, text="Prendre les contrôle", width=33, height=45)
        #     self.b1.configure(fg='white', bg='#969696', overrelief=tk.FLAT, relief=tk.FLAT, cursor='X_cursor')
        self.b2 = tk.Button(self, text="Mouvements définis", width=int((self.master.winfo_width()/10)), height=45, command=self.mouv)
        self.b2.configure(fg='white', bg='#008080', activebackground='#009999', overrelief=tk.FLAT, relief=tk.FLAT)
        self.b3 = tk.Button(self, text="Training", width=int((self.master.winfo_width()/10)), height=45, command=self.trainModel)
        self.b3.configure(fg='white', bg='#008080', activebackground='#009999', overrelief=tk.FLAT, relief=tk.FLAT)
        self.b1.pack(in_=self, side=tk.LEFT, padx=10, pady=10)
        self.b2.pack(in_=self, side=tk.LEFT, padx=10, pady=10)
        self.b3.pack(in_=self, side=tk.LEFT, padx=10, pady=10)

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
