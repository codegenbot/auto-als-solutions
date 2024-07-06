#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

string anti_shuffle(string s){
    string result = "";
    int i = 0;
    while(i<s.size()){
        if(s[i] == ' '){
            result += ' ';
            i++;
            continue;
        }
        int j = i + 1;
        for(;j<s.size() && s[j] != '\0'; j++){
            
        }
        string word = s.substr(i, j - i);
        result.append(word);
        sort(word.begin(), word.end());
        result += word;
        i = j;
    }
    return result;
}