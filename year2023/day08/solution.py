import argparse
from network import Network
import re
from typing import Iterable
import functools
import math

from node import Node

NODE_PATTERN = rf"[0-9A-Z]{{2}}[A-Z]"
MAP_LINE_PATTERN = rf"(?P<label>{NODE_PATTERN}) = \((?P<left>{NODE_PATTERN}), (?P<right>{NODE_PATTERN})\)"


def read_network_map(filename: str) -> str:
    with open(filename) as f:
        return f.read()


def parse_network(network_map: str) -> Network:
    network = Network()
    for line in network_map.splitlines():
        m = re.match(MAP_LINE_PATTERN, line)
        if m:
            network.add_node(m.group("label"), m.group("left"), m.group("right"))
        else:
            raise ValueError(f"Unrecognized line: {line}")
    return network


def label_equals(label: str, node: Node) -> bool:
    return node.label == label


def all_labels_equal(label: str, nodes: Iterable[Node]) -> bool:
    return all(label_equals(label, node) for node in nodes)


def label_ends_with(letter: str, node: Node) -> bool:
    return node.label[-1] == letter


def all_labels_end_with(letter: str, nodes: Iterable[Node]) -> bool:
    return all(label_ends_with(letter, node) for node in nodes)


def get_normal_steps(network: Network, directions: str) -> int:
    equals_AAA = functools.partial(label_equals, "AAA")
    equal_ZZZ = functools.partial(all_labels_equal, "ZZZ")
    return network.get_steps(
        is_start=equals_AAA,
        is_end=equal_ZZZ,
        directions=directions,
    )


# Too slow for large input
def get_ghost_steps(network: Network, directions: str) -> int:
    ends_with_A = functools.partial(label_ends_with, "A")
    end_with_Z = functools.partial(all_labels_end_with, "Z")
    return network.get_steps(
        is_start=ends_with_A,
        is_end=end_with_Z,
        directions=directions,
    )


# Assumes all paths from starting points contain exactly one end point
# and each of those end points is in a loop
# at exactly the number of steps from the start as the loop length
def get_ghost_steps_lcm(network: Network, directions: str) -> int:
    ends_with_A = functools.partial(label_ends_with, "A")
    ends_with_Z = functools.partial(label_ends_with, "Z")
    results = [
        network.get_loops(start=node.label, is_end=ends_with_Z, directions=directions)
        for node in network.nodes
        if ends_with_A(node)
    ]
    assert all(len(result.steps_to_ends) == 1 for result in results)
    assert all(result.steps_to_ends[0] == result.loop_length for result in results)
    return math.lcm(*[result.loop_length for result in results])


def main(filename: str) -> None:
    network_map_text = read_network_map(filename)
    directions, network_map = network_map_text.split("\n\n")
    network = parse_network(network_map)
    print(f"Number of steps (normal): {get_normal_steps(network, directions)}")
    print(f"Number of steps (ghost):  {get_ghost_steps_lcm(network, directions)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TODO.")
    parser.add_argument(
        "--input", help="The path to an input file.", default="input.txt"
    )
    args = parser.parse_args()
    main(args.input)
