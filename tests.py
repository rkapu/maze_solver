#!/usr/bin/env python

import unittest

from src.maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )

    def test_maze_create_cells_with_zero_cols(self):
        m1 = Maze(0, 0, 12, 0, 10, 10)
        self.assertEqual(
            len(m1._cells),
            0,
        )

    def test_maze_create_cells_with_zero_rows(self):
        m1 = Maze(0, 0, 0, 10, 10, 10)
        self.assertEqual(
            len(m1._cells),
            0,
        )

    def test_maze_entrance_and_exit_broken(self):
        m1 = Maze(0, 0, 12, 10, 10, 10)
        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False
        )
        self.assertEqual(
            m1._cells[-1][-1].has_bottom_wall,
            False
        )

if __name__ == "__main__":
    unittest.main()
