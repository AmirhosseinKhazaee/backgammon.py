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
        self.points = [
            Point(
                index=point.index, checker_count=point.checker_count, color=point.color
            )
            for point in arrange
        ]

    def get_point(self, index: int) -> Point:
        self.points_length = len(self.points)
        if 1 <= index <= self.points_length:
            return self.points[index - 1]
        else:
            raise ValueError(f"enter valid index (1 ,{self.points_length})")

    def has_checker(self, index: int, color: Color) -> bool:
        point = self.get_point(index=index)
        if point.color == color and point.checker_count > 0:
            return True
        return False
