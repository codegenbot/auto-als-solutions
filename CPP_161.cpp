#include <string>
#include <iostream>

std::string solve(std::string input) {
    int upper = 0;
    int lower = 0;
    for (char c : input) {
        if (isupper(c)) {
            upper++;
        } else if (islower(c)) {
            lower++;
        }
    }
    return "Uppercase: " + std::to_string(upper) + ", Lowercase: " + std::to_string(lower);
}

int main() {
    std::string input;
    std::cout << "Enter a string: ";
    std::getline(std::cin, input);
    if (input.empty()) {
        std::cout << "Error! Please enter a valid input." << std::endl;
    } else {
        std::string output = solve(input);
        std::cout << "Output: " << output << std::endl;
    }
    return 0;
}