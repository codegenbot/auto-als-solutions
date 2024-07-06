```
#include<string>
#include<algorithm>
using namespace std;

string remove_vowels(string text){
    string result = "";
    for (char c : text) {
        if (!isVowel(c)) {
            result += c;
        }
    }
    return result;
}

bool isVowel(char c) {
    return tolower(c) == 'a' || tolower(c) == 'e' || tolower(c) == 'i' || tolower(c) == 'o' || tolower(c) == 'u';
}