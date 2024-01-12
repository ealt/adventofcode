#include <algorithm>
#include <filesystem>
#include <fstream>
#include <iostream>
#include <numeric>
#include <map>
#include <string>
#include <tuple>
#include <vector>

#include "solution.h"

enum outcome { WIN, LOSS, DRAW };

std::map<std::tuple<move, move>, outcome> outcomeMap {
    {std::make_tuple(ROCK, ROCK), DRAW},
    {std::make_tuple(ROCK, PAPER), WIN},
    {std::make_tuple(ROCK, SCISSORS), LOSS},
    {std::make_tuple(PAPER, ROCK), LOSS},
    {std::make_tuple(PAPER, PAPER), DRAW},
    {std::make_tuple(PAPER, SCISSORS), WIN},
    {std::make_tuple(SCISSORS, ROCK), WIN},
    {std::make_tuple(SCISSORS, PAPER), LOSS},
    {std::make_tuple(SCISSORS, SCISSORS), DRAW}
};

std::map<std::tuple<move, outcome>, move> moveMap {
    {std::make_tuple(ROCK, WIN), PAPER},
    {std::make_tuple(ROCK, LOSS), SCISSORS},
    {std::make_tuple(ROCK, DRAW), ROCK},
    {std::make_tuple(PAPER, WIN), SCISSORS},
    {std::make_tuple(PAPER, LOSS), ROCK},
    {std::make_tuple(PAPER, DRAW), PAPER},
    {std::make_tuple(SCISSORS, WIN), ROCK},
    {std::make_tuple(SCISSORS, LOSS), PAPER},
    {std::make_tuple(SCISSORS, DRAW), SCISSORS}
};

move getOpponentMove(char code) {
    switch (code) {
        case 'A':
            return ROCK;
        case 'B':
            return PAPER;
        case 'C':
            return SCISSORS;
    }
    return UNKNOWN;
}

move getOwnMove1(char code) {
    switch (code) {
        case 'X':
            return ROCK;
        case 'Y':
            return PAPER;
        case 'Z':
            return SCISSORS;
    }
    return UNKNOWN;
}

move getOwnMove2(move opponentMove, char code) {
    outcome desiredOutcome;
    switch (code) {
        case 'X':
            desiredOutcome = LOSS;
            break;
        case 'Y':
            desiredOutcome = DRAW;
            break;
        case 'Z':
            desiredOutcome = WIN;
            break;
    }
    return moveMap[std::make_tuple(opponentMove, desiredOutcome)];
}

std::vector<std::tuple<move, move> > readInput(const std::string& filename, bool part2) {
    std::vector<std::tuple<move, move> > rounds;
    std::filesystem::path currentPath = std::filesystem::current_path() / "../year2022/day02";
    std::ifstream file(currentPath / filename);
    if (!file.is_open()) {
        std::cerr << "Error opening file: " << currentPath / filename << std::endl;
        return rounds;
    }
    
    char code1, code2;
    while (file >> code1 >> code2) {
        move opponentMove = getOpponentMove(code1);
        move ownMove = part2 ? getOwnMove2(opponentMove, code2) : getOwnMove1(code2);
        rounds.emplace_back(opponentMove, ownMove);
    }
    
    file.close();
    return rounds;
}

int getSelectionScore(move selection) {
    switch (selection) {
        case ROCK:
            return 1;
        case PAPER:
            return 2;
        case SCISSORS:
            return 3;
    }
    return 0;
}

int getOutcomeScore(const std::tuple<move, move>& round) {
    switch (outcomeMap[round]) {
        case WIN:
            return 6;
        case LOSS:
            return 0;
        case DRAW:
            return 3;
    }
    return 0;
}

int getScore(const std::tuple<move, move>& round) {
    return getSelectionScore(std::get<1>(round)) + getOutcomeScore(round);
}

int getTotalScore(const std::vector<std::tuple<move, move> >& rounds) {
    int totalScore = 0;
    for (const auto& round : rounds) {
        totalScore += getScore(round);
    }
    return totalScore;
}
