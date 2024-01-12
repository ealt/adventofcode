#include <algorithm>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <set>
#include <string>
#include <vector>

#include "solution.h"

std::vector<std::string> readInput(const std::string& filename) {
    std::vector<std::string> rucksacks;
    std::filesystem::path currentPath = std::filesystem::current_path() / "../year2022/day03";
    std::ifstream file(currentPath / filename);
    if (!file.is_open()) {
        std::cerr << "Error opening file: " << currentPath / filename << std::endl;
        return rucksacks;
    }
    
    std::string line;
    while (std::getline(file, line)) {
        rucksacks.push_back(line);
    }
    
    file.close();
    return rucksacks;
}

// Assumes rucksack.size() is even
// and two halves of string have exactly one character in common
char getIntersection(const std::string& rucksack) {
    auto middle = rucksack.begin() + (rucksack.size() / 2);
    auto it = std::find_first_of(rucksack.begin(), middle, middle, rucksack.end());
    if (it == middle) {
        std::cerr << "No overlap found" << std::endl;
        return ' ';
    }
    return *it;
}

int getValue(char c) {
    if ('a' <= c && c <= 'z') {
        return static_cast<int>(c - 'a') + 1;
    }
    if ('A' <= c && c <= 'Z') {
        return static_cast<int>(c - 'A') + 27;
    }
    return 0;
}

int getPrioritySum(const std::vector<std::string>& rucksacks) {
    int prioritySum = 0;
    for (const auto& rucksack : rucksacks) {
        char c = getIntersection(rucksack);
        prioritySum += getValue(c);
    }
    return prioritySum;
}

std::set<char> getIntersecion(const std::vector<std::string>::iterator& it, int n) {
    if (n < 2) {
        return {};
    }
    std::vector<char> currentIntersection(it->begin(), it->end());
    std::vector<char> updatedIntersection;
    for (int i = 1; i < n; i++) {
        // set_intersection requires the input iterators to be sorted
        std::sort((it + i)->begin(), (it + i)->end());
        std::sort(currentIntersection.begin(), currentIntersection.end());
        auto end = std::set_intersection(
            (it + i)->begin(), (it + i)->end(),
            currentIntersection.begin(), currentIntersection.end(),
            std::inserter(updatedIntersection, updatedIntersection.begin())
        );
        currentIntersection.swap(updatedIntersection);
        updatedIntersection.clear();
    }
    // set_intersection can return duplicate elements
    return std::set<char>(currentIntersection.begin(), currentIntersection.end());;
}

int getBadgeValue(const std::vector<std::string>::iterator& it, int n) {
    std::set<char> intersection = getIntersecion(it, n);
    if (intersection.size() != 1) {
        std::cerr << "Overap of " << intersection.size() << " found" << std::endl;
        return 0;
    }
    return getValue(*intersection.begin());
}

int getBadgeSum(std::vector<std::string>& rucksacks, int n) {
    if (rucksacks.size() % n != 0) {
        std::cerr << rucksacks.size() << " cannot be evenly divided into groups of " << n << std::endl;
        return 0;
    }
    int badgeSum = 0;
    for (auto it = rucksacks.begin(); it < rucksacks.end(); std::advance(it, n)) {
        badgeSum += getBadgeValue(it, n);
    }
    return badgeSum;
}
