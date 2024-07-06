#include <iostream>
#include <cctype>
#include <string>

bool isvowel(char c) {
    c = tolower(c);
    return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

std::string remove_vowels(std::string text) {
    std::string result = "";
    for (char c : text) {
        if (!isvowel(c)) {
            result += c;
        }
    }
    return result;
}

int main() {
    std::cout << "Enter a sentence: ";
    std::string input;
    std::getline(std::cin, input);
    std::cout << "Sentence without vowels: " << remove_vowels(input) << std::endl;
    return 0;
}