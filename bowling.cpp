int bowlingScore(std::string s) {
    int score = 0;
    bool inFrame = true;
    int currentRolls = 0;
    int currentFrameScore = 0;

    for (char c : s) {
        if (c == 'X') {
            score += 10 + (inFrame ? 10 : 20);
            inFrame = false;
            currentRolls++;
            currentFrameScore = 0;
        } else if (c == '/') {
            int firstRoll = currentRolls % 2 == 0 ? 10 - stoi(std::string(1, c)) : stoi(std::string(1, c));
            score += firstRoll;
            inFrame = false;
            currentRolls++;
            currentFrameScore = 0;
        } else if (c >= '0' && c <= '9') {
            int roll = stoi(std::string(1, c));
            currentRolls++;
            currentFrameScore += roll;

            if (currentRolls == 2) {
                inFrame = true;
                if (currentFrameScore < 10) {
                    score += currentFrameScore;
                } else if (currentFrameScore == 10) {
                    score += 10;
                }
                currentFrameScore = 0;
            }
        }
    }

    return score;
}