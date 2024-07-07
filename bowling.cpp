int bowlingScore(string s) {
    int score = 0;
    for (int i = 0; i < 10; i++) {
        if (s[i] == 'X') {
            score += 30;
        } else if (isdigit(s[i])) {
            int roll1 = s[i] - '0';
            if (i < 8 && (s[i + 1] == 'X' || s[i + 2] == 'X')) {
                score += 10 + roll1;
            } else if (i >= 8) {
                score += 10 + roll1;
            } else if (isdigit(s[i + 1])) {
                int roll2 = s[i + 1] - '0';
                if (s[i + 2] == '/') {
                    score += 10 + roll1 + roll2;
                } else {
                    score += 1 + roll1 + roll2;
                }
            } else {
                int roll2 = s[i + 1] - '0';
                score += roll1 + roll2;
            }
        } else if (s[i] == '/') {
            int roll1 = i < 8 ? s[i - 1] - '0' : 10;
            int roll2 = 10 - roll1;
            score += roll1 + roll2;
        }
    }
    return score;
}