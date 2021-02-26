import tkinter as tk
import Menu as mn
import RegisterMouv as rm


class Mouvements(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.mouv()

    def mouv(self):
        # configuration du Header
        self.t1 = tk.Label(self, text="Fenêtre des mouvements", justify=tk.CENTER, font=('Consolas', 20))
        self.t1.configure(fg='goldenrod', bg='#f0f0f0')
        self.br = tk.Button(self, text="<- Retour", command=self.retour)
        self.br.configure(fg='lightgray', bg='#008080')
        self.t1.pack(side=tk.TOP)
        self.br.pack(side=tk.TOP)

        mouvexist = self.nbMouv()
        # choix des mouvements
        self.bm1 = tk.Button(self, text="Mouvement 1", width=33, height=45, command=self.enremouv)
        self.bm2 = tk.Button(self, text="Mouvement 2", width=33, height=45, command=self.enremouv)
        self.bm3 = tk.Button(self, text="Mouvement 3", width=33, height=45, command=self.enremouv)

        if mouvexist == 0:
            self.bm1.configure(fg='white', bg='#969696', activebackground='#009999', overrelief=tk.FLAT, relief=tk.FLAT)
            self.bm2.configure(fg='white', bg='#969696', activebackground='#009999', overrelief=tk.FLAT, relief=tk.FLAT)
            self.bm3.configure(fg='white', bg='#969696', activebackground='#009999', overrelief=tk.FLAT, relief=tk.FLAT)
        elif mouvexist == 1:
            self.bm1.configure(fg='white', bg='#008080', activebackground='#009999', overrelief=tk.FLAT, relief=tk.FLAT)
            self.bm2.configure(fg='white', bg='#969696', activebackground='#009999', overrelief=tk.FLAT, relief=tk.FLAT)
            self.bm3.configure(fg='white', bg='#969696', activebackground='#009999', overrelief=tk.FLAT, relief=tk.FLAT)
        elif mouvexist == 2:
            self.bm1.configure(fg='white', bg='#008080', activebackground='#009999', overrelief=tk.FLAT, relief=tk.FLAT)
            self.bm2.configure(fg='white', bg='#008080', activebackground='#009999', overrelief=tk.FLAT, relief=tk.FLAT)
            self.bm3.configure(fg='white', bg='#969696', activebackground='#009999', overrelief=tk.FLAT, relief=tk.FLAT)
        else:
            self.bm1.configure(fg='white', bg='#008080', activebackground='#009999', overrelief=tk.FLAT, relief=tk.FLAT)
            self.bm2.configure(fg='white', bg='#008080', activebackground='#009999', overrelief=tk.FLAT, relief=tk.FLAT)
            self.bm3.configure(fg='white', bg='#008080', activebackground='#009999', overrelief=tk.FLAT, relief=tk.FLAT)

        self.bm1.pack(in_=self, side=tk.LEFT, padx=10, pady=10)
        self.bm2.pack(in_=self, side=tk.LEFT, padx=10, pady=10)
        self.bm3.pack(in_=self, side=tk.RIGHT, padx=10, pady=10)

    def retour(self):
        # supression des widgets présents sur la fenêtre
        for widget in self.winfo_children():
            widget.pack_forget()
        mn.Menu(self)

    def nbMouv(self):
        # | | | | | | | | | | | | | | |
        # | | | | CODES A MODIF | | | |
        # | | | | | | | | | | | | | | |
        # V V V V V V V V V V V V V V V
        return 2
        # A A A A A A A A A A A A A A A
        # | | | | | | | | | | | | | | |
        # | | | | CODES A MODIF | | | |
        # | | | | | | | | | | | | | | |

    def enremouv(self):
        # supression des widgets présents sur la fenêtre
        for widget in self.winfo_children():
            widget.pack_forget()
        rm.Regis(self)