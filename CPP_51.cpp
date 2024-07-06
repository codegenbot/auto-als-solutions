#include<stdio.h>
#include<string>
#include<algorithm>
using namespace std;

string remove_vowels(string text){
    string result = "";
    for (char c : text) {
        if (!("aeiouAEIOU").find(std::tolower(c))) {
            result += c;
        }
    }
    return result;
}