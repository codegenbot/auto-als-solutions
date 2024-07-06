bool check_if_last_char_is_a_letter(string txt) {
    if(txt.empty()) return false;
    string last_char = txt.substr(txt.length()-1, 1);
    bool is_last_char_alphabetical = (last_char.length() > 0) && isalpha(strtol(last_char.c_str(), NULL, 10));
    return !is_word_end(txt) && is_last_char_alphabetical;
}

bool is_word_end(string txt) {
    for(int i=0; i<txt.length(); i++) {
        if(!isspace(txt[i])) return false;
    }
    return true;
}