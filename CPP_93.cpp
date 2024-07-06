string encode(string message) {
    string result = "";
    for (char c : message) {
        if (isalpha(c)) {
            char base = isupper(c) ? 'A' : 'a';
            if (c == base) {
                c = (isupper(c)) ? 'Z' : 'z';
            } else {
                int diff = (int)(c - base);
                c = (char)((diff + 2) % 26 + base);
            }
        }
        result += c;
    }
    return result;
}