```cpp
#include <iostream>
#include <string>

std::string fix_spaces(std::string text) {
    if(text.empty()) {
        return text;
    }
    
    std::string result = "";
    bool in_sequence = false;

    for(char c : text) {
        if(c == ' ') {
            if(!in_sequence) {
                if(result.length() > 0 && (result.back() != '_' || !in_sequence)) {
                    result += '-';
                } else {
                    result += '_';
                }
                in_sequence = true;
            }
        } else {
            in_sequence = false;
        }
        result += c;
    }

    return result;
}

int main() {
    assert(fix_spaces("   Exa 1 2 2 mple") == "-Exa_1_2_2_mple");
    return 0;
}