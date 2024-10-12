import time
import random
from src.cell import *

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, window=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = window
        self.seed = seed
        self._cells = []

        if self.seed is not None:
            random.seed(self.seed)

        if self.num_cols > 0 and self.num_rows > 0:
            self.__create_cells()
            self.__break_entrance_and_exit()
            self.__break_walls_r(0, 0)
            self.__reset_cells_visited()

    def solve(self):
        return self.__solve_r(0, 0)

    def __solve_r(self, i, j):
        self.__animate()
        self._cells[i][j].visited = True

        # end cell
        if i == self.num_cols-1 and j == self.num_rows-1:
            return True

        directions = []

        # left cell
        if i > 0 and (not self._cells[i-1][j].visited and not self._cells[i][j].has_left_wall):
            directions.append((i-1, j))
        # right cell
        if i < self.num_cols - 1 and (not self._cells[i+1][j].visited and not self._cells[i][j].has_right_wall):
            directions.append((i+1, j))
        #top cell
        if j > 0 and (not self._cells[i][j-1].visited and not self._cells[i][j].has_top_wall):
            directions.append((i, j-1))
        # bottom cell
        if j < self.num_rows - 1 and (not self._cells[i][j+1].visited and not self._cells[i][j].has_bottom_wall):
            directions.append((i, j+1))

        for dir in directions:
            self._cells[i][j].draw_move(self._cells[dir[0]][dir[1]])
            if self.__solve_r(dir[0], dir[1]):
                return True
            self._cells[i][j].draw_move(self._cells[dir[0]][dir[1]], True)

        return False

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

    def __reset_cells_visited(self):
        for rows in self._cells:
            for cell in rows:
                cell.visited = False

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

    def __break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[-1][-1].has_bottom_wall = False

        self.__draw_cell(0, 0)
        self.__draw_cell(self.num_cols - 1, self.num_rows - 1)

    def __break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            need_to_visit = []

            # left cell
            if i > 0 and not self._cells[i-1][j].visited:
                need_to_visit.append((i-1, j))
            # right cell
            if i < self.num_cols - 1 and not self._cells[i+1][j].visited:
                need_to_visit.append((i+1, j))
            #top cell
            if j > 0 and not self._cells[i][j-1].visited:
                need_to_visit.append((i, j-1))
            # bottom cell
            if j < self.num_rows - 1 and not self._cells[i][j+1].visited:
                need_to_visit.append((i, j+1))

            if len(need_to_visit) == 0:
                self.__draw_cell(i, j)
                return

            direction_index = random.randrange(len(need_to_visit))
            next_index = need_to_visit[direction_index]

            # right
            if next_index[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False

            self.__break_walls_r(next_index[0], next_index[1])   #
