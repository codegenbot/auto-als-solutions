#include <iostream>
#include <string>

std::string fix_spaces(std::string text) {
    if(text.empty()) {
        return text;
    }
    
    bool prevSpace = false;
    for(int i = 0; i < text.length(); i++) {
        if(text[i] == ' ') {
            if(!prevSpace) {
                result += (i == 0 ? "" : "-");
            } else {
                result += "_";
            }
            prevSpace = true;
        } else {
            if(prevSpace) {
                result += "-";
                prevSpace = false;
            }
            result += text[i];
        }
    }
    
    return result;
}

int main() {
    assert(fix_spaces("   Exa 1 2 2 mple") == "-Exa_1_2_2_mple");
    return 0;
}