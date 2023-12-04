import argparse
import functools
import operator
import re
from collections import Counter
from typing import Iterable, Iterator

COUNT_PATTERN = rf"(\d+) (red|green|blue)"
REVEAL_PATTERN = rf"{COUNT_PATTERN}(?:, {COUNT_PATTERN})*"
GAME_PATTERN = rf"Game (?P<id>\d+): {REVEAL_PATTERN}(?:; {REVEAL_PATTERN})*"

THRESHOLDS = Counter({"red": 12, "green": 13, "blue": 14})


def read_game_records(filename: str) -> list[str]:
    with open(filename) as f:
        return f.readlines()


def get_reveal_counts(reveal: str) -> Counter[str, int]:
    counts: Counter[str, int] = Counter()
    for count in re.finditer(COUNT_PATTERN, reveal):
        color = count.group(2)
        quantity = int(count.group(1))
        counts[color] = quantity
    return counts


def get_max_counts(game_record: str) -> Counter[str, int]:
    max_counts: Counter[str, int] = Counter()
    for reveal in re.finditer(REVEAL_PATTERN, game_record):
        counts = get_reveal_counts(reveal.group())
        max_counts |= counts
    return max_counts


def is_possible(game_record: str) -> bool:
    max_counts = get_max_counts(game_record)
    for color, max_count in max_counts.items():
        if color in THRESHOLDS and max_count > THRESHOLDS[color]:
            return False
    return True


def get_possible_ids(game_records: Iterable[str]) -> Iterator[int]:
    for line in game_records:
        match = re.match(GAME_PATTERN, line)
        if match and is_possible(line):
            id = int(match.group("id"))
            yield id


def get_power(game_records: str) -> int:
    max_counts = get_max_counts(game_records)
    power = functools.reduce(operator.mul, max_counts.values())
    return power


def main(filename: str) -> None:
    game_records = read_game_records(filename)
    print(f"possible id sum: {sum(get_possible_ids(game_records))}")
    print(f"power sum:       {sum(map(get_power, game_records))}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyzes game records.")
    parser.add_argument(
        "--input", help="The path to an input file.", default="input.txt"
    )
    args = parser.parse_args()
    main(args.input)
