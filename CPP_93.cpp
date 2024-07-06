string encode(string message) {
    string result = "";
    for (char c : message) {
        if (isalpha(c)) {
            char base = isupper(c) ? 'A' : 'a';
            if (c == base || c == base + 1) {
                // Vowels
                c += 2;
            } else if (c >= 'a' && c <= 'z') {
                c -= 2;
            }
        }
        result += c;
    }
    return result;
}