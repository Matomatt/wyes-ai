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
        #self.ff = tk.Frame(self)
        self.pack()

    def init(self, movementIndex, desiredNumberOfEssai):
        self.movementIndex = movementIndex
        self.desiredNumberOfEssai = desiredNumberOfEssai
        while (len(gv.recordedMovements) < movementIndex+1):
            gv.recordedMovements.append([])

        # supression des widgets présents sur la fenêtre
        for widget in self.winfo_children():
            widget.pack_forget()

        # configuration du Header
        self.t1 = tk.Label(self, text="Enregistrement du mouvement " + str(movementIndex+1), justify=tk.CENTER, font=('Consolas', 20))
        self.t1.configure(fg='goldenrod', bg='#f0f0f0')
        self.br = tk.Button(self, text="<- Retour", command=self.retour)
        self.br.configure(fg='lightgray', bg='#008080')
        self.t1.pack(side=tk.TOP)
        self.br.pack(side=tk.TOP)

        self.bregis = tk.Button(self, text="Nouvel essai : " + str(len(gv.recordedMovements[self.movementIndex])) + "/" + str(desiredNumberOfEssai), command=self.progression)
        self.bregis.pack(side=tk.TOP, pady=20)

        le = tk.Label(self, text="Essai :", justify=tk.LEFT, font=('Consolas', 10))
        le.place(x=0, y=110)

        self.bagain = tk.Button(self, text="Recommencer ou supprimer le mouvement", command=self.recommencer)
        self.bagain.configure(fg='lightgray', bg='#b30000')
        self.bagain.pack(side=tk.BOTTOM, pady=120)

        self.essaiButtons = []
        nbEssai = len(gv.recordedMovements[movementIndex])+1 if len(gv.recordedMovements[movementIndex])>=desiredNumberOfEssai else desiredNumberOfEssai
        for i in range(nbEssai):
            self.addEssaiButton(i)
            if (i<len(gv.recordedMovements[movementIndex])):
                self.essaiButtons[i].configure(fg='black', bg='#009933', width=int(self.master.winfo_width()/(10*nbEssai)))
            elif (i==len(gv.recordedMovements[movementIndex])):
                self.essaiButtons[i].configure(fg='black', bg='#d9d9d9', width=int(self.master.winfo_width()/(10*nbEssai)))

    def addEssaiButton(self, index):
        l = tk.Label(self, text="n°"+str(index+1), justify=tk.CENTER, font=('Consolas', 10))
        l.configure(fg='black', bg='#b3b3b3')
        l.pack(side=tk.LEFT)
        self.essaiButtons.append(l)

    def retour(self):
        # supression des widgets présents sur la fenêtre
        for widget in self.winfo_children():
            widget.pack_forget()
        mn.Mouvements(self)

    def recommencer(self):
        gv.recordedMovements[self.movementIndex] = []
        self.init(self.movementIndex, self.desiredNumberOfEssai)

    def progression(self):
        newMovement = le.start()
        if (newMovement != None):
            self.essaiButtons[len(gv.recordedMovements[self.movementIndex])].configure(fg='black', bg='#009933')

            gv.recordedMovements[self.movementIndex].append(newMovement)

            if (len(gv.recordedMovements[self.movementIndex])>=len(self.essaiButtons)):
                self.addEssaiButton(len(self.essaiButtons))

            self.essaiButtons[len(gv.recordedMovements[self.movementIndex])].configure(fg='black', bg='#d9d9d9')
            self.bregis.configure(text="Nouvel essai : " + str(len(gv.recordedMovements[self.movementIndex])) + "/" +str(self.desiredNumberOfEssai))

            if len(gv.recordedMovements[self.movementIndex])>=self.desiredNumberOfEssai:
                print("finito")
                # Ajouter un label pour dire bien joué on peut passer à la suite mtn
                lf = tk.Label(self, text="Les 10 essais nécessaires ont été fait\nMais vous pouvez continuer à entrainer l'IA", justify=tk.CENTER, font=('Consolas', 10))
                lf.place(x=65, y=200)
        else:
            print("QUITTING")
            #QUIT
