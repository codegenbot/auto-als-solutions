#include<string>

int bowlingScore(string s) {
    int score = 0;
    for (int i = 0; i < 10; i++) {
        if (s[i] == 'X') {
            score += 30;
        } else if (s[i] == '/') {
            int strikeFrames = 1, total = 10;
            for (int j = i + 1; j < 11 && j < s.size(); j++) {
                if (s[j] != 'X') {
                    strikeFrames++;
                    total += s[j] - '0';
                } else {
                    break;
                }
            }
            score += strikeFrames * 10 + total / strikeFrames;
        } else {
            int first = s[i] - '0', second = (i < s.size() && s[i + 1] != '/') ? s[i + 1] - '0' : 0;
            score += first + second;
        }
    }
    return score;
}