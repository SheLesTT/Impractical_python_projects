import random
import tkinter as tk



class Game(tk.Frame):
    """ Mounty Hall game"""

    doors  =('a', 'b', 'c')

    def __init__(self,parent):

        super(Game, self).__init__(parent)

        self.parent = parent
        self.img_file = 'all_closed.png'
        self.choice = ''
        self.winner = ''
        self.reval = ''
        self.first_choice_wins = 0
        self.pick_change_wins = 0
        self.create_widgets()

    def create_widgets(self):

        img = tk.PhotoImage(file= 'all_closed.png')
        self.photo_lbl = tk.Label(self.parent, image = img, text ='', borderwidth=0)
        self.photo_lbl.grid(row =0, column = 0, columnspan=10, sticky= "W")
        self.photo_lbl.image = img

        instr_input = [('There are money behind one of the dors',1,0,5,'W'),
                       ('There are goats behind others' 2,0,5,'W'),
                       ('Choose a door:', 1,3,1, "E")
                       ]

        for text, row, column, columnspan, sticky in instr_input:
            instr_lbl = tk.Label(self.parent, text = text)
            instr_lbl.grid(row=row, column=column, columnspan = columnspan,
                           sticky= sticky, ipadx=30)