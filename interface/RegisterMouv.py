import tkinter as tk
from tkinter import ttk
import Mouvements as mn
import time
import live_emulation as le
import global_variables as gv


class Regis(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.t1 = tk.Label(self)
        self.br = tk.Button(self)
        self.bregis = tk.Button(self)
        self.deleteLastMovementButton = tk.Button(self)
        self.pack(fill=tk.BOTH)

    def init(self, movementIndex, desiredNumberOfEssai):
        # supression des widgets présents sur la fenêtre
        for widget in self.winfo_children():
            widget.pack_forget()
        print("taille master register mouvement = " + str(self.master.winfo_width()) + "x" + str(self.master.winfo_height()))
        self.movementIndex = movementIndex
        self.desiredNumberOfEssai = desiredNumberOfEssai
        while (len(gv.recordedMovements) < movementIndex+1):
            gv.recordedMovements.append([])

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

        self.bregis.configure(text="Nouvel essai", command=self.progression, relief=tk.FLAT, bg='#196619', fg='white')
        self.bregis.pack(pady=20)
        self.bregis.place(x=int((self.master.winfo_width()/3.5)), y=50)

        self.can2 = tk.Canvas(self, bg='#f0f0f0')
        photoagain = tk.PhotoImage(file=r"Images/again.png", master=self)
        self.deleteLastMovementButton.configure(fg='lightgray', bg='#f0f0f0', text="Annuler", image=photoagain, command=self.deleteLast, relief=tk.FLAT)
        self.item2 = self.can2.create_image(20, 20, image=photoagain)
        self.can2.image = photoagain
        self.deleteLastMovementButton.pack(pady=60)
        self.deleteLastMovementButton.place(x=int((self.master.winfo_width()/2.5)), y=50)

        self.can3 = tk.Canvas(self, bg='#f0f0f0')
        photostop = tk.PhotoImage(file=r"Images/annuler.png", master=self)
        self.bagain = tk.Button(self, text="X", image=photostop, command=self.recommencer, relief=tk.FLAT, font='Consolas 22 bold', fg='white')
        self.item3 = self.can2.create_image(50, 50, image=photostop)
        self.can3.image = photostop
        self.bagain.configure(fg='lightgray', bg='#f0f0f0')
        self.bagain.pack(side=tk.BOTTOM, pady=10)

        self.lf = tk.Label(self, text="", justify=tk.CENTER, font=('Consolas', 10))
        self.lf.pack(side=tk.BOTTOM, pady=30)

        self.essaiButtons = []
        nbEssai = len(gv.recordedMovements[movementIndex])+1 if len(gv.recordedMovements[movementIndex])>=desiredNumberOfEssai else desiredNumberOfEssai
        for i in range(nbEssai):
            self.addEssaiButton(i)
            if (i<len(gv.recordedMovements[movementIndex])):
               self.essaiButtons[i].configure(fg='black', bg='#009933', width=int(self.master.winfo_width()/(10*nbEssai)))
            elif (i==len(gv.recordedMovements[movementIndex])):
                self.essaiButtons[i].configure(fg='black', bg='#d9d9d9', width=int(self.master.winfo_width()/(10*nbEssai)))

    def addEssaiButton(self, index):
        if self.movementIndex < 10:
            nbEssai = 10
        else:
            nbEssai = self.movementIndex
        l = tk.Label(self, text=str(index+1), justify=tk.CENTER, font=('Consolas', 10))
        l.configure(fg='black', bg='#b3b3b3', width=10)
        l.pack(side=tk.LEFT, pady=60)
        self.essaiButtons.append(l)

    def retour(self):
        # supression des widgets présents sur la fenêtre
        for widget in self.winfo_children():
            widget.pack_forget()
        mn.Mouvements(self)

    def recommencer(self):
        gv.recordedMovements[self.movementIndex] = []
        self.init(self.movementIndex, self.desiredNumberOfEssai)

    def deleteLast(self):
        if (len(gv.recordedMovements[self.movementIndex]) == 0): return
        gv.recordedMovements[self.movementIndex] = gv.recordedMovements[self.movementIndex][:-1]
        self.init(self.movementIndex, self.desiredNumberOfEssai)

    def progression(self):
        newMovement = le.start()
        if (newMovement != None):
            self.essaiButtons[len(gv.recordedMovements[self.movementIndex])].configure(fg='black', bg='#009933')

            gv.recordedMovements[self.movementIndex].append(newMovement)

            if (len(gv.recordedMovements[self.movementIndex])>=len(self.essaiButtons)):
                self.addEssaiButton(len(self.essaiButtons))

            self.essaiButtons[len(gv.recordedMovements[self.movementIndex])].configure(fg='black', bg='#d9d9d9')
            #self.bregis.configure(text="Nouvel essai : " + str(len(gv.recordedMovements[self.movementIndex])) + "/" +str(self.desiredNumberOfEssai))

            if len(gv.recordedMovements[self.movementIndex])>=self.desiredNumberOfEssai:
                print("finito")
                self.lf.configure(text = "Les 10 essais nécessaires ont été fait\nMais vous pouvez continuer à entrainer l'IA")

        else:
            print("QUITTING")
            #QUIT
