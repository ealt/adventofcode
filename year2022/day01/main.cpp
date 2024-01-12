#include <iostream>
#include <vector>

#include "solution.h"

int main() {
    std::vector<std::vector<int> > values = readInput("input.txt");
    std::cout << getMaxSum(values) << std::endl;
    std::cout << getTopNSum(values, 3) << std::endl;

    return 0;
}
