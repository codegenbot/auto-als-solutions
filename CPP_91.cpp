#include <iostream>
#include <string>

int is_bored(std::string S) {
    int count = 0;
    size_t pos = 0;
    while ((pos = S.find("I", pos)) != std::string::npos) {
        if (S.find(".", pos) == std::string::npos && S.find("?", pos) == std::string::npos && S.find("!", pos) == std::string::npos)
            count++;
        else
            pos = S.find('.', pos);
    }
    return count;

int main() {
    std::string input;
    std::cout << "Enter a string: ";
    std::getline(std::cin, input);
    if (input.empty()) {
        std::cout << "Error! You must enter a string.\n";
    } else {
        int result = is_bored(input);
        std::cout << "Number of 'I' without punctuation: " << result << "\n";
    }
    return 0;
}