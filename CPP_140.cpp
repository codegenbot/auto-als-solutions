```cpp
#include <iostream>
#include <string>

std::string fix_spaces(std::string text) {
    std::string result = "";
    bool consecutive = false;

    for(int i = 0; i < text.length(); i++){
        if(text[i] == ' '){
            if(consecutive){
                result += '-';
                consecutive = false;
            } else {
                if(result.length() > 0 && (result[result.length()-1] != '_' || result[result.length()-1] != '-')){
                    result += '_';
                }
                consecutive = true;
            }
        } else {
            result += text[i];
            consecutive = false;
        }
    }

    return result;
}

int main() {
    assert(fix_spaces("   Exa 1 2 2 mple") == "-Exa_1_2_2_mple");
    return 0;
}