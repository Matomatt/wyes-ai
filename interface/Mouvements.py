import tkinter as tk
import Menu as mn
import RegisterMouv as rm
from RegisterMouv import Regis
import global_variables as gv


class Mouvements(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.init()
        self.pack()


    def init(self):
        # configuration du Header
        self.t1 = tk.Label(self, text="Fenêtre des mouvements", justify=tk.CENTER, font=('Consolas', 20))
        self.t1.configure(fg='goldenrod', bg='#f0f0f0')
        self.returnButton = tk.Button(self, text="<- Retour", command=self.retour, width=int(self.winfo_width()*3/10))
        self.returnButton.configure(fg='lightgray', bg='#008080')
        self.addMovementButton = tk.Button(self, text="Ajouter un mouvement", command=self.addMovement)
        self.addMovementButton.configure(fg='lightgray', bg='#008080')

        self.t1.pack(side=tk.TOP)
        self.returnButton.pack(side=tk.TOP)
        self.addMovementButton.pack(side=tk.TOP)

        self.mouvementButtons = []
        nbMov = len(gv.recordedMovements) if len(gv.recordedMovements)>3 else 3
        for i in range(nbMov):
            self.mouvementButtons.append( tk.Button(self, text="Mouvement "+str(i+1), width=int((100-nbMov-1)/nbMov), height=45, command=lambda index=i: self.buildMovementDataset(index)))
            self.mouvementButtons[i].configure(fg='white', bg='#969696', activebackground='#009999', overrelief=tk.FLAT, relief=tk.FLAT)
            self.mouvementButtons[i].pack(in_=self, side=tk.LEFT, padx=10, pady=10)

    def retour(self):
        # supression des widgets présents sur la fenêtre
        for widget in self.winfo_children():
            widget.pack_forget()
        mn.Menu(self)

    def buildMovementDataset(self, movementIndex):
        # supression des widgets présents sur la fenêtre
        for widget in self.winfo_children():
            widget.pack_forget()
        tp = rm.Regis(self)
        tp.init(movementIndex, 10)

    def addMovement(self):
        newIndex = len(self.mouvementButtons)
        for mouv in self.mouvementButtons:
            mouv.configure(width=int((100-newIndex-1)/newIndex))
        button = tk.Button(self, text="Mouvement "+str(newIndex+1), width=int(100/newIndex), height=45, command=lambda index=newIndex: self.buildMovementDataset(index))
        self.mouvementButtons.append(button)
        self.mouvementButtons[newIndex].configure(fg='white', bg='#969696', activebackground='#009999', overrelief=tk.FLAT, relief=tk.FLAT)
        self.mouvementButtons[newIndex].pack(in_=self, side=tk.LEFT, padx=10, pady=10)

