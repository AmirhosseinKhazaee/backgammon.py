from engine.point import Point
from engine.color import Color
from engine.layouts.types import InitPoint
from layouts.default import DEFAULT

class Board:
    """
    this class is designed for configure the statholder of the game
    its store the current state of the game ,
    get_point let you get checker count and color of the point
    """

    def __init__(self, arrange: tuple[InitPoint]):
        self.initial_board = [
            Point(
                index=point.index, checker_count=point.checker_count, color=point.color
            )
            for point in arrange
        ]

    def get_point(self, index: int) -> Point:
        valid_range = range(1, 25)
        if index in valid_range:
            return self.initial_board[index - 1]
        else:
            raise ValueError("enter valid index (1 ,24)")

    def has_checker(self, index: int, color: Color) -> bool:
        point = self.get_point(index=index)
        if point.color == color and point.checker_count > 0:
            return True
        return False
