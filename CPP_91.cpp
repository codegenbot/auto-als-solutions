#include <iostream>
#include <string>

int is_bored(std::string input) {
    int count = 0;
    for (char c : input) {
        if (c == 'I' && !isalpha(c + 1)) {
            count++;
        }
    }
    return count;
}

int main() {
    std::string input;
    std::cout << "Enter a string: ";
    std::getline(std::cin, input);
    int result = is_bored(input);
    std::cout << "Number of 'I' without punctuation: " << result << "\n";
}