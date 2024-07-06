bool is_happy(string s) {
    int len = s.length();
    if (len < 3)
        return false;
    for (int i = 0; i <= len - 3; i++) {
        bool unique = true;
        set<char> letters;
        for (int j = 0; j < 3; j++)
            letters.insert(s[i + j]);
        for (char c : s.substr(i, 3)) {
            if (letters.find(c) == letters.end())
                unique = false;
        }
        if (!unique)
            return false;
    }
    return true;
}