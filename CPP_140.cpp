#include <iostream>
#include <string>

std::string fix_spaces(std::string str) {
    if (str.empty()) {
        return str;
    }
    
    // Remove leading spaces
    while (!str.empty() && str[0] == ' ') {
        str = str.substr(1);
    }
    
    // Remove trailing spaces
    int pos = str.find_last_of(' ');
    if (~pos) {
        str = str.substr(0, pos + 1);
    }
    
    return str;
}

int main() {
    std::string str = " Example   3";
    std::cout << fix_spaces(str) << std::endl;
}