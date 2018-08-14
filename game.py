# -*- coding: utf-8 -*-

import time, random
from tkinter import *

'''this class contains game graphics'''


class Graphics():
    def __init__(self):
        self.board = PhotoImage(file='graphics\\board.png')
        
        
'''game window and canvas'''


class Window():
    def __init__(self, graphics_object):
        # window declaration
        self.window = Tk()
        self.window.title('Labyrint Game')
        self.window.resizable(0, 0)
        self.window.wm_attributes('-topmost', 1)
        self.window.geometry('600x500')
        # canvas declaration
        self.canvas = Canvas(self.window, width=500, height=500, bd=0, highlightthickness=0)
        self.canvas.place(x=0, y=0)
        self.graphics = graphics_object()
        self.board = self.canvas.create_image(0, -1500, image=self.graphics.board, anchor='nw')
        # buttons declaration
        self.button1 = Button(self.window, text='1', font=('Arial', 20),
                              command=print, relief='solid')
        self.button1.place(x=500, y=0)
        self.button2 = Button(self.window, text='2', font=('Arial', 20),
                              command=print, relief='solid')
        self.button2.place(x=500, y=80)
        
'''this class contains all labyrinths in list of lists'''


class Labyrinths():
    def __init__(self):
        labyrinth1 = [[1, 2, 1], [1, 0, 1], [1, 0, 1]]
        
window = Window(Graphics)
window.window.mainloop()



