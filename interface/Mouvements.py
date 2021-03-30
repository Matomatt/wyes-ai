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
        print("taille master mouvements = " + str(self.master.winfo_width()) + "x" + str(self.master.winfo_height()))
        # configuration du Header
        self.t1 = tk.Label(self)
        self.br = tk.Button(self, text="<---", command=self.retour)
        self.br.configure(fg='lightgray', bg='#008080')
        self.br.pack(padx=10, pady=10)
        self.br.place(x=0, y=0)
        self.t1.pack(side=tk.TOP)

        self.mouvementButtons = []
        nbMov = len(gv.recordedMovements) if len(gv.recordedMovements)>3 else 3
        for i in range(nbMov):
            self.mouvementButtons.append( tk.Button(self, text="Mouvement "+str(i+1), width=int((self.master.winfo_width()/10-nbMov-1)/nbMov), height=45, command=lambda index=i: self.buildMovementDataset(index)))
            self.mouvementButtons[i].configure(fg='white', bg='#008080', activebackground='#009999', overrelief=tk.FLAT, relief=tk.FLAT)
            self.mouvementButtons[i].pack(in_=self, side=tk.LEFT, padx=10, pady=10)

        # bouton ajouter mouvement
        self.addMovementButton = tk.Button(self, text="+", width=int((self.master.winfo_width()/10-nbMov-1)/nbMov), height=45, command=self.addMovement)
        self.addMovementButton.configure(fg='white', bg='#969696', activebackground='#009999', overrelief=tk.FLAT, relief=tk.FLAT, font='Consolas 10 bold')
        self.addMovementButton.pack(in_=self, side=tk.RIGHT, padx=10, pady=10)

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
            mouv.configure(width=int((self.master.winfo_width()/10-newIndex-1)/newIndex))
        button = tk.Button(self, text="Mouvement "+str(newIndex+1), width=int((self.master.winfo_width()/10-newIndex-1)/newIndex), height=45, command=lambda index=newIndex: self.buildMovementDataset(index))
        self.mouvementButtons.append(button)
        self.mouvementButtons[newIndex].configure(fg='white', bg='#008080', activebackground='#009999', overrelief=tk.FLAT, relief=tk.FLAT)
        self.mouvementButtons[newIndex].pack(in_=self, side=tk.LEFT, padx=10, pady=10)

