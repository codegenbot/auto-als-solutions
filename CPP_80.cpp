bool is_happy(string s) {
    if (s.length() < 3)
        return false;
    for (int i = 0; i <= s.length() - 3; i++) {
        string t = s.substr(i, 3);
        bool duplicate = true;
        int charCount[256] = {0}; 
        for (char c : t) {
            charCount[c]++;
        }
        for (char c : t) {
            if (charCount[c] > 1) {
                duplicate = false;
                break;
            }
        }
        if (!duplicate)
            return false;
    }
    return true;
}