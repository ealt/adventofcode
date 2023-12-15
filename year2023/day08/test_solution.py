from solution import (
    read_network_map,
    parse_network,
    get_ghost_steps,
    get_ghost_steps_lcm,
    get_normal_steps,
)
import pytest
from network import Network
import functools

EXAMPLE_NETWORK_MAP_1 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)
"""

EXAMPLE_NETWORK_MAP_2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

EXAMPLE_NETWORK_MAP_3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""


@pytest.fixture
def example_network_1() -> tuple[str, str]:
    return tuple(EXAMPLE_NETWORK_MAP_1.split("\n\n"))


@pytest.fixture
def example_network_2() -> tuple[str, str]:
    return tuple(EXAMPLE_NETWORK_MAP_2.split("\n\n"))


@pytest.fixture
def example_network_3() -> tuple[str, str]:
    return tuple(EXAMPLE_NETWORK_MAP_3.split("\n\n"))


@pytest.fixture
def actual_network() -> tuple[str, str]:
    network_map_text = read_network_map("input.txt")
    return tuple(network_map_text.split("\n\n"))


@pytest.mark.parametrize(
    "network_name, expected",
    [("example_network_1", 2), ("example_network_2", 6), ("actual_network", 17287)],
)
def test_get_normal_steps(
    network_name: str, expected: int, request: pytest.FixtureRequest
) -> None:
    directions, network_map = request.getfixturevalue(network_name)
    network = parse_network(network_map)
    assert get_normal_steps(network, directions) == expected


def test_get_ghost_steps(example_network_3: tuple[str, str]) -> None:
    directions, network_map = example_network_3
    network = parse_network(network_map)
    assert get_ghost_steps(network, directions) == 6


def test_get_ghost_steps_lcm(actual_network: tuple[str, str]) -> None:
    directions, network_map = actual_network
    network = parse_network(network_map)
    get_ghost_steps_lcm(network, directions) == 18625484023687
