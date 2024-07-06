```c++
#include <iostream>
#include <string>

bool isVowel(char c) {
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

std::string get_closest_vowel(std::string word) {
    std::string closestVowel = "";
    for (int i = 0; i < word.length(); ++i) {
        if (isVowel(word[i])) {
            closestVowel = std::string(1, word[i]);
            break;
        }
    }
    return closestVowel;
}

int main() {
    std::string word = "";
    std::cout << "Enter a word: ";
    std::cin >> word;
    std::cout << "The closest vowel is: " << get_closest_vowel(word) << std::endl;
    return 0;
}