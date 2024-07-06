#include <iostream>

void solve(const char* input) {
}

int main() {
    std::cout << "Enter a string: ";
    getline(std::cin, std::string(input));
    if (input.empty()) {
        std::cout << "Error! Please enter a valid input." << std::endl;
    } else {
        solve(input.c_str());
    }
}