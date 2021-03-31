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
        self.pack(fill=tk.BOTH)


    def init(self):
        # supression des widgets présents sur la fenêtre
        for widget in self.winfo_children():
            widget.pack_forget()
        print("taille master mouvements = " + str(self.master.winfo_width()) + "x" + str(self.master.winfo_height()))
        # configuration du Header
        self.t1 = tk.Label(self)
        self.can1 = tk.Canvas(self, bg='#f0f0f0')
        photo = tk.PhotoImage(file=r"Images/return.png", master=self)
        self.br = tk.Button(self, text="<---", image=photo, command=self.retour, overrelief=tk.FLAT, relief=tk.FLAT)
        self.item = self.can1.create_image(40, 20, image=photo)
        self.can1.image = photo
        self.br.pack(padx=10, pady=10)
        self.br.place(x=0, y=0)
        self.t1.pack(side=tk.TOP)

        button = tk.PhotoImage(file="Images/button.png")
        self.mouvementButtons = []
        self.can = []
        self.items = []
        nbMov = len(gv.recordedMovements) if len(gv.recordedMovements)>3 else 3
        for i in range(nbMov):
            self.can.append(tk.Canvas(self, bg='#f0f0f0'))
            self.mouvementButtons.append(tk.Button(self, text="Mouvement "+str(i+1), image=button, command=lambda index=i: self.buildMovementDataset(index)))
            self.items.append(self.can[i].create_image(int((self.master.winfo_width()/10-nbMov-1)/nbMov), 45, image=button))
            self.can[i].image = button
            self.mouvementButtons[i].configure(fg='white', bg='#f0f0f0', overrelief=tk.FLAT, relief=tk.FLAT, compound="center")
            self.mouvementButtons[i].pack(in_=self, side=tk.LEFT, padx=10, pady=10)

        # bouton ajouter mouvement
        self.can2 = tk.Canvas(self, bg='#f0f0f0')
        photoplus = tk.PhotoImage(file=r"Images/plus.png", master=self)
        self.addMovementButton = tk.Button(self, text="+", image=photoplus, command=self.addMovement)
        self.item2 = self.can2.create_image(int((self.master.winfo_width()/10-nbMov-1)/nbMov), 48, image=photoplus)
        self.can2.image = photoplus
        self.addMovementButton.configure(fg='white', bg='#f0f0f0', overrelief=tk.FLAT, relief=tk.FLAT, font='Consolas 10 bold')
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
        imbutton = tk.PhotoImage(file="Images/button.png")
        newIndex = len(self.mouvementButtons)
        for mouv in self.can:
            mouv.create_image(int((self.master.winfo_width()/10-newIndex-1)/newIndex), 45, image=imbutton)
        self.can.append(tk.Canvas(self, bg='#f0f0f0'))
        button = tk.Button(self, text="Mouvement "+str(newIndex+1), image=imbutton, command=lambda index=newIndex: self.buildMovementDataset(index))
        self.mouvementButtons.append(button)
        self.items.append(
            self.can[newIndex].create_image(int((self.master.winfo_width()/10-newIndex-1)/newIndex), 45, image=imbutton))
        self.can[newIndex].image = imbutton
        self.mouvementButtons[newIndex].configure(fg='white', bg='#f0f0f0', overrelief=tk.FLAT, relief=tk.FLAT, compound="center")
        self.mouvementButtons[newIndex].pack(in_=self, side=tk.LEFT, padx=10, pady=10)

