#!/usr/bin/env python

from src.window import *
from src.line import *
from src.cell import *
from src.maze import * 

window = Window(800, 600)

Maze(50, 50, 5, 3, 50, 50, window)

window.wait_for_close()
