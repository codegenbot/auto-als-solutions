#include <string>
#include <iostream>

std::string solve(std::string str) {
    // implement your logic here
    return str;
}

int main() {
    std::string input;
    std::cout << "Enter a string: ";
    std::getline(std::cin, input);
    
    if(input.empty()) {
        std::cout << "Error! Please enter a valid input." << std::endl;
    } else {
        std::string output = solve(input);
        std::cout << "Output: " << output << std::endl;
    }
}