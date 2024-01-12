#ifndef SOLUTION_H
#define SOLUTION_H

#include <string>
#include <vector>

std::vector<std::vector<int> > readInput(const std::string& filename);
int getMaxSum(const std::vector<std::vector<int> >& values);
int getTopNSum(const std::vector<std::vector<int> >& values, int n);

#endif // SOLUTION_H