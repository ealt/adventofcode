from collections import defaultdict
from typing import Sequence

from position import Position
from schematic_explorer import SchematicExplorer


class GearFinder(SchematicExplorer):
    def __init__(self):
        super().__init__()
        self._neighboring_gears: list[Position] = []
        self._gears: defaultdict[Position, list[int]] = defaultdict(list)

    @property
    def gears(self) -> dict[Position, list[int]]:
        return {
            pos: part_numbers
            for pos, part_numbers in self._gears.items()
            if len(part_numbers) == 2
        }

    @property
    def _part(self) -> bool:
        return len(self._neighboring_gears) > 0

    def _is_symbol(self, val: str) -> bool:
        return val == "*"

    def _record_part_number(self) -> None:
        for gear in self._neighboring_gears:
            self._gears[gear].append(self._part_number)

    def explore(self, schematic: Sequence[str]) -> None:
        self._gears.clear()
        super().explore(schematic)

    def _add_digit(self, digit: str, pos: Position, schematic: Sequence[str]) -> None:
        for gear in self._get_adjacent_symbol_positions(pos, schematic):
            self._neighboring_gears.append(gear)
        super()._add_digit(digit)

    def _reset(self) -> None:
        super()._reset()
        self._neighboring_gears.clear()
