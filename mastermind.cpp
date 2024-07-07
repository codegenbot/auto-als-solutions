#include <vector>
#include <iostream>
#include <string>

int mastermind(string code, string guess) {
    int white = 0;
    int black = 0;
    vector<char> codeVec(code.begin(), code.end());
    vector<char> guessVec(guess.begin(), guess.end());

    for (int i = 0; i < 4; i++) {
        if (codeVec[i] == guessVec[i]) {
            black++;
            codeVec[i] = '\0';
            guessVec[i] = '\0';
        }
    }

    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (codeVec[j] == guessVec[i] && codeVec[j] != '\0' && guessVec[i] != '\0') {
                white++;
                codeVec[j] = '\0';
                break;
            }
        }
    }

    return {black, white};
}