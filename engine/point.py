from dataclasses import dataclass
from engine.color import Color


@dataclass(frozen=True)
class Point:
    index: int
    color: Color | None
    checker_count: int