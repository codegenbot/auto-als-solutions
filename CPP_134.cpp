#include <string>

bool check_if_last_char_is_a_letter(std::string txt) {
    if(txt.empty()) return false;
    int last_pos = txt.length() - 1;
    if(!isalpha(txt[last_pos])) return false;
    for(int i = 0; i < last_pos; i++) {
        if(isspace(txt[i]) || !isspace(txt[i+1])) return true;
    }
    return false;
}