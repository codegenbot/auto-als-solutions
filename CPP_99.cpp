#include <iostream>
#include <string>
#include <cmath>

int closest_integer(std::string value) {
    double num = std::stod(value);
    return (num >= 0) ? ceil(num) : floor(num);
}

int main() {
    assert(closest_integer("0") == 0);
    std::cout << "Enter a decimal number: ";
    std::string input;
    std::cin >> input;
    int result = closest_integer(input);
    std::cout << "The closest integer is: " << result << std::endl;
    return 0;
}