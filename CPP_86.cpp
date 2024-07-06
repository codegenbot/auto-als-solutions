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
        for(;j<s.size() && s[j] != ''; j++){
            
        }
        string word = s.substr(i, j - i);
        for(int k=0; k<word.size(); k++){
            result += word[k];
        }
        sort(&word[0], &word[0] + word.size());
        result += word;
        i = j;
    }
    return result;
}

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
        for(;j<s.size() && s[j] != ''; j++){
            
        }
        string word = s.substr(i, j - i);
        result.append(word);
        sort(&word[0], &word[0] + word.size());
        result += word;
        i = j;
    }
    return result;
}