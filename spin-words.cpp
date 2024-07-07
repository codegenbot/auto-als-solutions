#include <iostream>
#include <string>

std::string spinWords(std::string str) {
    std::string result = "";
    std::vector<std::string> words;
    int start = 0;

    // Split string into individual words
    for (int i = 0; i <= str.length(); i++) {
        if (i == str.length() || str[i] == ' ') {
            words.push_back(str.substr(start, i - start));
            start = i + 1;
        }
    }

    // Reverse words that are 5 or more letters long
    for (int i = 0; i < words.size(); i++) {
        if (words[i].length() >= 5) {
            std::string reversedWord = "";
            for (int j = words[i].length() - 1; j >= 0; j--) {
                reversedWord += words[i][j];
            }
            words[i] = reversedWord;
        }
    }

    // Join the words back into a string
    for (int i = 0; i < words.size(); i++) {
        result += words[i];
        if (i < words.size() - 1) {
            result += " ";
        }
    }

    return result;
}

int main() {
    std::cout << spinWords("this is a test") << std::endl;
    return 0;
}