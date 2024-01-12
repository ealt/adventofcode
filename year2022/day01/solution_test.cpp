#define DOCTEST_CONFIG_IMPLEMENT_WITH_MAIN

#include <vector>

#include "doctest.h"
#include "solution.h"

std::vector<std::vector<int> > sampleValues = {
    {1000, 2000, 3000},
    {4000},
    {5000, 6000},
    {7000, 8000, 9000},
    {10000}
};


TEST_CASE("test readInput") {
    CHECK(readInput("sample_input.txt") == sampleValues);
}

TEST_CASE("test maxSum") {
    CHECK(getMaxSum(sampleValues) == 24000);
    std::vector<std::vector<int> > values = readInput("input.txt");
    CHECK(getMaxSum(values) == 69177);
}

TEST_CASE("test getTopNSum") {
    CHECK(getTopNSum(sampleValues, 3) == 45000);
    std::vector<std::vector<int> > values = readInput("input.txt");
    CHECK(getTopNSum(values, 3) == 207456);
}
