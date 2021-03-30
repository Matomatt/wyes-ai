import tkinter as tk
from tkinter import ttk
import Menu
import Menu as mn
import time
from CNN.payload import *
import global_variables as gv
import numpy as np


class TrMouv(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.essai = 0
        self.nummouv = 0
        self.pack()

    def newmouv(self):
        print("taille master training = " + str(self.master.winfo_width()) + "x" + str(self.master.winfo_height()))
        # supression des widgets présents sur la fenêtre
        for widget in self.winfo_children():
            widget.pack_forget()
        # configuration du Header
        self.t1 = tk.Label(self)
        self.br = tk.Button(self, text="<---", command=self.retour)
        self.br.configure(fg='lightgray', bg='#008080')
        self.br.pack(padx=10, pady=10)
        self.br.place(x=0, y=0)
        self.t1.pack(side=tk.TOP)

        self.ex = tk.Label(self, text="Training permet d'entrainer l'intelligence artificielle du logiciel, plus vous l'entrainerez, plus celle-ci deviendra performante dans l'analyse de vos mouvements.\n"
                                      "")
        self.ex.pack(pady=20)

        self.btrain = tk.Button(self, text="Training", command=self.training, font='Consolas 22 bold')
        self.btrain.configure(fg='lightgray', bg='#2d8659')
        self.btrain.pack(side=tk.TOP, pady=100)


    def retour(self):
        # supression des widgets présents sur la fenêtre
        for widget in self.winfo_children():
            widget.pack_forget()
        mn.Menu(self)

    def menu(self):
        # supression des widgets présents sur la fenêtre
        for widget in self.winfo_children():
            widget.pack_forget()
        Menu.Menu(self)

    def training(self):
        print('*'*25 + 'training du model' + '*'*25)
        
        print("plop avant", len(gv.recordedMovements[0]))
        
        if (len(gv.recordedMovements)<1):
            data = loadData()
            print("plop if", len(gv.recordedMovements[0]))
        else:
            print("plop else", len(gv.recordedMovements[0]))
            data = gv.recordedMovements[0:]
            file = open("dataset", "wb") # open a binary file in write mode
            np.save(file, np.array(data)) # save array to the file
            file.close
            print("plop data", len(data[0]))
        print("plop appr", len(gv.recordedMovements[0]))

        print("LOADED DATA", len(data), len(data[0]), len(data[0][0]), len(data[0][0][0]))

        # 1 essai toujours 12*19

        # data = [
        # mouvement 1: [ [essai1], [essai2], ... ],
        # mouvement 2: [ [essai1], [essai2], ... ],
        # mouvement 3: [ [essai1], [essai2], ... ],
        # ...
        # ]

        X_train , Y_train , X_test, Y_test = splitData(data, 0.6)

        # [
        # [m1 essai1],
        # [m1 essai2],
        # ...
        # [mx essaiz]
        # ]

        model = createModel(X_train, Y_train)
        gv.AImodel = train(model, X_train, Y_train, X_test, Y_test)

        self.newmouv()
