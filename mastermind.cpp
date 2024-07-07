int mastermind(string code, string guess) {
    int white = 0;
    int black = 0;
    vector<char> codeVec(code.begin(), code.end());
    vector<char> guessVec(guess.begin(), guess.end());

    for (int i = 0; i < 4; ++i) {
        if (codeVec[i] == guessVec[i]) {
            --guessVec.end();
            ++black;
        }
    }

    for (char c : codeVec) {
        int count = 0;
        for (char d : guessVec) {
            if (c == d) {
                ++count;
            }
        }
        white += min(count, 1);
    }

    return black + white - black;
}