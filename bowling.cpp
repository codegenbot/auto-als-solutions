int bowlingScore(string s) {
    int score = 0;
    int frame = 1;
    for (char c : s) {
        if (c == '/') {
            if (frame < 10) {
                score += min(stoi(s.substr(0, s.find('/'))) + stoi(s.substr(s.find('/') + 1)), 10);
            }
            frame++;
            s = s.substr(s.find('/') + 1);
        } else if (c == 'X') {
            score += 10;
            frame++;
            s = "";
        } else {
            int pins = 0;
            for (; c != '/' && c != 'X'; c++) {
                pins *= 10;
                pins += c - '0';
            }
            if (pins < 10) {
                score += pins;
            } else {
                score += 10 + min(pins - 10, 10);
            }
            frame++;
            s = s.substr(s.find('/') + 1);
        }
    }
    return score;
}