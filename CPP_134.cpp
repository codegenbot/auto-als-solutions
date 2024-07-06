bool check_if_last_char_is_a_letter(string txt) {
    if (txt.empty()) return false;
    string last_char = txt.substr(txt.length() - 1);
    return isalpha(last_char[0]) && !isalnum(last_char[0]);
}