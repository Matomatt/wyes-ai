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
        self.essai = 0
        self.nummouv = 0
        self.pack()

    def newmouv(self):
        if self.essai!=10:
            # supression des widgets présents sur la fenêtre
            for widget in self.winfo_children():
                widget.pack_forget()
            # configuration du Header
            self.t1 = tk.Label(self, text="Enregistrement du mouvement " + str(self.nummouv), justify=tk.CENTER, font=('Consolas', 20))
            self.t1.configure(fg='goldenrod', bg='#f0f0f0')
            self.br = tk.Button(self, text="<- Retour", command=self.retour)
            self.br.configure(fg='lightgray', bg='#008080')
            self.t1.pack(side=tk.TOP)
            self.br.pack(side=tk.TOP)

            self.bregis = tk.Button(self, text="Nouvel essai : " + str(self.essai + 1) + "/10", command=self.progression)
            self.bregis.pack(side=tk.TOP, pady=20)
            
            self.bagain = tk.Button(self, text="Recommencer ou supprimer le mouvement", command=self.recommencer)
            self.bagain.configure(fg='lightgray', bg='#b30000')
            self.bagain.pack(side=tk.BOTTOM, pady=120)
            
            self.etape()

        if self.essai==10:
            self.retour


    def retour(self):
        # supression des widgets présents sur la fenêtre
        for widget in self.winfo_children():
            widget.pack_forget()
        mn.Mouvements(self)
        
    def etape(self):
        if self.essai == 0:
            self.ff = tk.Frame(self)
            self.ff.l1 = tk.Label(self.ff, text="Essai n°1", justify=tk.CENTER, font=('Consolas', 10))
            self.ff.l1.configure(fg='black', bg='#d9d9d9')
            self.ff.l2 = tk.Label(self.ff, text="Essai n°2", justify=tk.CENTER, font=('Consolas', 10))
            self.ff.l2.configure(fg='black', bg='#b3b3b3')
            self.ff.l3 = tk.Label(self.ff, text="Essai n°3", justify=tk.CENTER, font=('Consolas', 10))
            self.ff.l3.configure(fg='black', bg='#b3b3b3')
            self.ff.l4 = tk.Label(self.ff, text="Essai n°4", justify=tk.CENTER, font=('Consolas', 10))
            self.ff.l4.configure(fg='black', bg='#b3b3b3')
            self.ff.l5 = tk.Label(self.ff, text="Essai n°5", justify=tk.CENTER, font=('Consolas', 10))
            self.ff.l5.configure(fg='black', bg='#b3b3b3')
            self.ff.l6 = tk.Label(self.ff, text="Essai n°6", justify=tk.CENTER, font=('Consolas', 10))
            self.ff.l6.configure(fg='black', bg='#b3b3b3')
            self.ff.l7 = tk.Label(self.ff, text="Essai n°7", justify=tk.CENTER, font=('Consolas', 10))
            self.ff.l7.configure(fg='black', bg='#b3b3b3')
            self.ff.l8 = tk.Label(self.ff, text="Essai n°8", justify=tk.CENTER, font=('Consolas', 10))
            self.ff.l8.configure(fg='black', bg='#b3b3b3')
            self.ff.l9 = tk.Label(self.ff, text="Essai n°9", justify=tk.CENTER, font=('Consolas', 10))
            self.ff.l9.configure(fg='black', bg='#b3b3b3')
            self.ff.l10 = tk.Label(self.ff, text="Essai n°10", justify=tk.CENTER, font=('Consolas', 10))
            self.ff.l10.configure(fg='black', bg='#b3b3b3')

        if self.essai == 1:
            self.ff.l2.configure(fg='black', bg='#d9d9d9')
            self.ff.l1.configure(fg='black', bg='#009933')
        if self.essai == 2:
            self.ff.l3.configure(fg='black', bg='#d9d9d9')
            self.ff.l2.configure(fg='black', bg='#009933')
        if self.essai == 3:
            self.ff.l4.configure(fg='black', bg='#d9d9d9')
            self.ff.l3.configure(fg='black', bg='#009933')
        if self.essai == 4:
            self.ff.l5.configure(fg='black', bg='#d9d9d9')
            self.ff.l4.configure(fg='black', bg='#009933')
        if self.essai == 5:
            self.ff.l6.configure(fg='black', bg='#d9d9d9')
            self.ff.l5.configure(fg='black', bg='#009933')
        if self.essai == 6:
            self.ff.l7.configure(fg='black', bg='#d9d9d9')
            self.ff.l6.configure(fg='black', bg='#009933')
        if self.essai == 7:
            self.ff.l8.configure(fg='black', bg='#d9d9d9')
            self.ff.l7.configure(fg='black', bg='#009933')
        if self.essai == 8:
            self.ff.l9.configure(fg='black', bg='#d9d9d9')
            self.ff.l8.configure(fg='black', bg='#009933')
        if self.essai == 9:
            self.ff.l10.configure(fg='black', bg='#d9d9d9')
            self.ff.l9.configure(fg='black', bg='#009933')

        self.ff.l10.pack(side=tk.RIGHT)
        self.ff.l9.pack(side=tk.RIGHT)
        self.ff.l8.pack(side=tk.RIGHT)
        self.ff.l7.pack(side=tk.RIGHT)
        self.ff.l6.pack(side=tk.RIGHT)
        self.ff.l5.pack(side=tk.RIGHT)
        self.ff.l4.pack(side=tk.RIGHT)
        self.ff.l3.pack(side=tk.RIGHT)
        self.ff.l2.pack(side=tk.RIGHT)
        self.ff.l1.pack(side=tk.RIGHT)

        self.ff.pack(side=tk.BOTTOM)


    def quelmouv(self, idid):
        self.nummouv = idid

        while (len(gv.recordedMovements) < idid):
            #print(str(idid) + " - " + str(len(gv.recordedMovements)))
            gv.recordedMovements.append([])


    def recommencer(self):
        self.essai=0
        # Remettre à 0 la matrice
        # | | | | | | | | | | | | | | |
        # | | | | CODES A MODIF | | | |
        # | | | | | | | | | | | | | | |
        # V V V V V V V V V V V V V V V

        # A A A A A A A A A A A A A A A
        # | | | | | | | | | | | | | | |
        # | | | | CODES A MODIF | | | |
        # | | | | | | | | | | | | | | |
        self.newmouv()
        
    def progression(self):
        self.essai = self.essai + 1

        # Appel pour lancer un essai
        # | | | | | | | | | | | | | | |
        # | | | | CODES A MODIF | | | |
        # | | | | | | | | | | | | | | |
        # V V V V V V V V V V V V V V V

        gv.recordedMovements[self.nummouv-1].append(le.start())
        print(gv.recordedMovements[self.nummouv-1])

        # A A A A A A A A A A A A A A A
        # | | | | | | | | | | | | | | |
        # | | | | CODES A MODIF | | | |
        # | | | | | | | | | | | | | | |

        if self.essai<10:
            self.newmouv()
        else:
            self.retour()
