#include <iostream>
#include <string>

std::string kebabToCamel(const std::string& input) {
    std::string result;
    bool capitalize = true;

    for (char c : input) {
        if (c == '-') {
            capitalize = true;
        } else if (capitalize) {
            result += std::toupper(c);
            capitalize = false;
        } else {
            result += std::tolower(c);
        }
    }

    return result;
}

int main() {
    std::string input;

    while (std::cin >> input) {
        std::cout << kebabToCamel(input) << '\n';
    }

    return 0;
}