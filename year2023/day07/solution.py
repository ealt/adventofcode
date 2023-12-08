import argparse
from collections import Counter

from hand import Hand
from hand_type import HandType

DIGITS = set(str(digit) for digit in range(2, 10))
JOKER = 1


def read_hands(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def get_card_strength(card: str, include_jokers: bool = False) -> int:
    if card in DIGITS:
        return int(card)
    if card == "T":
        return 10
    if card == "J":
        return JOKER if include_jokers else 11
    if card == "Q":
        return 12
    if card == "K":
        return 13
    if card == "A":
        return 14
    raise ValueError(f"Unknown card: {card}")


def get_hand_type(cards: str) -> HandType:
    counts = Counter(cards)
    jokers = counts[JOKER]
    del counts[JOKER]
    count_values = list(sorted(counts.values(), reverse=True))
    if not count_values:
        count_values = [0]
    count_values[0] += jokers
    if count_values == [5]:
        return HandType.FIVE_OF_A_KIND
    if count_values == [4, 1]:
        return HandType.FOUR_OF_A_KIND
    if count_values == [3, 2]:
        return HandType.FULL_HOUSE
    if count_values == [3, 1, 1]:
        return HandType.THREE_OF_A_KIND
    if count_values == [2, 2, 1]:
        return HandType.TWO_PAIR
    if count_values == [2, 1, 1, 1]:
        return HandType.ONE_PAIR
    return HandType.HIGH_CARD


def parse_hands(hand_text: str, include_jokers: bool = False) -> list[Hand]:
    hands: list[Hand] = []
    for line in hand_text.splitlines():
        cards, bid = line.split()
        cards = tuple([get_card_strength(card, include_jokers) for card in cards])
        bid = int(bid)
        hand_type = get_hand_type(cards)
        hands.append(Hand(cards, bid, hand_type))
    return hands


def get_winnings(hands: list[Hand]) -> int:
    return sum(rank * hand.bid for rank, hand in enumerate(sorted(hands), start=1))


def main(filename: str) -> None:
    hand_text = read_hands(filename)
    hands = parse_hands(hand_text, include_jokers=False)
    print(f"Total winnings (without jokers): {get_winnings(hands)}")
    hands = parse_hands(hand_text, include_jokers=True)
    print(f"Total winnings (with jokers):    {get_winnings(hands)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate Camel Cards winnings.")
    parser.add_argument(
        "--input", help="The path to an input file.", default="input.txt"
    )
    args = parser.parse_args()
    main(args.input)
