#ifndef SOLUTION_H
#define SOLUTION_H

#include <string>
#include <vector>

std::vector<std::string> readInput(const std::string& filename);
int getPrioritySum(const std::vector<std::string>& rucksacks);
int getBadgeSum(std::vector<std::string>& rucksacks, int n);

#endif // SOLUTION_H