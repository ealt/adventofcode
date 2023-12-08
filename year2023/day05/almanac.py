import dataclasses
from typing import Collection

from mapping import Mapping
from range_map import RangeMap


@dataclasses.dataclass
class Almanac:
    seeds: Collection[int] = dataclasses.field(default_factory=list)
    category_map: dict[str, str] = dataclasses.field(default_factory=dict)
    delta_maps: dict[Mapping, RangeMap] = dataclasses.field(default_factory=dict)
