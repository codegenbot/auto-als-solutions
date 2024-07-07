int bowlingScore(string s) {
    int score = 0;
    for (int i = 0; i < 10; i++) {
        if (s[i] == 'X') {
            score += 30;
        } else if (isdigit(s[i])) {
            int strikeRoll = s[i] - '0';
            score += 10 + strikeRoll * 2;
        } else if (s[i] == '/') {
            string roll1 = s.substr(i-1,1);
            string roll2 = s.substr(i+1,1);
            score += (roll1[0] - '0') + (roll2[0] - '0');
            i++;
        }
    }
    return score;
}