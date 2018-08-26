# -*- coding: utf-8 -*-

import time, random
from tkinter import *

'''this class contains game graphics'''


class Graphics():
    def __init__(self):
        self.board = PhotoImage(file='graphics\\board.png')
        
'''this class contains all labyrinths in list of lists'''


class Labyrinths():
    def __init__(self):
        # 0 - corridor, 1 - wall, 2 - exit
        self.labyrinth1 = [[1, 2, 1], [1, 0, 1], [1, 0, 1], [1, 1, 1]]
        
    def turn_around(self, labyrinth):
        labyrinth = labyrinth[-1::-1] #  nie zadzaila
        
'''main game class, game window, buttons and canvas'''


class Window():
    def __init__(self, graphics_object, labyrinths_object):
        self.labyrinths = labyrinths_object()
        # window declaration
        self.window = Tk()
        self.window.title('Labyrinth Game')
        self.window.resizable(0, 0)
        self.window.wm_attributes('-topmost', 1)
        self.window.geometry('650x500')
        # canvas declaration
        self.canvas = Canvas(self.window, width=500, height=500, bd=0, highlightthickness=0)
        self.canvas.place(x=0, y=0)
        self.graphics = graphics_object()
        self.board = self.canvas.create_image(0, -1500, image=self.graphics.board, anchor='nw')
        # buttons and labels declaration
        self.labelLabyrinths = Label(self.window, text='Labyrinths', font=('Arial', 20))
        self.labelLabyrinths.place(x=510, y=10)
        self.button1 = Button(self.window, text='I    ', font=('Arial', 20),
                              command=print, relief='solid')
        self.button1.place(x=510, y=60)
        self.button2 = Button(self.window, text='II   ', font=('Arial', 20),
                              command=print, relief='solid')
        self.button2.place(x=580, y=60)
        self.button3 = Button(self.window, text='III  ', font=('Arial', 20),
                              command=print, relief='solid')
        self.button3.place(x=510, y=120)
        self.button4 = Button(self.window, text='IV  ', font=('Arial', 20),
                              command=print, relief='solid')
        self.button4.place(x=580, y=120)
        self.button5 = Button(self.window, text='V   ', font=('Arial', 20),
                              command=print, relief='solid')
        self.button5.place(x=510, y=180)
        self.button6 = Button(self.window, text='VI  ', font=('Arial', 20),
                              command=print, relief='solid')
        self.button6.place(x=580, y=180)
        self.button7 = Button(self.window, text='VII ', font=('Arial', 20),
                              command=print, relief='solid')
        self.button7.place(x=510, y=240)
        self.button8 = Button(self.window, text='VIII', font=('Arial', 20),
                              command=print, relief='solid')
        self.button8.place(x=580, y=240)
        self.labelKeys = Label(self.window, text='KEYS', font=('Arial', 12))
        self.labelKeys.place(x=510, y=320)
        self.labelW = Label(self.window, text='W    FORWARD', font=('Arial', 10))
        self.labelW.place(x=510, y=350)
        self.labelA = Label(self.window, text='A     LEFT', font=('Arial', 10))
        self.labelA.place(x=510, y=380)
        self.labelD = Label(self.window, text='D     RIGHT', font=('Arial', 10))
        self.labelD.place(x=510, y=410)
        self.labelS = Label(self.window, text='S     TURN AROUND', font=('Arial', 10))
        self.labelS.place(x=510, y=440)
        # position of graphics board
        self.board_position = [0, -1500]
        
    def move_forward(self):
        pass
        
window = Window(Graphics, Labyrinths)
window.window.mainloop()



