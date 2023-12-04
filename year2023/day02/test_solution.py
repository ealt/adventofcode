import pytest
from solution import get_possible_ids, get_power, read_game_records

EXAMPLE_RECORDS = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""


@pytest.fixture
def example_game_records() -> list[str]:
    return EXAMPLE_RECORDS.splitlines()


@pytest.fixture
def actual_game_records() -> list[str]:
    return read_game_records("input.txt")


def test_get_possible_ids(example_game_records) -> None:
    assert list(get_possible_ids(example_game_records)) == [1, 2, 5]


@pytest.mark.parametrize(
    "game_records_name,expected",
    [("example_game_records", 8), ("actual_game_records", 2505)],
)
def test_possible_id_sum(
    game_records_name: str, expected: int, request: pytest.FixtureRequest
) -> None:
    game_records = request.getfixturevalue(game_records_name)
    assert sum(get_possible_ids(game_records)) == expected


def test_get_power(example_game_records) -> None:
    assert list(map(get_power, example_game_records)) == [48, 12, 1560, 630, 36]


@pytest.mark.parametrize(
    "game_records_name,expected",
    [("example_game_records", 2286), ("actual_game_records", 70265)],
)
def test_power_sum(
    game_records_name: str, expected: int, request: pytest.FixtureRequest
) -> None:
    game_records = request.getfixturevalue(game_records_name)
    assert sum(map(get_power, game_records)) == expected
