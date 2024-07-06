#include <string>
#include <algorithm>

using namespace std;

string get_closest_vowel(string word) {
    int left = 0;
    for (int right = word.size() - 1; right >= 0 && !isVowel(word[right]); right--) {
        left = right + 1;
    }
    if (!isVowel(word[left])) return "";
    for (int i = left - 1; i > 0; i--) {
        if (isVowel(word[i])) return string(1, word[i]);
    }
    return "";
}

bool isVowel(char c) {
    c = tolower(c);
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}