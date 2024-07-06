#include <string>

bool check_if_last_char_is_a_letter(string txt) {
    if (txt.empty()) return false;
    size_t last_space = txt.find_last_of(' ');
    if (last_space == string::npos || last_space == txt.size() - 1) 
        return isalpha(txt.back());
    return isalpha(txt.back());
}