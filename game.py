# -*- coding: utf-8 -*-

import time, random
from tkinter import *

'''this class contains all game graphics'''


class Graphics():
    def __init__(self):
        self.left = PhotoImage(file='graphics/left.png')
        self.right = PhotoImage(file='graphics/right.png')
        self.forward = PhotoImage(file='graphics/forward.png')
        self.wall = PhotoImage(file='graphics/wall.png')
        self.left_right = PhotoImage(file='graphics/left_right.png')
        self.forward_left = PhotoImage(file='graphics/left_forward.png')
        self.forward_right = PhotoImage(file='graphics/forward_right.png')
        self.forward_left_right = PhotoImage(file='graphics/forward_left_right.png')

'''this class contains all labyrinths in list of lists'''


class Labyrinths():
    def __init__(self):
        labyrinth1 = [[1, 0, 1], [1, 0, 1], [1, 0, 1]]

