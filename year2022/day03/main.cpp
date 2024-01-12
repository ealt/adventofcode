#include <iostream>
#include <string>
#include <vector>

#include "solution.h"

int main() {
    std::vector<std::string> rucksacks = readInput("input.txt");
    std::cout << getPrioritySum(rucksacks) << std::endl;
    std::cout << getBadgeSum(rucksacks, 3) << std::endl;

    return 0;
}
