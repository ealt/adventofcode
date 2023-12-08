import pytest
from almanac import Almanac
from solution import (
    brute_force_pt2,
    get_closest_location,
    get_location,
    parse_almanac,
    read_almanac,
)

EXAMPLE_ALMANAC = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""


@pytest.fixture
def example_almanac() -> Almanac:
    return parse_almanac(EXAMPLE_ALMANAC)


@pytest.fixture
def actual_almanac() -> Almanac:
    return parse_almanac(read_almanac("input.txt"))


def test_get_location(example_almanac) -> None:
    assert [get_location(example_almanac, seed) for seed in example_almanac.seeds] == [
        82,
        43,
        86,
        35,
    ]


@pytest.mark.parametrize(
    "almanac_name, expected",
    [("example_almanac", 35), ("actual_almanac", 389056265)],
)
def test_closest_location(
    almanac_name: str, expected: int, request: pytest.FixtureRequest
) -> None:
    almanac = request.getfixturevalue(almanac_name)
    assert get_closest_location(almanac) == expected


def test_get_todo2(example_almanac) -> None:
    assert brute_force_pt2(example_almanac) == 46


@pytest.mark.parametrize(
    "almanac_name, expected",
    [("example_almanac", 46), ("actual_almanac", "137516820")],
)
def test_todo2(
    almanac_name: str, expected: int, request: pytest.FixtureRequest
) -> None:
    almanac = request.getfixturevalue(almanac_name)
    assert brute_force_pt2(almanac) == expected
