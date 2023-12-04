from collections import defaultdict
from typing import DefaultDict, Iterable, Optional


class Node:
    def __init__(self):
        self.terminal: bool = True
        self.children: DefaultDict[str, Node] = defaultdict(Node)


class Trie:
    def __init__(self, inputs: Optional[Iterable[str]] = None):
        self.root = Node()
        if inputs:
            for input in inputs:
                self.add(input)

    def add(self, input: str) -> None:
        node = self.root
        for char in input:
            node.terminal = False
            node = node.children[char]

    def first_prefix(self, query: str) -> str:
        node = self.root
        prefix = []
        for char in query:
            if node.terminal:
                return "".join(prefix)
            if char in node.children:
                prefix.append(char)
                node = node.children[char]
            else:
                return ""
        return "".join(prefix) if node.terminal else ""
