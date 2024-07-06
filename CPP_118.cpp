#include <iostream>
#include <string>

std::string get_closest_vowel(std::string word) {
    std::string closestVowel = "";
    for (int i = word.length() - 1; i >= 0; --i) {
        if (word[i] == 'a' || word[i] == 'e' || word[i] == 'i' ||
            word[i] == 'o' || word[i] == 'u') {
            closestVowel = std::string(1, word[i]);
            bool isLast = true;
            for (int j = i + 1; j < word.length(); ++j) {
                if (!isVowel(word[j])) {
                    isLast = false;
                    break;
                }
            }
            if (!isLast) {
                return closestVowel;
            }
        }
    }
    return closestVowel;
}

bool isVowel(char c) {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

int main() {
    std::string word;
    std::cout << "Enter a word: ";
    std::cin >> word;
    std::cout << "The closest vowel is: " << get_closest_vowel(word) << std::endl;
    return 0;
}