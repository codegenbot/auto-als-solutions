int bowlingScore(string s) {
    int score = 0;
    for (int i = 0; i < 10; i++) {
        if (s[i] == 'X') {
            score += 30;
        } else if (s[i] == '/') {
            int nextTwo = stoi(s.substr(i + 1, 2));
            score += 10 + nextTwo;
            i++;
        } else {
            int thisRoll = 0;
            for (int j = i; j < s.length() && j < i + 2; j++) {
                if (s[j] == 'X') {
                    thisRoll += 30;
                    break;
                } else if (s[j] == '/') {
                    int nextTwo = stoi(s.substr(j + 1, 2));
                    thisRoll += 10 + nextTwo;
                    i++;
                    j++;
                    break;
                }
                thisRoll += s[j] - '0';
            }
            score += thisRoll;
        }
    }
    return score;
}