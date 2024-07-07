int mastermind(string code, string guess) {
    int white = 0;
    int black = 0;

    vector<int> codeCount(6, 0);
    vector<int> guessCount(6, 0);

    for (int i = 0; i < 4; i++) {
        if (code[i] == guess[i]) {
            black++;
            codeCount[code[i] - 'A']++;
            guessCount[guess[i] - 'A']++;
        } else {
            int j;
            for (j = 0; j < 6; j++) {
                if (code[i] != guess[j] && codeCount[j] < guessCount[j]) {
                    break;
                }
            }
            if (j < 6) {
                white++;
                codeCount[code[i] - 'A']++;
                guessCount[guess[j] - 'A']++;
            } else {
                black++;
                codeCount[code[i] - 'A']++;
                guessCount[guess[i] - 'A']++;
            }
        }
    }

    return make_tuple(white, black);
}