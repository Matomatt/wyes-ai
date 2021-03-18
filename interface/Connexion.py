import tkinter as tk
from Menu import Menu
import global_variables as gv
from CNN.payload import loadData
import serial

class Application(tk.Frame):
    def __init__(self, master=None):
        # initialisation de la nouvelle fenêtre
        super().__init__(master)
        self.master = master
        self.pack()
        self.connex()

    def connex(self):
        # connexion aux lunettes
        self.t1 = tk.Label(self, text="Connexion à vos lunettes", justify=tk.CENTER, font=('Consolas', 20))
        self.t1.configure(fg='goldenrod', bg='#f0f0f0')
        self.b1 = tk.Button(self, text="Connexion ->", command=self.testco)
        self.b1.configure(fg='goldenrod', bg='#f0f0f0', overrelief=tk.FLAT)
        self.t1.pack(pady=20)
        self.b1.pack(pady=220)

    def suiv(self):
        # supression des widgets présents sur la fenêtre
        for widget in self.winfo_children():
            widget.pack_forget()

        gv.recordedMovements = loadData("dataset").tolist()

        Menu(self)

    def testco(self):
        try:
            gv.esp = serial.Serial(port='COM6', baudrate=115200, timeout=.1)
        except:
            gv.esp = None
        if(gv.esp!= None) :
            print("Let's go")
            self.suiv()
        else :
            print("error")
