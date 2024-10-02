#!/usr/bin/env python

from src.window import *
from src.line import *
from src.cell import *

win = Window(800, 600)
cell = Cell(win)
cell.has_right_wall = False
cell.draw(Point(50,50), Point(100,100))

cell2 = Cell(win)
cell2.has_left_wall = False
cell2.draw(Point(100, 50), Point(150, 100))

cell.draw_move(cell2)
win.wait_for_close()
