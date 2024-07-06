string encrypt(string s) {
    string result = "";
    for (char c : s) {
        if (c >= 'a' && c <= 'z') {
            int val = (int(c) - 97 + 2 * 2) % 26;
            result += (char)(val + 97);
        } else if (c >= 'A' && c <= 'Z') {
            int val = (int(c) - 65 + 2 * 2) % 26;
            result += (char)(val + 65);
        } else {
            result += c;
        }
    }
    return result;
}