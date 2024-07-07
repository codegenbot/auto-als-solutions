string solve(string s) {
    string result = "";
    bool has_letter = false;

    for (char c : s) {
        if (isalpha(c)) { // Check if character is a letter
            has_letter = true;
            result += (c >= 'a' && c <= 'z') ? toupper(c) : tolower(c);
        } else {
            result += c;
        }
    }

    return has_letter ? s : string(rbegin(s), rend(s));
}