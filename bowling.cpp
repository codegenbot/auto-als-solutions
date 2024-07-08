```
#include <string>

int bowlingScore(string s) {
    int score = 0;
    int currentRoll = 0;
    bool spare = false;
    for (char c : s) {
        if (c == '/') {
            if (!spare) {
                score += 10 - (10 - currentRoll);
            }
            currentRoll = 0;
            spare = false;
        } else if (c == 'X') {
            score += 10;
            currentRoll = 0;
            spare = true;
        } else {
            currentRoll++;
            score += c - '0';
            if (currentRoll > 1) {
                spare = true;
            }
        }
    }
    return score;
}