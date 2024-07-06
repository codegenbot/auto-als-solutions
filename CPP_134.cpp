bool check_if_last_char_is_a_letter(string txt) {
    if (txt.empty()) return false; 
    char lastChar = txt.back();
    bool isLetter = isalpha(lastChar);
    int i;
    for(i=0; i<txt.length(); i++) {
        if(txt[i] == ' ') break;
    }
    return !isLetter && i == txt.length() - 1;
}