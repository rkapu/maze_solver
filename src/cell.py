from src.line import *

class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_top_wall = True
        self.has_right_wall = True
        self.has_bottom_wall = True
        self.__window = window
        self.__start_point = None
        self.__end_point = None

    def draw(self, start_point, end_point):
        self.__start_point = start_point
        self.__end_point = end_point

        lines = [
            self.__left_wall_line(),
            self.__top_wall_line(),
            self.__right_wall_line(),
            self.__bottom_wall_line()
        ]
        for line in lines:
            if line is not None:
                self.__window.draw_line(line)

    def __left_wall_line(self):
        if self.has_left_wall:
            return Line(
                self.__start_point,
                Point(self.__start_point.x, self.__end_point.y)
            )

    def __top_wall_line(self):
        if self.has_top_wall:
            return Line(
                self.__start_point,
                Point(self.__end_point.x, self.__start_point.y)
            )

    def __right_wall_line(self):
        if self.has_right_wall:
            return Line(
                Point(self.__end_point.x, self.__start_point.y),
                self.__end_point
            )

    def __bottom_wall_line(self):
        if self.has_bottom_wall:
            return Line(
                self.__end_point,
                Point(self.__start_point.x, self.__end_point.y)
            )
