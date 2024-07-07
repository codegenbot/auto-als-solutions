int bowlingScore(string s) {
    int score = 0;
    int i = 0;
    while (i < s.length()) {
        if (s[i] == 'X') {
            score += 30;
            i++;
        } else if (s[i] == '/') {
            int strikeCount = 1;
            while (i + 2 <= s.length() && s.substr(i, 3) != "XXX") {
                if (s.substr(i, 1) == 'X') {
                    score += 10;
                    i++;
                    strikeCount++;
                } else {
                    score += 10 - s[i] - '0';
                    i++;
                    break;
                }
            }
            for (int j = 0; j < strikeCount; j++) {
                score += 10;
            }
        } else {
            int count = s[i] - '0' + s[i+1] - '0';
            score += count;
            i += 2;
        }
    }
    return score;
}