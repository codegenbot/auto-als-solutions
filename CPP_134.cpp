#include <string>

bool check_if_last_char_is_a_letter(std::string txt) {
    if(txt.empty()) return false;
    char lastChar = txt.back();
    return isalpha(lastChar) && (txt.find(' ') == std::string::npos || txt.rfind(' ') < txt.size() - 1);
}