string solve(string s) {
    string result = "";
    for (char c : s) {
        if (isalpha(c)) {
            result += toupper(c) == tolower(c) ? tolower(c) : toupper(c);
        } else {
            result += c;
        }
    }
    return result.empty() ? s.substr(1, s.length()-1) + s[0] : result;
}