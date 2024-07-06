#include<string>
#include<algorithm>
using namespace std;

bool isVowel(char c) {
    return toupper(c) == 'A' || toupper(c) == 'E' || toupper(c) == 'I' || toupper(c) == 'O' || toupper(c) == 'U';
}

string remove_vowels(string text){
    string result = "";
    for (char c : text) {
        if (!isVowel(c)) {
            result += c;
        }
    }
    return result;
}