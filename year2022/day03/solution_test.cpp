#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN

#include <string>
#include <vector>

#include "doctest.h"
#include "solution.h"

std::vector<std::string> sampleRucksacks = {
    "vJrwpWtwJgWrhcsFMMfFFhFp",
    "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
    "PmmdzqPrVvPwwTWBwg",
    "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
    "ttgJtRGJQctTZtZT",
    "CrZsJsPPZsGzwwsLwLmpwMDw"
};


TEST_CASE("test readInput") {
    CHECK(readInput("sample_input.txt") == sampleRucksacks);
}

TEST_CASE("test getPrioritySum") {
    CHECK(getPrioritySum(sampleRucksacks) == 157);
    std::vector<std::string> rucksacks = readInput("input.txt");
    CHECK(getPrioritySum(rucksacks) == 8515);
}

TEST_CASE("test getBadgeSum") {
    CHECK(getBadgeSum(sampleRucksacks, 3) == 70);
    std::vector<std::string> rucksacks = readInput("input.txt");
    CHECK(getBadgeSum(rucksacks, 3) == 2434);
}
