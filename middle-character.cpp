#include <iostream>
#include <string>

int main() {
    std::string input;
    std::cin >> input;
    int len = input.length();
    if (len % 2 == 0) {
        std::cout << input.substr(len / 2 - 1, 2) << std::endl;
    } else {
        std::cout << input.substr(len / 2, 1) << std::endl;
    }
    return 0;
}