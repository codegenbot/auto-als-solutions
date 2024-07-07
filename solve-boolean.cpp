bool evaluate(const string &s) {
    bool res = true;
    for (char c : s) {
        if (c == '&') {
            res &= false;
        } else if (c == '|') {
            res |= true;
        } else if (c == 't' || c == 'T') {
            res = true;
        } else if (c == 'f' || c == 'F') {
            res = false;
        }
    }
    return res;
}