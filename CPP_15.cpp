#include <iostream>
#include <sstream>
#include <string>

std::string string_sequence(int n) {
    std::ostringstream oss;
    for (int i = 0; i <= n; ++i) {
        oss << i << " ";
    }
    if(n != 0)
        oss << std::endl; 
    return oss.str();
}

int main() {
    int n;
    std::cout << "Enter a number: ";
    std::cin >> n;
    if(n > 0) {
        std::cout << string_sequence(n) << std::endl;
    }
    else
        std::cout << "Error! Please enter a positive integer." << std::endl;
}