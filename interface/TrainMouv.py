import tkinter as tk
from tkinter import ttk
import Menu
import Menu as mn
import time
from CNN.payload import *
import global_variables as gv


class TrMouv(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.essai = 0
        self.nummouv = 0
        self.pack()

    def newmouv(self):
        # supression des widgets présents sur la fenêtre
        for widget in self.winfo_children():
            widget.pack_forget()
        # configuration du Header
        self.t1 = tk.Label(self, text="Training des mouvements", justify=tk.CENTER, font=('Consolas', 20))
        self.t1.configure(fg='goldenrod', bg='#f0f0f0')
        self.br = tk.Button(self, text="<- Retour", command=self.retour)
        self.br.configure(fg='lightgray', bg='#008080')
        self.t1.pack(side=tk.TOP)
        self.br.pack(side=tk.TOP)

        self.btrain = tk.Button(self, text="Training", command=self.training)
        self.btrain.configure(fg='lightgray', bg='#2d8659')
        self.btrain.pack(side=tk.TOP, pady=20)


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
        # Appel pour lancer un essai
        # | | | | | | | | | | | | | | |
        # | | | | CODES A MODIF | | | |
        # | | | | | | | | | | | | | | |
        # V V V V V V V V V V V V V V V
        print('*'*25 + 'training du model' + '*'*25)
        # 3( nombre de type de mouv ) 1 (nombre d'essai) 19 (nombre de seconde) 12 (nombre de capteur)
        """
        # 30 2 19 6 
        tableau  = gv.recordedMovements # 3 10 19 12 -> 30 2 19 6 
        data = []
        for i in range(len(tableau)): #nombre de type de mouv -> 3
            for j in range(len(tableau[0])): #nombre d'essai -> 10
                tab1_ = [] 
                tab2_ = []
                for k in range(len(tableau[0][0])): #nombre de seconde -> 19 
                    tab1_.append(tableau[i][j][k][:6]) #six premier capteurs
                    tab2_.append(tableau[i][j][k][6:]) # six derniers capteurs
                data.append([tab1_, tab2_])
        print(f' dimension :\t[{len(data)}][{len(data[0])}][{len(data[0][0])}][{len(data[0][0][0])}]')

        x_train , y_train , x_test, y_test = splitData(data,percent = 0.5, number_of_movements = len(tableau[0]))
        model = createModel(x_train,y_train)
        model = train(model,x_train,y_train,x_test,y_test)
        """
        
        data = loadData()
        x_train , y_train , x_test, y_test = splitData(data)
        model = createModel(x_train,y_train)
        model = train(model,x_train,y_train,x_test,y_test)
        
        # A A A A A A A A A A A A A A A
        # | | | | | | | | | | | | | | |
        # | | | | CODES A MODIF | | | |
        # | | | | | | | | | | | | | | |
        
        self.newmouv()
