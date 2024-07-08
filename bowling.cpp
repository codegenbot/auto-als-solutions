#include <string>

int bowlingScore(std::string s) {
    int score = 0;
    int currentRoll = 0;
    bool spareOrStrike = false;
    for (char c : s) {
        if (c == '/') {
            if (currentRoll < 2) {
                score += 10 - (10 - currentRoll);
            }
            currentRoll = 0;
        } else if (c == 'X') {
            score += 10;
            currentRoll = 0;
            spareOrStrike = true;
        } else {
            currentRoll++;
            if (c == '0' || c == '1' || c == '2' || c == '3' || c == '4' || c == '5' || c == '6' || c == '7' || c == '8' || c == '9') {
                score += c - '0';
            } else if (c == '+' && spareOrStrike) {
                score += 10;
                currentRoll = 0;
                spareOrStrike = false;
            }
        }
    }
    return score;