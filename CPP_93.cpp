string encode(string message) {
    string result = "";
    for (char c : message) {
        if (isalpha(c)) {
            char base = isupper(c) ? 'A' : 'a';
            char newChar = ((c - base + 2) % 26) + base;
            if (vowel(base, newChar))
                newChar = ((newChar - base + 4) % 26) + base;
            result += newChar;
        } else {
            result += c;
        }
    }
    return result;
}

bool vowel(char base, char c) {
    if (isupper(c)) {
        return c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U';
    } else {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
    }
}