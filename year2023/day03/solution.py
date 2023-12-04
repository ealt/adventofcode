import argparse
from typing import Sequence

from gear_finder import GearFinder
from part_finder import PartFinder


def read_schematic(filename: str) -> list[str]:
    with open(filename) as f:
        return [row.strip() for row in f.readlines()]


def get_part_numbers(schematic: Sequence[str]) -> list[int]:
    finder = PartFinder()
    finder.explore(schematic)
    return finder.part_numbers


def gear_ratio(part_numbers: list[int]) -> int:
    return part_numbers[0] * part_numbers[1]


def get_gear_ratios(schematic: Sequence[str]) -> list[int]:
    finder = GearFinder()
    finder.explore(schematic)
    return [gear_ratio(part_numbers) for part_numbers in finder.gears.values()]


def main(filename: str) -> None:
    schematic = read_schematic(filename)
    print(f"part number sum: {sum(get_part_numbers(schematic))}")
    print(f"gear ratio sum:  {sum(get_gear_ratios(schematic))}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Parses schematic.")
    parser.add_argument(
        "--input", help="The path to an input file.", default="input.txt"
    )
    args = parser.parse_args()
    main(args.input)
