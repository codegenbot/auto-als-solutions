#include <string>

int bowlingScore(std::string s) {
    int score = 0;
    int currentRoll = 0;
    bool strike = false;

    for (char c : s) {
        if (c == 'X') {
            score += 10 + (strike ? 10 : currentRoll);
            strike = true;
            currentRoll = 0;
        } else if (c == '/') {
            score += 10 - currentRoll;
            strike = false;
            currentRoll = 0;
        } else {
            int roll = c - '0';
            if (strike) {
                score += roll;
                strike = false;
            } else {
                currentRoll += roll;
            }
        }
    }

    return score;
}