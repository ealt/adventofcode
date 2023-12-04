import argparse
import re
from typing import Iterable, Iterator

from copy_queue import CopyQueue

NUMBER_LIST_PATTERN = rf"\d+(?:\s+\d+)*"
CARD_PATTERN = rf"Card\s+(?P<id>\d+):\s*(?P<winning_numbers>{NUMBER_LIST_PATTERN})\s*\|\s*(?P<your_numbers>{NUMBER_LIST_PATTERN})"


def read_card_list(filename: str) -> list[str]:
    with open(filename) as f:
        return f.readlines()


def parse_numbers(number_list: str) -> set[int]:
    return set(map(int, number_list.split()))


def get_num_matches(card: str) -> set[int]:
    m = re.match(CARD_PATTERN, card)
    if not m:
        raise ValueError(f'"{card}" does not match expected pattern.')
    winning_numbers = parse_numbers(m.group("winning_numbers"))
    your_numbers = parse_numbers(m.group("your_numbers"))
    matches = winning_numbers & your_numbers
    return len(matches)


def get_points(card: str) -> int:
    if num_matches := get_num_matches(card):
        return 2 ** (num_matches - 1)
    return 0


def get_num_cards(card_list: Iterable[str]) -> Iterator[int]:
    copy_queue = CopyQueue()
    for card in card_list:
        copies = copy_queue.pop()
        num_cards = copies + 1
        yield num_cards
        num_matches = get_num_matches(card)
        copy_queue.push(num_matches, num_cards)


def main(filename: str) -> None:
    card_list = read_card_list(filename)
    print(f"total points: {sum(map(get_points, card_list))}")
    print(f"total cards:  {sum(get_num_cards(card_list))}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Evaluate scratchcard winnings.")
    parser.add_argument(
        "--input", help="The path to an input file.", default="input.txt"
    )
    args = parser.parse_args()
    main(args.input)
