#include <iostream>
#include <string>

std::string fix_spaces(std::string text) {
    if(text.empty()) {
        return text;
    }
    
    bool in_sequence = false;
    std::string result = "";
    
    for(char c : text) {
        if(c == ' ') {
            if(!in_sequence) {
                result += (result.empty() ? "-" : "_");
                in_sequence = true;
            }
        } else {
            in_sequence = false;
            result += c;
        }
    }
    
    return result;
}

int main() {
    assert(fix_spaces("   Exa 1 2 2 mple") == "-Exa_1_2_2_mple");
    return 0;
}