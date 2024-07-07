#include <algorithm>
#include <cctype>

int bowlingScore(const string& input) {
    int score = 0;
    int roll1, roll2, prevRolls = 0;

    for (char c : input.begin(), input.end()) {
        if (c == '/') {
            score += std::min(10, prevRolls);
            prevRolls = 0;
        } else if (std::isdigit(c)) {
            prevRolls *= 10;
            prevRolls += c - '0';
        } else { // X
            score += 10;
            prevRolls = 0;
        }
    }

    if (prevRolls > 0) {
        score += std::min(10, prevRolls);
    }

    return score;
}