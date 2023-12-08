import bisect
import itertools
from collections.abc import ItemsView, Iterator, KeysView, Mapping, ValuesView
from typing import Any

from range import Range


class RangeMap(Mapping):
    @staticmethod
    def get_lower_bound(item: tuple[Range, Any]) -> int:
        return item[0].start

    def __init__(self, items: list[tuple[Range, Any]]) -> None:
        self._items = sorted(items, key=RangeMap.get_lower_bound)
        self._validate_ranges()

    def __getitem__(self, __key: int) -> Any:
        _, value = self._get_item(__key)
        return value

    def __iter__(self) -> Iterator:
        self.__i = 0
        return self

    def __next__(self) -> tuple[Range, Any]:
        if self.__i < len(self):
            return self._items[self.__i]
        raise StopIteration

    def __len__(self) -> int:
        return len(self._items)

    def __contains__(self, key: int) -> bool:
        try:
            _ = self._get_item(key)
        except KeyError:
            return False
        return True

    def keys(self) -> KeysView:
        for range, _ in self._items:
            yield range

    def items(self) -> ItemsView:
        for item in self._items:
            yield item

    def values(self) -> ValuesView:
        for _, value in self._items:
            yield value

    def get(self, key: int, value: Any) -> Any:
        if key in self:
            return self[key]
        return value

    def __eq__(self, __other: object) -> bool:
        if not isinstance(__other, self.__class__):
            return False
        return self._items == __other._items

    def __ne__(self, __value: object) -> bool:
        return not (self == __value)

    def __str__(self) -> str:
        return f"{self.__class__}({str(self._items)})"

    def __repr__(self) -> str:
        return str(self)

    def _get_item(self, __key: int) -> tuple[Range, Any]:
        index = bisect.bisect_right(self._items, __key, key=RangeMap.get_lower_bound)
        if index == 0:
            raise KeyError
        item = self._items[index - 1]
        if item[0].start <= __key < item[0].start + item[0].length:
            return item
        raise KeyError

    def _validate_ranges(self) -> None:
        for left, right in itertools.pairwise(self._items):
            # for left, right in zip(self._items, self._items[1:]):
            if left[0].start + left[0].length >= right[0].start:
                raise ValueError(f"Overlapping ranges: {left[0]}, {right[0]}")
