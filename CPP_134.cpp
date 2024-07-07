#include <string>
#include <cctype>

bool check_if_last_char_is_a_letter(std::string txt) {
    if(txt.empty()) return false;
    std::string lastChar = txt.substr(txt.length() - 1);
    if(lastChar.length() > 0 && !std::isalpha(lastChar[0])) return false;
    return true;