#include <iostream>
#include <string>
#include <vector>

std::string camelCase(const std::string& input) {
    std::vector<std::string> words;
    size_t start = 0;
    for (size_t i = 0; i <= input.size(); ++i) {
        if (i == input.size() || input[i] == ' ') {
            words.push_back(input.substr(start, i - start));
            start = i + 1;
        }
    }

    std::string result;
    for (const auto& word : words) {
        if (!result.empty()) {
            result += std::toupper(word[0]);
        } else {
            result += word;
        }
        for (size_t i = 1; i < word.size(); ++i) {
            result += std::tolower(word[i]);
        }
    }

    return result;
}

int main() {
    std::string input;
    while (true) {
        std::cout << "Enter a string in kebab-case: ";
        std::cin >> input;
        std::cout << camelCase(input) << std::endl;
    }
    return 0;
}