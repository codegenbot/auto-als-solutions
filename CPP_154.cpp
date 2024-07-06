bool cycpattern_check(string a, string b) {
    for (int i = 0; i < a.length(); i++) {
        for (int j = 0; j <= a.length() - b.length(); j++) {
            if (a.substr(j, a.length()).find(b) != string::npos) {
                return true;
            }
        }
    }
    return false;
}