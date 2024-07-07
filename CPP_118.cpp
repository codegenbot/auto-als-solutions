#include <string>
#include <algorithm>
using namespace std;

string get_closest_vowel(string word) {
    for (int i = 0; i < word.size(); i++) {
        if (!isalpha(word[i])) continue;
        for (int j = i + 1; j < word.size(); j++) {
            if (!isalpha(word[j])) break;
            if (vowel(word[i]) || vowel(word[j])) return word.substr(i, 1);
        }
    }
    return "";
}

bool vowel(char c) {
    return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
            c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U');
}