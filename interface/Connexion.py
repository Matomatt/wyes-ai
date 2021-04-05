import tkinter as tk
from PIL import Image, ImageTk
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
        self.configure(bg='white')
        self.pack()
        self.connex()
        self.testco()

    def connex(self):
        # connexion aux lunettes
        print("taille master connexion = " + str(self.master.winfo_width()) + "x" + str(self.master.winfo_height()))
        self.t1 = tk.Label(self, text="Connexion à vos lunettes impossible !", justify=tk.CENTER, font=('Montserrat', 20))
        self.t1.configure(fg='goldenrod', bg='white')
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
            photo = ImageTk.PhotoImage(Image.open("Images/connect.png").resize((550, 90), Image.ANTIALIAS))
            self.can = tk.Canvas(self, bg='white', highlightthickness=0)
            self.b1 = tk.Button(self, font=('Montserrat', 20), image=photo, compound='center')
            self.item = self.can.create_image(550, 90, image=photo)
            self.can.image = photo
            self.b1.configure(text="Cliquez pour accéder au logiciel malgré tout", fg="white", command=self.suiv, relief=tk.FLAT, overrelief=tk.FLAT)
            self.b1.pack(pady=50)
