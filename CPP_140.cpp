#include <iostream>
#include <string>

std::string fix_spaces(std::string text) {
    std::string result = "";
    bool in_sequence = false;
    for(int i = 0; i < text.length(); i++){
        if(text[i] == ' '){
            if(!in_sequence){
                if(result.length() > 0 || i != 0)
                    result += '_';
                else
                    result += '-';
                in_sequence = true;
            }
        }else{
            in_sequence = false;
            result += text[i];
        }
    }
    return result;
}

int main() {
    assert(fix_spaces("   Exa 1 2 2 mple") == "-Exa_1_2_2_mple");
    return 0;
}