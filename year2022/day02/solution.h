#ifndef SOLUTION_H
#define SOLUTION_H

#include <string>
#include <tuple>
#include <vector>

enum move { ROCK, PAPER, SCISSORS, UNKNOWN };
std::vector<std::tuple<move, move> > readInput(const std::string& filename, bool part2 = false);
int getTotalScore(const std::vector<std::tuple<move, move> >& rounds);

#endif // SOLUTION_H