#!/usr/bin/env python

from src.window import *
from src.line import *
from src.cell import *
from src.maze import * 

window = Window(800, 600)

maze = Maze(50, 50, 10, 10, 50, 50, window)
maze.solve()

window.wait_for_close()
