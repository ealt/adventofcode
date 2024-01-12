#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN

#include <tuple>
#include <vector>

#include "doctest.h"
#include "solution.h"

std::vector<std::tuple<move, move> > sampleRounds1 = {
    std::make_tuple(ROCK, PAPER),
    std::make_tuple(PAPER, ROCK),
    std::make_tuple(SCISSORS, SCISSORS)
};

std::vector<std::tuple<move, move> > sampleRounds2 = {
    std::make_tuple(ROCK, ROCK),
    std::make_tuple(PAPER, ROCK),
    std::make_tuple(SCISSORS, ROCK)
};


TEST_CASE("test readInput") {
    CHECK(readInput("sample_input.txt") == sampleRounds1);
    CHECK(readInput("sample_input.txt", true) == sampleRounds2);
}

TEST_CASE("test getTotalScore") {
    CHECK(getTotalScore(sampleRounds1) == 15);
    std::vector<std::tuple<move, move> > rounds = readInput("input.txt");
    CHECK(getTotalScore(rounds) == 9759);

    CHECK(getTotalScore(sampleRounds2) == 12);
    rounds = readInput("input.txt", true);
    CHECK(getTotalScore(rounds) == 12429);
}
