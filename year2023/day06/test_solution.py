import pytest
from solution import (
    get_num_ways_to_win,
    output_product,
    parse_record,
    parse_records,
    read_records,
)

EXAMPLE_RECORDS = """Time:      7  15   30
Distance:  9  40  200
"""


@pytest.fixture
def example_record_text() -> list[str]:
    return EXAMPLE_RECORDS


@pytest.fixture
def actual_record_text() -> list[str]:
    return read_records("input.txt")


def test_get_num_ways_to_win(example_record_text) -> None:
    records = parse_records(example_record_text)
    assert list(map(get_num_ways_to_win, records)) == [4, 8, 9]


@pytest.mark.parametrize(
    "record_text_name, expected",
    [("example_record_text", 288), ("actual_record_text", 219849)],
)
def test_winning_ways_product(
    record_text_name: str, expected: int, request: pytest.FixtureRequest
) -> None:
    record_text = request.getfixturevalue(record_text_name)
    records = parse_records(record_text)
    assert output_product(get_num_ways_to_win, records) == expected


@pytest.mark.parametrize(
    "record_text_name, expected",
    [("example_record_text", 71503), ("actual_record_text", 29432455)],
)
def test_get_num_ways_to_win_pt2(
    record_text_name: str, expected: int, request: pytest.FixtureRequest
) -> None:
    record_text = request.getfixturevalue(record_text_name)
    record = parse_record(record_text)
    assert get_num_ways_to_win(record) == expected
