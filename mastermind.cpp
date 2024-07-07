int getHint(string code, string guess) {
    int white = 0;
    int black = 0;

    // Count the correct colors at wrong places (white pegs)
    map<char, int> codeCount, guessCount;
    for (char c : code) {
        codeCount[c]++;
    }
    for (char c : guess) {
        guessCount[c]++;
    }
    for (int i = 0; i < 4; i++) {
        if (code[i] != guess[i]) {
            white += min(codeCount[code[i]], guessCount[guess[i]]);
        }
    }

    // Count the correct colors at correct places (black pegs)
    int blackPegs = 0;
    for (int i = 0; i < 4; i++) {
        if (code[i] == guess[i]) {
            black++;
        }
    }

    return white + black;
}