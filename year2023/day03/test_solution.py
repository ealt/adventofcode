import pytest
from solution import get_gear_ratios, get_part_numbers, read_schematic

EXAMPLE_SCHEMATIC = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


@pytest.fixture
def example_schematic() -> list[str]:
    return EXAMPLE_SCHEMATIC.splitlines()


@pytest.fixture
def actual_schematic() -> list[str]:
    return read_schematic("input.txt")


def test_get_part_numbers(example_schematic) -> None:
    assert get_part_numbers(example_schematic) == [
        467,
        35,
        633,
        617,
        592,
        755,
        664,
        598,
    ]


@pytest.mark.parametrize(
    "schematic_name, expected",
    [("example_schematic", 4361), ("actual_schematic", 540212)],
)
def test_part_number_sum(
    schematic_name: str, expected: int, request: pytest.FixtureRequest
) -> None:
    schematic = request.getfixturevalue(schematic_name)
    assert sum(get_part_numbers(schematic)) == expected


def test_get_gear_ratios(example_schematic) -> None:
    assert get_gear_ratios(example_schematic) == [16345, 451490]


@pytest.mark.parametrize(
    "schematic_name, expected",
    [("example_schematic", 467835), ("actual_schematic", 87605697)],
)
def test_gear_ratio_sum(
    schematic_name: str, expected: int, request: pytest.FixtureRequest
) -> None:
    schematic = request.getfixturevalue(schematic_name)
    assert sum(get_gear_ratios(schematic)) == expected
