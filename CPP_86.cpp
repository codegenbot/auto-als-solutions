#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>

std::string anti_shuffle(std::string s) {
    std::stringstream result;
    std::string word;
    for(int i=0; i<s.size(); i++){
        if(s[i] == ' '){
            result << ' ';
            continue;
        }
        for(int j=i; j<s.size() && s[j] != ' '; j++){
            word += s[j];
        }
        std::sort(word.begin(), word.end());
        while (!word.empty()) {
            result << word.back();
            word.pop_back();
        }
    }
    return result.str();
}

int main() {
    std::string str = "Hi. My name is Mister Robot. How are you?";
    assert(anti_shuffle(str) == ".Hi My aemn is Meirst .Rboot How aer ?ouy");
    return 0;
}