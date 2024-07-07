int bowlingScore(string s) {
    int score = 0;
    int roll = 0;
    for(int i=0; i<s.length(); i++) {
        if(s[i] == 'X') {
            score += 10 + (roll > 1 ? 10 : 0);
            roll = 0;
        } else if(s[i] == '/') {
            int previousRoll = s[i-1] - '0';
            int currentRoll = s[i+1] - '0';
            score += previousRoll + currentRoll;
            i++;
        } else {
            roll += s[i] - '0';
        }
    }
    return score;
}