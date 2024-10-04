import time
from src.cell import *

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window
        self._cells = []
        self.__create_cells()

    def __create_cells(self):
        for _ in range(self.num_cols):
            col = []
            for _ in range(self.num_rows):
                col.append(Cell(self.window))
            if len(col) > 0:
                self._cells.append(col)

        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self.__draw_cell(i, j)

    def __draw_cell(self, i, j):
        if self.window is None:
            return

        cell_start_x = self.x1 + (self.cell_size_x * i)
        cell_start_y = self.y1 + (self.cell_size_x * j)
        cell_end_x = cell_start_x + self.cell_size_x
        cell_end_y = cell_start_y + self.cell_size_y
        self._cells[i][j].draw(
            Point(cell_start_x, cell_start_y),
            Point(cell_end_x, cell_end_y)
        )
        self.__animate()

    def __animate(self):
        if self.window is None:
            return

        self.window.redraw()
        time.sleep(0.05)
