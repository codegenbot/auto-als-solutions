#include <string>
#include <cctype>

std::string get_closest_vowel(std::string word) {
    for (int i = word.size() - 1; i > 0; --i) {
        if (!isalpha(word[i])) continue;
        if (ispunct(word[i]) || !islower(word[i])) continue;
        if (word[i] == 'y' && (i == 1 || !isalpha(word[i-1]))) continue;
        for (int j = i - 1; j >= 0; --j) {
            if (!isalpha(word[j])) break;
            if (ispunct(word[j]) || !islower(word[j])) break;
            if (word[j] == 'y' && (j == 0 || !isalpha(word[j-1]))) break;
            if (strchr("aeiouAEIOU", tolower(word[j])) != NULL) {
                return word.substr(j, i-j+1);
            }
        }
    }
    return "";
}