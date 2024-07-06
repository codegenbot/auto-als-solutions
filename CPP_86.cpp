#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>

std::string anti_shuffle(std::string s) {
    std::stringstream result;
    bool inWord = false;
    for(int i=0; i<s.size(); i++){
        if(s[i] == ' '){
            if(inWord){
                sort(word.begin(), word.end());
                result << word << " ";
                inWord = false;
            }
            else{
                result << s[i];
            }
        }
        else{
            if(!inWord){
                inWord = true;
                word += s[i];
            }
            else{
                word += s[i];
            }
        }
    }
    if(inWord){
        sort(word.begin(), word.end());
        result << word;
    }
    return result.str();
}

int main() {
    std::string str = "Hi. My name is Mister Robot. How are you?";
    assert(anti_shuffle(str) == ".Hi My aemn is Meirst .Rboot How aer ?ouy");
    return 0;
}