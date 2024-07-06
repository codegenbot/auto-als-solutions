#include <iostream>
#include <string>

using namespace std;

string fix_spaces(string text){
    string result = "";
    bool prev_space = false;

    for(int i=0; i<text.length(); i++){
        if(text[i] == ' '){
            if(prev_space || i==text.length()-1) {
                if(result.length() > 0) {
                    result += "_";
                }
                continue;
            }
            result += '_';
        } else {
            result += text[i];
        }
        prev_space = (text[i] == ' ');
    }

    return result;
}