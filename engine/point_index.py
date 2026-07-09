from dataclasses import dataclass
from typing import ClassVar


@dataclass(frozen=True)
class PointIndex:
    value: int
    MIN_INDEX : ClassVar[int] = 1
    MAX_INDEX: ClassVar[int] = 24

    def __post_init__(self):
        if not self.MIN_INDEX <= self.value <= self.MAX_INDEX:
            raise ValueError(f"enter valid range between {self.MIN_INDEX} to {self.MAX_INDEX}")
