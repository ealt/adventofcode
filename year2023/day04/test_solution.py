import pytest
from solution import get_num_cards, get_points, read_card_list

EXAMPLE_CARD_LIST = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""


@pytest.fixture
def example_card_list() -> list[str]:
    return EXAMPLE_CARD_LIST.splitlines()


@pytest.fixture
def actual_card_list() -> list[str]:
    return read_card_list("input.txt")


def test_get_points(example_card_list) -> None:
    assert list(map(get_points, example_card_list)) == [8, 2, 2, 1, 0, 0]


@pytest.mark.parametrize(
    "card_list_name, expected",
    [("example_card_list", 13), ("actual_card_list", 21088)],
)
def test_point_sum(
    card_list_name: str, expected: int, request: pytest.FixtureRequest
) -> None:
    card_list = request.getfixturevalue(card_list_name)
    assert sum(map(get_points, card_list)) == expected


def test_get_num_cards(example_card_list) -> None:
    assert list(get_num_cards(example_card_list)) == [1, 2, 4, 8, 14, 1]


@pytest.mark.parametrize(
    "card_list_name, expected",
    [("example_card_list", 30), ("actual_card_list", 6874754)],
)
def test_card_num_sum(
    card_list_name: str, expected: int, request: pytest.FixtureRequest
) -> None:
    card_list = request.getfixturevalue(card_list_name)
    assert sum(get_num_cards(card_list)) == expected
