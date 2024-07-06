#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;

string get_closest_vowel(string word) {
    string vowels = "aeiouAEIOU";
    int left = 0;
    for(int i=word.size()-1; i>=0; i--) {
        if(vowels.find(word[i]) != -1)
            return word.substr(left, i-left+1);
        else
            left = i + 1;
    }
    return "";
}