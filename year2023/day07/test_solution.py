import pytest
from solution import get_winnings, parse_hands, read_hands

EXAMPLE_HANDS = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""


@pytest.fixture
def example_hands() -> str:
    return EXAMPLE_HANDS


@pytest.fixture
def actual_hands() -> str:
    return read_hands("input.txt")


@pytest.mark.parametrize(
    "hands_name, include_jokers, expected",
    [
        ("example_hands", False, 6440),
        ("actual_hands", False, 250946742),
        ("example_hands", True, 5905),
        ("actual_hands", True, 251824095),
    ],
)
def test_get_winnings(
    hands_name: str, include_jokers: bool, expected: int, request: pytest.FixtureRequest
) -> None:
    hand_text = request.getfixturevalue(hands_name)
    hands = parse_hands(hand_text, include_jokers)
    assert get_winnings(hands) == expected
