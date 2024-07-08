```cpp
#include <string>
#include <vector>

using namespace std;

int bowlingScore(string s) {
    int score = 0;
    vector<int> rolls;

    for (char c : s) {
        if (c == 'X') {
            score += 10;
            rolls.push_back(10);
        } else if (c == '/') {
            score += 10 - (rolls[rolls.size() - 1] + 1);
            rolls.pop_back();
        } else {
            int roll = c - '0';
            if (rolls.size() >= 2) {
                if (rolls[rolls.size() - 1] + rolls[rolls.size() - 2] + 1 == 10) {
                    score += 10;
                    score += roll;
                } else {
                    score += roll;
                }
            } else {
                score += roll;
            }
            rolls.push_back(roll);
        }
    }

    return score;
}