from typing import NamedTuple


class MapEntry(NamedTuple):
    destination_start: int
    source_start: int
    range_length: int
