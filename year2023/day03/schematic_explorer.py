import abc
import string
from typing import Iterable, Iterator, Sequence

from position import Position

DIGITS = set(string.digits)


class SchematicExplorer(abc.ABC):
    def __init__(self):
        self._digits: list[str] = []

    @property
    @abc.abstractmethod
    def _is_part(self) -> bool:
        pass

    @property
    def _part_number(self) -> int:
        if self._is_part and self._digits:
            return int("".join(self._digits))
        return 0

    @abc.abstractmethod
    def _is_symbol(self, val: str) -> bool:
        pass

    @abc.abstractmethod
    def _record_part_number(self) -> None:
        pass

    def explore(self, schematic: Sequence[str]) -> None:
        for r, row in enumerate(schematic):
            for c, val in enumerate(row):
                if val in DIGITS:
                    pos = Position(row=r, col=c)
                    self._add_digit(val, pos, schematic)
                else:
                    if self._part_number:
                        self._record_part_number()
                    self._reset()
            if self._part_number:
                self._record_part_number()
            self._reset()

    def _add_digit(self, digit: str, *args, **kwargs) -> None:
        self._digits.append(digit)

    def _reset(self) -> None:
        self._digits.clear()

    def _get_adjacent_symbol_positions(
        self, pos: Position, schematic: Sequence[str]
    ) -> Iterable[Position]:
        for neighbor in self._get_neighbors(pos, schematic):
            val = schematic[neighbor.row][neighbor.col]
            if self._is_symbol(val):
                yield neighbor

    def _get_neighbors(
        self, pos: Position, schematic: Sequence[str]
    ) -> Iterator[Position]:
        height = len(schematic)
        width = len(schematic[0])
        up = pos.row > 0
        down = pos.row < height - 1
        left = pos.col > 0
        right = pos.col < width - 1
        right_only = len(self._digits) > 0
        if right:
            yield Position(row=pos.row, col=pos.col + 1)
            if up:
                yield Position(row=pos.row - 1, col=pos.col + 1)
            if down:
                yield Position(row=pos.row + 1, col=pos.col + 1)
        if not right_only:
            if up:
                yield Position(row=pos.row - 1, col=pos.col)
            if down:
                yield Position(row=pos.row + 1, col=pos.col)
        if left and not right_only:
            yield Position(row=pos.row, col=pos.col - 1)
            if up:
                yield Position(row=pos.row - 1, col=pos.col - 1)
            if down:
                yield Position(row=pos.row + 1, col=pos.col - 1)
