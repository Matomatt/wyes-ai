import tkinter as tk
from tkinter import ttk
import Mouvements as mn
import time


class Regis(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.essai = 0
        self.pack()
        self.newmouv()

    def recup(self, idid):
        self.id = idid

    def newmouv(self):
        if self.essai!=10:
            # supression des widgets présents sur la fenêtre
            for widget in self.winfo_children():
                widget.pack_forget()
            # configuration du Header
            self.t1 = tk.Label(self, text="Enregistrement du mouvement", justify=tk.CENTER, font=('Consolas', 20))
            self.t1.configure(fg='goldenrod', bg='#f0f0f0')
            self.br = tk.Button(self, text="<- Retour", command=self.retour)
            self.br.configure(fg='lightgray', bg='#008080')
            self.t1.pack(side=tk.TOP)
            self.br.pack(side=tk.TOP)

            self.bregis = tk.Button(self, text="Nouvel essai", command=self.progression)
            self.bregis.pack(side=tk.TOP, pady=40)

        if self.essai==10:
            self.retour

    def retour(self):
        # supression des widgets présents sur la fenêtre
        for widget in self.winfo_children():
            widget.pack_forget()
        mn.Mouvements(self)

    def progression(self):
        self.progress = ttk.Progressbar(self, orient="horizontal",
                                        length=240, mode="determinate")
        self.progress.pack()
        self.progress.start()

        for i in range(12):
            self.progress["value"] = i * 9
            self.update()
            time.sleep(0.1)
        self.progress.stop()

        # Appel pour lancer un essai
        # | | | | | | | | | | | | | | |
        # | | | | CODES A MODIF | | | |
        # | | | | | | | | | | | | | | |
        # V V V V V V V V V V V V V V V

        # A A A A A A A A A A A A A A A
        # | | | | | | | | | | | | | | |
        # | | | | CODES A MODIF | | | |
        # | | | | | | | | | | | | | | |

        self.essai = self.essai+1

        if self.essai<10:
            self.newmouv()
        else:
            self.retour()