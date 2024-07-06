bool is_palindrome(string text) {
    string str = text;
    for (int i = 0; i < str.length(); i++) {
        if (str[i] != tolower(str[str.length() - 1 - i]))
            return false;
    }
    return true;
}