import argparse
import string
from collections import deque
from typing import Optional

from trie import Trie

DIGITS = set(string.digits)

# Note: "zero" is not specified as a valid digit
WRITTEN_DIGITS = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

WRITTEN_VALUES = {
    name: str(value) for value, name in enumerate(WRITTEN_DIGITS, start=1)
}

TRIE = Trie(WRITTEN_DIGITS)
REVERSED_TRIE = Trie([name[::-1] for name in WRITTEN_DIGITS])


def read_calibration_document(filename: str) -> list[str]:
    with open(filename) as f:
        return f.readlines()


def get_written_prefix(chars: list[str], reversed: Optional[bool] = False) -> str:
    trie = REVERSED_TRIE if reversed else TRIE
    prefix = trie.first_prefix(chars)
    if not prefix:
        return prefix
    if reversed:
        prefix = prefix[::-1]
    return WRITTEN_VALUES[prefix]


def get_first_digit(
    line: str, parse_written: bool, reversed: Optional[bool] = False
) -> str:
    if reversed:
        line = line[::-1]
    chars = deque(line)
    while chars:
        if chars[0] in DIGITS:
            return chars[0]
        if parse_written and (digit := get_written_prefix(chars, reversed)):
            return digit
        chars.popleft()
    raise ValueError(f"No digit found in {line}")


def get_calibration(line: str, parse_written: Optional[bool] = False) -> int:
    first_digit = get_first_digit(line, parse_written, reversed=False)
    last_digit = get_first_digit(line, parse_written, reversed=True)
    return int(first_digit + last_digit)


def main(filename: str) -> None:
    calibration_document = read_calibration_document(filename)
    print(
        f"calibration sum (digits only):           {sum(get_calibration(line, parse_written=False) for line in calibration_document)}"
    )
    print(
        f"calibration sum (written values parsed): {sum(get_calibration(line, parse_written=True) for line in calibration_document)}"
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extracts calibration values.")
    parser.add_argument(
        "--input", help="The path to an input file.", default="input.txt"
    )
    args = parser.parse_args()
    main(args.input)
