int bowlingScore(string s) {
    int score = 0;
    int roll = 0;
    for (char c : s) {
        if (c == 'X') {
            score += 30;
            roll = 1;
        } else if (c == '/') {
            score += (10 - roll);
            roll = 0;
        } else if (isdigit(c)) {
            int strike = c - '0';
            score += strike;
            if (roll > 0) score += strike;
            roll++;
        }
    }
    return score;
}