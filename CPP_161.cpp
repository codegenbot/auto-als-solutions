string solve(string s) {
    string result = "";
    bool foundLetter = false;

    for (char c : s) {
        if (isalpha(c)) {
            foundLetter = true;
            c = (c == tolower(c)) ? toupper(c) : tolower(c);
        }
        result += c;
    }

    if (!foundLetter)
        reverse(result.begin(), result.end());

    return result;
}