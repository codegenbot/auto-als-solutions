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

bool std::isVowel(char c) {
    return toupper(c) == 'A' || toupper(c) == 'E' || toupper(c) == 'I' || toupper(c) == 'O' || toupper(c) == 'U';
}