from dataclasses import dataclass

from engine.color import Color
from engine.point import Point, PointIndex


@dataclass(frozen=True)
class MoveCommand:
    start_point: PointIndex
    end_point: Point
    color: Color
    dice_value: int
