import tkinter as tk
from Menu import Menu
import global_variables as gv
from CNN.payload import loadData
import serial
import glasses_calibration as gc

class Application(tk.Frame):
    def __init__(self, master=None):
        # initialisation de la nouvelle fenêtre
        super().__init__(master)
        self.master = master
        self.pack()
        self.connex()
        self.testco()

    def connex(self):
        # connexion aux lunettes
        print("taille master connexion = " + str(self.master.winfo_width()) + "x" + str(self.master.winfo_height()))
        self.t1 = tk.Label(self, text="Connexion à vos lunettes impossible", justify=tk.CENTER, font=('Consolas', 20))
        self.t1.configure(fg='goldenrod', bg='#f0f0f0')
        self.t1.pack(pady=20)

    def suiv(self):
        # supression des widgets présents sur la fenêtre
        for widget in self.winfo_children():
            widget.pack_forget()

        try:
            gv.recordedMovements = loadData("dataset").tolist()
        except:
            gv.recordedMovements = []
            
        Menu(self)

    def testco(self):
        try:
            gv.esp = serial.Serial(port='COM3', baudrate=115200, timeout=.1)
        except:
            gv.esp = None
        if(gv.esp!= None):
            gv.minThreshold = gc.start()
            print("Min Threshold :", gv.minThreshold)
            self.suiv()
        else:
            #Ajouter un bouton, pour dire connection foiré et permettre l'entrée au programme quand même
            self.b1 = tk.Button(self, font=('Consolas', 20))
            self.b1.configure(text="Connexion aux lunettes impossible\nCliquez pour accéder au logiciel malgré tout", bg="#cc0000", fg="white", command=self.suiv)
            self.b1.pack(pady=50)
