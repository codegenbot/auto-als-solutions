int bowling(string s) {
    int score = 0;
    int currentFrame = 0;
    bool firstRollInFrame = true;

    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '/') {
            currentFrame++;
            firstRollInFrame = true;
        } else {
            int rollValue = s[i] - 'X';
            if (firstRollInFrame) {
                score += (rollValue == 10 ? 10 : rollValue);
                firstRollInFrame = false;
            } else {
                int lastRollValue = score - ((currentFrame - 1) * 10);
                if (lastRollValue + rollValue > 10) {
                    score += 10;
                } else {
                    score += lastRollValue + rollValue;
                }
                firstRollInFrame = false;
            }
        }
    }

    return score;
}