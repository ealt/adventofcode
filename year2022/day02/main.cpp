#include <iostream>
#include <tuple>
#include <vector>

#include "solution.h"

int main() {
    std::vector<std::tuple<move, move> > rounds = readInput("input.txt");
    std::cout << getTotalScore(rounds) << std::endl;
    rounds = readInput("input.txt", true);
    std::cout << getTotalScore(rounds) << std::endl;

    return 0;
}
