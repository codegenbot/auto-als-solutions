int bowlingScore(string frames) {
    int score = 0;
    for (int i = 0; i < frames.length(); i++) {
        if (frames[i] == 'X') {
            score += 30;
            i++;
            if (i < frames.length() && frames[i] != '/') {
                score += frames[i] - '0';
            }
        } else if (frames[i] == '/') {
            score += 10;
            i++;
            if (i < frames.length()) {
                score += frames[i] - '0';
            }
        } else {
            int strike = 0;
            while (i < frames.length() && frames[i] != '/' && frames[i] <= '9') {
                strike *= 10;
                strike += frames[i] - '0';
                i++;
            }
            if (strike > 10) {
                score += 10 + strike / 10;
            } else {
                score += strike;
            }
        }
    }
    return score;
}