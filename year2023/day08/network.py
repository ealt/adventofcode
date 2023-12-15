from typing import Iterable, Callable
import itertools
from collections import defaultdict

from node import Node
from loop_result import LoopResult


class Network:
    def __init__(self) -> None:
        self._nodes: defaultdict[str, Node] = defaultdict(Node)

    @property
    def nodes(self) -> Iterable[Node]:
        return self._nodes.values()

    def add_node(self, label: str, left: str, right: str) -> None:
        self._nodes[label].label = label
        self._nodes[label].left = self._nodes[left]
        self._nodes[label].right = self._nodes[right]

    def get_steps(
        self,
        is_start: Callable[[Node], bool],
        is_end: Callable[[Iterable[Node]], bool],
        directions: str,
    ) -> int:
        current = [node for node in self._nodes.values() if is_start(node)]
        visited = set()
        steps = 0
        for i, direction in itertools.cycle(enumerate(directions)):
            key = tuple([str(i), *[node.label for node in current]])
            if key in visited:
                RuntimeError(f"End condition is not reachable from start state")
            if is_end(current):
                return steps
            visited.add(key)
            if direction == "L":
                current = [node.left for node in current]
            elif direction == "R":
                current = [node.right for node in current]
            else:
                ValueError(f"Unknown direction: {direction}")
            steps += 1

    def get_loops(
        self,
        start: str,
        is_end: Callable[[Node], bool],
        directions: str,
    ) -> LoopResult:
        current = self._nodes[start]
        visited: dict[tuple[int, str], int] = {}
        steps = 0
        end_steps: list[int] = []
        for i, direction in itertools.cycle(enumerate(directions)):
            key = (i, current.label)
            if key in visited:
                return LoopResult(
                    loop_start=visited[key],
                    loop_length=steps - visited[key],
                    steps_to_ends=tuple(end_steps),
                )
            if is_end(current):
                end_steps.append(steps)
            visited[key] = steps
            if direction == "L":
                current = current.left
            elif direction == "R":
                current = current.right
            else:
                ValueError(f"Unknown direction: {direction}")
            steps += 1
