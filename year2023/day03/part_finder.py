from typing import Sequence

from position import Position
from schematic_explorer import DIGITS, SchematicExplorer


class PartFinder(SchematicExplorer):
    def __init__(self):
        super().__init__()
        self._has_adjacent_symbol: bool = False
        self._part_numbers: list[int] = []

    @property
    def part_numbers(self) -> list[int]:
        return self._part_numbers

    @property
    def _part(self) -> bool:
        return self._has_adjacent_symbol

    def _is_symbol(self, val: str) -> bool:
        return val != "." and val not in DIGITS

    def _record_part_number(self) -> None:
        self._part_numbers.append(self._part_number)

    def explore(self, schematic: Sequence[str]) -> None:
        self._part_numbers.clear()
        super().explore(schematic)

    def _add_digit(self, digit: str, pos: Position, schematic: Sequence[str]) -> None:
        if not self._part:
            self._has_adjacent_symbol = any(
                self._get_adjacent_symbol_positions(pos, schematic)
            )
        super()._add_digit(digit)

    def _reset(self) -> None:
        super()._reset()
        self._has_adjacent_symbol = False
