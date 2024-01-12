#include <algorithm>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <numeric>
#include <string>
#include <vector>

#include "solution.h"

std::vector<std::vector<int> > readInput(const std::string& filename) {
    std::vector<std::vector<int> > values;
    std::filesystem::path currentPath = std::filesystem::current_path() / "../year2022/day01";
    std::ifstream file(currentPath / filename);
    if (!file.is_open()) {
        std::cerr << "Error opening file: " << currentPath / filename << std::endl;
        return values;
    }
    
    std::string line;
    while (std::getline(file, line)) {
        std::vector<int> row;
        row.push_back(std::stoi(line));
        while (std::getline(file, line)) {
            if (line == "") break;
            row.push_back(std::stoi(line));
        }
        values.push_back(row);
    }
    
    file.close();
    return values;
}

int getMaxSum(const std::vector<std::vector<int> >& values) {
    int maxSum = 0;
    for (const auto& row : values) {
        int rowSum = std::accumulate(row.begin(), row.end(), 0);
        maxSum = std::max(maxSum, rowSum);
    }
    return maxSum;
}

int getTopNSum(const std::vector<std::vector<int> >& values, int n) {
    if (values.size() < n) {
        std::cerr << "Size of values " << values.size() << " is less than " << n << std::endl;
        return 0;
    }
    std::vector<int> rowSums;
    for (const auto& row : values) {
        int rowSum = std::accumulate(row.begin(), row.end(), 0);
        rowSums.push_back(rowSum);
    }
    std::partial_sort(rowSums.begin(), rowSums.begin() + n, rowSums.end(), std::greater<int>());
    return std::accumulate(rowSums.begin(), rowSums.begin() + n, 0);
}
