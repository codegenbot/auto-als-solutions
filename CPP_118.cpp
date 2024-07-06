```cpp
#include <iostream>
#include <string>

bool isVowel(char c) {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

std::string get_closest_vowel(std::string word) {
    for (int i = 0; i < word.length(); ++i) {
        if (word[i] == 'a' || word[i] == 'e' || word[i] == 'i' ||
            word[i] == 'o' || word[i] == 'u') {
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

int main() {
    std::string str;
    std::cout << "Enter a word: ";
    std::cin >> str;
    std::cout << get_closest_vowel(str) << std::endl;
}