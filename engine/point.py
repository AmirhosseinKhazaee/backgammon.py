from dataclasses import dataclass
from engine.color import Color
from engine.point_index import PointIndex


@dataclass
class Point:
    index: PointIndex
    color: Color | None
    checker_count: int

    def __post_init__(self):
        if self.checker_count < 0:
            raise ValueError("checker_count cannot be negative")
        if self.checker_count == 0 and self.color is not None:
            raise ValueError("color of point with zero checker count should be none !")

    def remove_checker(self):
        if self.checker_count == 0:
            raise ValueError(
                "this point already empty you can't remove checker from it !"
            )
        self.checker_count -= 1
        if self.checker_count == 0:
            self.color = None

    def add_checker(self, color : Color):
        if self.checker_count == 0:
            self.color = color
            self.checker_count += 1
        elif self.color != color:
            raise ValueError(
                f"you cannot add this color , the point is already filled with another color"
            )
        else:
            self.checker_count += 1
