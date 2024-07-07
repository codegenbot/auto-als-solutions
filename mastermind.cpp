#include <string>

int mastermind(string code, string guess) {
    int white = 0;
    int black = 0;

    for (int i = 0; i < 4; i++) {
        if (code[i] == guess[i]) {
            black++;
        } else {
            bool found = false;
            for (int j = 0; j < 4; j++) {
                if (guess[i] == code[j] && !found) {
                    found = true;
                }
            }
            if (!found) white++;
        }
    }

    return black + white;
}