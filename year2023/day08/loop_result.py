from typing import NamedTuple


class LoopResult(NamedTuple):
    loop_start: int
    loop_length: int
    steps_to_ends: tuple[int, ...]
