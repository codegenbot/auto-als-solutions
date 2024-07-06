#include <string>
#include <cctype>

string get_closest_vowel(string word) {
    for (int i = 0; i <= word.length() - 1; ++i) {
        if (isVowel(word[i])) {
            for (int j = i + 1; j <= word.length(); ++j) {
                if (!isVowel(word[j])) {
                    return string(1, word[i]);
                }
            }
        }
    }
    return "";
}

bool isVowel(char c) {
    c = tolower(c);
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}