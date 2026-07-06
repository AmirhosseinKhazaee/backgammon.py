from typing import NamedTuple
from engine.color import Color

class InitPoint(NamedTuple):
    index : int
    color : Color | None
    checker_count : int


