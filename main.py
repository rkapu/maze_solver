#!/usr/bin/env python

from src.window import *
from src.line import *
from src.cell import *

win = Window(800, 600)
cell = Cell(win)
cell.draw(Point(50,50), Point(100,100))
win.wait_for_close()
