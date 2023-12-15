import dataclasses
from typing import Optional


@dataclasses.dataclass
class Node:
    label: str = ""
    left: Optional["Node"] = None
    right: Optional["Node"] = None
