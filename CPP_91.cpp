#include <iostream>
#include <string>

int main() {
    std::string input;
    std::cout << "Enter a string: ";
    std::getline(std::cin, input);
    int result = count_i(input);
    std::cout << "Number of 'I' without punctuation: " << result << "\n";
}

int count_i(const std::string& str) {
    int count = 0;
    bool in_word = false;
    for (char c : str) {
        if (!in_word && !std::ispunct(c)) {
            in_word = true;
        }
        else if (in_word && std::isdigit(c) || std::isspace(c) || std::ispunct(c)) {
            in_word = false;
        }
        if (c == 'I' || c == 'i') {
            count++;
        }
    }
    return count;
}