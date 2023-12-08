import argparse
import functools
import multiprocessing
import re
import time
from collections import deque
from typing import Iterator

from almanac import Almanac
from map_entry import MapEntry
from mapping import Mapping
from range import Range
from range_map import RangeMap
from seed_range import SeedRange

SEEDS_PATTERN = rf"seeds: (?P<seeds>\d+(?: \d+)*)"
CATEGORY_PATTERN = "[a-z]+"
MAP_TITLE_PATTERN = rf"({CATEGORY_PATTERN})-to-({CATEGORY_PATTERN}) map:"
MAP_ENTRY_PATTERN = rf"\d+(?: \d+){{2}}"
MAP_PATTERN = rf"{MAP_TITLE_PATTERN}\n{MAP_ENTRY_PATTERN}(?:\n{MAP_ENTRY_PATTERN})*"
ALMANAC_PATTERN = rf"{SEEDS_PATTERN}\n+{MAP_PATTERN}(?:\n+{MAP_PATTERN})"


def read_almanac(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def parse_map(map_text) -> RangeMap:
    items = []
    for m in re.finditer(MAP_ENTRY_PATTERN, map_text):
        entry = MapEntry(*map(int, m.group(0).split()))
        range = Range(entry.source_start, entry.range_length)
        delta = entry.destination_start - entry.source_start
        items.append((range, delta))
    delta_map = RangeMap(items)
    return delta_map


def parse_maps(almanac_text) -> dict[Mapping, RangeMap]:
    delta_maps: dict[Mapping, RangeMap] = {}
    for m in re.finditer(MAP_PATTERN, almanac_text):
        mapping = Mapping(source=m.group(1), destination=m.group(2))
        delta_maps[mapping] = parse_map(m.group(0))
    return delta_maps


def update_category_maps(almanac: Almanac) -> None:
    for mapping in almanac.delta_maps.keys():
        almanac.category_map[mapping.source] = mapping.destination


def parse_almanac(almanac_text: str) -> Almanac:
    almanac = Almanac()
    m = re.match(ALMANAC_PATTERN, almanac_text)
    if not m:
        raise ValueError("Could not parse almanac.")
    almanac.seeds = tuple(map(int, m.group("seeds").split()))
    almanac.delta_maps = parse_maps(almanac_text)
    update_category_maps(almanac)
    return almanac


def get_location(almanac: Almanac, seed: int) -> int:
    number = seed
    source = "seed"
    while source != "location":
        destination = almanac.category_map[source]
        mapping = Mapping(source, destination)
        delta_map = almanac.delta_maps[mapping]
        delta = delta_map.get(number, 0)
        number += delta
        source = destination
    return number


def get_closest_location(almanac: Almanac) -> int:
    return min(get_location(almanac, seed) for seed in almanac.seeds)


def get_running_closest(almanac: Almanac, closest_so_far: int, seed: int) -> int:
    return min(closest_so_far, get_location(almanac, seed))


def get_seeds_in_range(seed_range: SeedRange) -> Iterator[int]:
    for i in range(seed_range.range_length):
        yield seed_range.range_start + i


def get_seed_ranges(seeds: list[int]) -> Iterator[int]:
    values = deque(seeds)
    while values:
        range_start = values.popleft()
        range_length = values.popleft()
        yield SeedRange(range_start, range_length)


def get_closest_in_range(reduce_fun, seed_range: SeedRange) -> int:
    return functools.reduce(reduce_fun, get_seeds_in_range(seed_range), 1e12)


def brute_force_pt2(almanac: Almanac) -> str:
    pool = multiprocessing.Pool(processes=10)
    reduce_fun = functools.partial(get_running_closest, almanac)
    map_fun = functools.partial(get_closest_in_range, reduce_fun)
    return min(pool.map(map_fun, get_seed_ranges(almanac.seeds)))


def get_time_elapsed(start: float) -> None:
    end = time.time()
    dt = int(end - start)
    s = dt % 60
    dt //= 60
    m = dt % 60
    dt //= 60
    h = dt
    return f"{h}:{m:02}:{s:02}"


def main(filename: str) -> None:
    almanac_text = read_almanac(filename)
    almanac = parse_almanac(almanac_text)
    print(f"Closest location (seed numbers): {get_closest_location(almanac)}")

    # TODO: Implement a more efficient solution for ranges of seeds
    start = time.time()
    print(f"Closest location (seed ranges):  {brute_force_pt2(almanac)}")
    print(get_time_elapsed(start))  # 1:02:07


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TODO.")
    parser.add_argument(
        "--input", help="The path to an input file.", default="input.txt"
    )
    args = parser.parse_args()
    main(args.input)
