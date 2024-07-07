bool check_if_last_char_is_a_letter(string txt) {
    if (txt.empty()) return false;
    char lastChar = txt.back();
    bool isLastCharLetter = isalpha(lastChar);
    int i = 0;
    while (i < txt.length() - 1 && txt[i] != ' ') i++;
    if (i == txt.length() - 2) {
        return isLastCharLetter;
    } else {
        return false;
    }
}