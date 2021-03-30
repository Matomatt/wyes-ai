import tkinter as tk
import Menu as mn
import random
import live_emulation as le
import global_variables as gv
import numpy as np


class Controle(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.co = True
        self.master = master
        self.pack()
        self.cont()

    def cont(self):
        print("taille master controle = " + str(self.master.winfo_width()) + "x" + str(self.master.winfo_height()))
        if self.co == True:
            # supression des widgets présents sur la fenêtre
            for widget in self.winfo_children():
                widget.pack_forget()

            # configuration du Header
            self.br = tk.Button(self, text="<---", command=self.retour)
            self.br.configure(fg='lightgray', bg='#008080')
            self.br.pack(padx=10, pady=10)
            self.br.place(x=0, y=0)
            self.t1 = tk.Label(self)
            self.t1.pack(side=tk.TOP)

            self.movementButtons = []
            for i in range(len(gv.recordedMovements)):
                button = tk.Button(self, text="Mouvement "+str(i+1), width=int((self.master.winfo_width()/10-len(gv.recordedMovements)-1)/len(gv.recordedMovements)), height=10)
                button.pack(in_=self, side=tk.LEFT, padx=10, pady=10)
                self.movementButtons.append(button)

        if self.co==True:
            self.after(100, self.predictMouv)




    def retour(self):
        self.co = False
        # supression des widgets présents sur la fenêtre
        for widget in self.winfo_children():
            widget.pack_forget()
        mn.Menu(self)

    def predictMouv(self):
        mouv = self.whichMouv(le.start())

        if (mouv == -1):
            self.retour()
            return

        for bt in self.movementButtons:
            bt.configure(fg='white', bg='#969696', activebackground='#969696', overrelief=tk.FLAT, relief=tk.FLAT)
        self.movementButtons[mouv].configure(fg='white', bg='#008080', activebackground='#009999', overrelief=tk.FLAT, relief=tk.FLAT)

        if self.co==True:
            self.after(100, self.predictMouv)

    def whichMouv(self, record):
        if (record == None):
            return -1

        arr = []
        arr.append(record)
        Y_hat = gv.AImodel.predict(np.expand_dims(arr, -1))

        print(Y_hat)
        return list(Y_hat[0]).index(max(Y_hat[0]))
