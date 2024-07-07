int bowling(string s) {
    int score = 0;
    int rolls[2][3]; // first dimension represents frames, second dimension represents number of rolls per frame (1 or 2)
    int i = 0, j = 0;

    // parse input string and store it in the 2D array
    for (int k = 0; k < s.length(); k++) {
        if (s[k] == '/') {
            j++;
            i = 0;
        } else {
            rolls[i][j] = s[k] - '0';
            i++;
        }
    }

    // calculate the score
    for (int i = 0; i < 2; i++) {
        if (rolls[i][1] + rolls[i][0] >= 10) {
            score += 10;
        } else {
            score += rolls[i][0] + rolls[i][1];
        }
    }

    // calculate the bonus for the last two frames
    if (rolls[1][0] + rolls[1][1] >= 10) {
        score += rolls[1][0] + rolls[1][1];
    } else {
        score += rolls[1][0] + rolls[1][1] + rolls[1][2];
    }

    return score;
}