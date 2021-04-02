import tkinter as tk
from PIL import Image, ImageTk
import Menu as mn
import RegisterMouv as rm
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
        self.height = int(self.master.winfo_height())
        self.width = int(self.master.winfo_width())
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

        self.mouvementButtons = []
        self.can = []
        self.items = []
        nbMov = len(gv.recordedMovements) if len(gv.recordedMovements)>3 else 3
        button = ImageTk.PhotoImage(Image.open("Images/button.png").resize((int(950/4), 600), Image.ANTIALIAS))
        for i in range(nbMov):
            self.can.append(tk.Canvas(self, bg='#f0f0f0'))
            self.mouvementButtons.append(tk.Button(self, text="Mouvement "+str(i+1), image=button, command=lambda index=i: self.buildMovementDataset(index)))
            self.items.append(self.can[i].create_image((950/4), 600, image=button))
            self.can[i].image = button
            self.mouvementButtons[i].configure(fg='white', bg='#f0f0f0', overrelief=tk.FLAT, relief=tk.FLAT, compound="center", font='Montserrat')
            self.mouvementButtons[i].pack(in_=self, side=tk.LEFT, padx=5, pady=5)

        # bouton ajouter mouvement
        self.can2 = tk.Canvas(self, bg='#f0f0f0')
        photoplus = ImageTk.PhotoImage(Image.open("Images/plus.png").resize(
            (150, 600), Image.ANTIALIAS))
        self.addMovementButton = tk.Button(self, text="+", image=photoplus, command=self.addMovement)
        self.item2 = self.can2.create_image(150, 600, image=photoplus)
        self.can2.image = photoplus
        self.addMovementButton.configure(fg='white', bg='#f0f0f0', overrelief=tk.FLAT, relief=tk.FLAT, font='Montserrat 10 bold')
        self.addMovementButton.pack(in_=self, side=tk.RIGHT, padx=5, pady=5)

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
        for mouvBut in self.mouvementButtons:
            mouvBut.pack_forget()
        newIndex = len(self.mouvementButtons)
        imbutton = ImageTk.PhotoImage(Image.open("Images/button.png").resize(
            (int(950/(newIndex+2)-10), 600), Image.ANTIALIAS))
        for i in range(newIndex):
            self.can[i] = tk.Canvas(self, bg='#f0f0f0')
            self.mouvementButtons[i] = tk.Button(self, text="Mouvement " + str(i + 1), image=imbutton,
                                                   command=lambda index=i: self.buildMovementDataset(index))
            self.items[i] = self.can[i].create_image(int(950/(newIndex+1)), 600, image=imbutton)
            self.can[i].image = imbutton
            self.mouvementButtons[i].configure(fg='white', bg='#f0f0f0', overrelief=tk.FLAT, relief=tk.FLAT,
                                               compound="center", font='Montserrat')
            if newIndex>4:
                self.mouvementButtons[i].configure(font="Montserrat "+str(20-2*newIndex))
            self.mouvementButtons[i].pack(in_=self, side=tk.LEFT, padx=5, pady=5)

        self.can.append(tk.Canvas(self, bg='#f0f0f0'))
        self.mouvementButtons.append(tk.Button(self, text="Mouvement " + str(newIndex + 1), image=imbutton,
                                               command=lambda index=i: self.buildMovementDataset(index)))
        self.items.append(self.can[newIndex].create_image(int(950/(newIndex+1)), 600, image=imbutton))
        self.can[newIndex].image = imbutton
        self.mouvementButtons[newIndex].configure(fg='white', bg='#f0f0f0', overrelief=tk.FLAT, relief=tk.FLAT,
                                           compound="center", font='Montserrat')
        if newIndex>4:
            self.mouvementButtons[newIndex].configure(font="Montserrat "+str(20-2*newIndex))
        self.mouvementButtons[newIndex].pack(in_=self, side=tk.LEFT, padx=5, pady=5)



