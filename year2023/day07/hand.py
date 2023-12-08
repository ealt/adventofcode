from typing import NamedTuple

from hand_type import HandType


class Hand(NamedTuple):
    cards: tuple[int, int, int, int, int]
    bid: int
    type: HandType

    def __lt__(self, other: "Hand") -> bool:
        if not isinstance(other, self.__class__):
            raise TypeError(
                f"Cannot compare types {self.__class__} and {other.__class__}"
            )
        if self.type.value < other.type.value:
            return True
        if self.type.value > other.type.value:
            return False
        for s, o in zip(self.cards, other.cards):
            if s < o:
                return True
            if s > o:
                return False
        return False

    def __le__(self, other: "Hand") -> bool:
        if not isinstance(other, self.__class__):
            raise TypeError(
                f"Cannot compare types {self.__class__} and {other.__class__}"
            )
        if self.type.value < other.type.value:
            return True
        if self.type.value > other.type.value:
            return False
        for s, o in zip(self.cards, other.cards):
            if s < o:
                return True
            if s > o:
                return False
        return True

    def __gt__(self, other: "Hand") -> bool:
        if not isinstance(other, self.__class__):
            raise TypeError(
                f"Cannot compare types {self.__class__} and {other.__class__}"
            )
        if self.type.value > other.type.value:
            return True
        if self.type.value < other.type.value:
            return False
        for s, o in zip(self.cards, other.cards):
            if s > o:
                return True
            if s < o:
                return False
        return False

    def __ge__(self, other: "Hand") -> bool:
        if not isinstance(other, self.__class__):
            raise TypeError(
                f"Cannot compare types {self.__class__} and {other.__class__}"
            )
        if self.type.value > other.type.value:
            return True
        if self.type.value < other.type.value:
            return False
        for s, o in zip(self.cards, other.cards):
            if s > o:
                return True
            if s < o:
                return False
        return False

    def __eq__(self, other: "Hand") -> bool:
        if not isinstance(other, self.__class__):
            raise TypeError(
                f"Cannot compare types {self.__class__} and {other.__class__}"
            )
        if self.type.value != other.type.value:
            return False
        for s, o in zip(self.cards, other.cards):
            if s != o:
                return False
        return True

    def __ne__(self, other: "Hand") -> bool:
        return not (self == other)
