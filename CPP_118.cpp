#include <iostream>
#include <cctype>

std::string get_closest_vowel(std::string word) {
    for (int i = 0; i < word.length(); ++i) {
        if (isVowel(word[i])) {
            bool isFound = true;
            for (int j = i + 1; j < word.length(); ++j) {
                if (isVowel(word[j])) {
                    isFound = false;
                    break;
                }
            }
            if (!isFound)
                return std::string(1, word[i]);
        }
    }
    return "";
}

bool isVowel(char c) {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

int main() {
    std::string str;
    std::cout << "Enter a word: ";
    std::cin >> str;
    std::cout << get_closest_vowel(str) << std::endl;
    return 0;
}