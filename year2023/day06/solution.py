import argparse
import functools
import math
import operator
from typing import Any, Callable, Iterable, Iterator, Sequence

from record import Record


def read_records(filename: str) -> list[str]:
    with open(filename) as f:
        return f.read()


def parse_row_values(row: str) -> Iterator[int]:
    return map(int, row.split()[1:])


def parse_row_value(row: str) -> int:
    return int("".join(row.split()[1:]))


def parse_records(record_text: str) -> Iterator[Record]:
    for time, distance in zip(*map(parse_row_values, record_text.splitlines())):
        yield Record(time, distance)


def parse_record(record_text: str) -> Record:
    return Record(*map(parse_row_value, record_text.splitlines()))


def get_max_charge(record: Record) -> float:
    """
    x(t-x) > d
    x^2 - t*x + d < 0
    """
    return 0.5 * (record.time + math.sqrt(record.time**2 - 4 * record.distance))


def get_num_ways_to_win(record: Record) -> int:
    opt_charge = record.time / 2  # optimum time
    max_charge = get_max_charge(record)  # breakeven point to tie record distance
    low = int(math.floor(opt_charge + 1))  # minimum discrete charge over the optimum
    high = int(math.ceil(max_charge - 1))  # maximum discrete charge (must win, not tie)
    num_ways = 2 * (high - low + 1)  # num discrete ways above and below optimum
    if record.time % 2 == 0:  # optimum is a valid discrete value
        num_ways += 1
    return num_ways


def output_product(f: Callable[[Any], int], input: Iterable[Any]) -> int:
    return functools.reduce(operator.mul, map(f, input), 1)


def main(filename: str) -> None:
    record_text = read_records(filename)
    records = parse_records(record_text)
    print(f"Ways to win (product): {output_product(get_num_ways_to_win, records)}")
    record = parse_record(record_text)
    print(f"Ways to win (single):  {get_num_ways_to_win(record)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Optimize boat races.")
    parser.add_argument(
        "--input", help="The path to an input file.", default="input.txt"
    )
    args = parser.parse_args()
    main(args.input)
