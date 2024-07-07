int bowlingScore(string s) {
    int score = 0;
    bool lastRollWasStrike = false;
    for (int i = 0; i < 10; i++) {
        if (s[i] == 'X') {
            score += 30;
            lastRollWasStrike = true;
        } else if (s[i] == '/') {
            int nextTwoChars = s[i+1] - '0' + 10*(s[i+2] - '0');
            score += 10 + nextTwoChars;
            i++;
        } else {
            int thisRoll = s[i] - '0';
            if (lastRollWasStrike) {
                score += thisRoll * 2;
                lastRollWasStrike = false;
            } else {
                score += thisRoll;
            }
        }
    }
    return score;
}