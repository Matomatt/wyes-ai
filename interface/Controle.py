import tkinter as tk
import Menu as mn
import random


class Controle(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.co = True
        self.master = master
        self.pack()
        self.cont()

    def cont(self):
        if self.co == True:
            # supression des widgets présents sur la fenêtre
            for widget in self.winfo_children():
                widget.pack_forget()

            # configuration du Header
            self.t1 = tk.Label(self, text="Fenêtre de contrôle", justify=tk.CENTER, font=('Consolas', 20))
            self.t1.configure(fg='goldenrod', bg='#f0f0f0')
            self.br = tk.Button(self, text="<- Retour", command=self.retour)
            self.br.configure(fg='lightgray', bg='#008080')
            self.t1.pack(side=tk.TOP)
            self.br.pack(side=tk.TOP)

            self.bm1 = tk.Button(self, text="Mouvement 1", width=33, height=10)
            self.bm2 = tk.Button(self, text="Mouvement 2", width=33, height=10)
            self.bm3 = tk.Button(self, text="Mouvement 3", width=33, height=10)

            mouv = self.whichMouv()

            # Mouvement 1
            if(mouv==1):
                self.bm1.configure(fg='white', bg='#008080', activebackground='#009999', overrelief=tk.FLAT,
                                   relief=tk.FLAT)
                self.bm2.configure(fg='white', bg='#969696', activebackground='#969696', overrelief=tk.FLAT,
                                   relief=tk.FLAT)
                self.bm3.configure(fg='white', bg='#969696', activebackground='#969696', overrelief=tk.FLAT,
                                   relief=tk.FLAT)

            # Mouvement 2
            elif(mouv==2):
                self.bm1.configure(fg='white', bg='#969696', activebackground='#969696', overrelief=tk.FLAT,
                                   relief=tk.FLAT)
                self.bm2.configure(fg='white', bg='#008080', activebackground='#009999', overrelief=tk.FLAT,
                                   relief=tk.FLAT)
                self.bm3.configure(fg='white', bg='#969696', activebackground='#969696', overrelief=tk.FLAT,
                                   relief=tk.FLAT)

            # Mouvement 3
            else:
                self.bm1.configure(fg='white', bg='#969696', activebackground='#969696', overrelief=tk.FLAT,
                                   relief=tk.FLAT)
                self.bm2.configure(fg='white', bg='#969696', activebackground='#969696', overrelief=tk.FLAT,
                                   relief=tk.FLAT)
                self.bm3.configure(fg='white', bg='#008080', activebackground='#009999', overrelief=tk.FLAT,
                                   relief=tk.FLAT)

            # Affichage des boutons mouvements
            self.bm1.pack(in_=self, side=tk.LEFT, padx=10, pady=10)
            self.bm2.pack(in_=self, side=tk.LEFT, padx=10, pady=10)
            self.bm3.pack(in_=self, side=tk.LEFT, padx=10, pady=10)

        if self.co==True:
            self.after(1200, self.cont)

    def retour(self):
        self.co = False
        # supression des widgets présents sur la fenêtre
        for widget in self.winfo_children():
            widget.pack_forget()
        mn.Menu(self)

    def whichMouv(self):
        # | | | | | | | | | | | | | | |
        # | | | | CODES A MODIF | | | |
        # | | | | | | | | | | | | | | |
        # V V V V V V V V V V V V V V V
        return random.randint(1, 3)
        # A A A A A A A A A A A A A A A
        # | | | | | | | | | | | | | | |
        # | | | | CODES A MODIF | | | |
        # | | | | | | | | | | | | | | |

