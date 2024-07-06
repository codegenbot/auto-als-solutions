#include <iostream>
#include <string>

void solve(const char* input) {
    std::cout << "Reversed: ";
    for(int i = strlen(input)-1; i >=0 ; i--) {
        std::cout << input[i];
    }
    std::cout << std::endl;
}

int main() {
    std::cout << "Enter a string: ";
    std::string input;
    std::getline(std::cin, input);
    if (input.empty()) {
        std::cout << "Error! Please enter a valid input." << std::endl;
    } else {
        solve(input.c_str());
    }
    return 0;
}