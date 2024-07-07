#include <iostream>
#include <string>

std::string fix_spaces(std::string text) {
    std::string result = "";
    for(int i = 0; i < text.length(); i++){
        if(text[i] == ' ' && (i == 0 || text[i-1] != ' ') && (i == text.length() - 1 || text[i+1] != ' ')){
            result += '_';
        }
        else if(text[i] == ' '){
            int count = 0;
            while(i < text.length() && text[i] == ' '){
                i++;
                count++;
            }
            if(count > 2)result += '-';
            else result += '_';
        }
        else{
            result += text[i];
        }
    }
    return result;
}

int main() {
    assert(fix_spaces("   Exa 1 2 2 mple") == "-Exa_1_2_2_mple");
    return 0;
}