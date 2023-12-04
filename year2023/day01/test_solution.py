import pytest
from solution import get_calibration, read_calibration_document

EXAMPLE_DOCUMENT_1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

EXAMPLE_DOCUMENT_2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""


@pytest.fixture
def example_document_1() -> list[str]:
    return EXAMPLE_DOCUMENT_1.splitlines()


@pytest.fixture
def example_document_2() -> list[str]:
    return EXAMPLE_DOCUMENT_2.splitlines()


@pytest.fixture
def actual_document() -> list[str]:
    return read_calibration_document("input.txt")


@pytest.mark.parametrize(
    "document_name, parse_written, expected",
    [
        ("example_document_1", False, [12, 38, 15, 77]),
        ("example_document_2", True, [29, 83, 13, 24, 42, 14, 76]),
    ],
)
def test_get_calibration(
    document_name: str,
    parse_written: bool,
    expected: list[int],
    request: pytest.FixtureRequest,
):
    calibration_document = request.getfixturevalue(document_name)
    assert [
        get_calibration(line, parse_written) for line in calibration_document
    ] == expected


@pytest.mark.parametrize(
    "document_name, parse_written, expected",
    [
        ("example_document_1", False, 142),
        ("actual_document", False, 54877),
        ("example_document_2", True, 281),
        ("actual_document", True, 54100),
    ],
)
def test_calibration_sum(
    document_name: str,
    parse_written: bool,
    expected: int,
    request: pytest.FixtureRequest,
):
    calibration_document = request.getfixturevalue(document_name)
    assert (
        sum(get_calibration(line, parse_written) for line in calibration_document)
        == expected
    )
