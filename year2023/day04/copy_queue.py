from collections import deque


class CopyQueue:
    def __init__(self):
        self._queue: deque[int] = deque([])

    def push(self, num_matches: int, num_cards: int) -> None:
        while len(self._queue) < num_matches:
            self._queue.append(0)
        for i in range(num_matches):
            self._queue[i] += num_cards

    def pop(self) -> int:
        if self._queue:
            return self._queue.popleft()
        return 0
