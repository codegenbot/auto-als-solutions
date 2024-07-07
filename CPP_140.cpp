#include <iostream>
#include <string>

std::string fix_spaces(std::string text) {
    if(text.empty()) {
        return text;
    }
    
    std::string result = "";
    bool in_space_sequence = false;
    for(char c : text) {
        if(c == ' ') {
            if(in_space_sequence) {
                result += '-';
                in_space_sequence = false;
            } else {
                if(result.size() > 0 && (result.back() != '_' || result.back() != '-')) {
                    result += '_';
                }
                in_space_sequence = true;
            }
        } else {
            if(in_space_sequence) {
                result += c;
                in_space_sequence = false;
            } else {
                result += c;
            }
        }
    }
    
    return result;
}

int main() {
    assert(fix_spaces("   Exa 1 2 2 mple") == "-Exa_1_2_2_mple");
    return 0;
}