#include <string>

std::string anti_shuffle(std::string s){
    std::string result = "";
    for(int i=0; i<s.size(); i++){
        if(s[i] == ' '){
            result += ' ';
            continue;
        }
        std::string word = "";
        for(int j=i; j<s.size() && s[j] != ' '; j++){
            word += s[j];
        }
        i = j - 1;
        sort(word.begin(), word.end());
        result += word;
    }
    return result;