#include <iostream>
#include <string>

std::string fix_spaces(std::string str) {
    size_t start = 0;
    while (start < str.size() && isspace(str[start])) {
        start++;
    }
    size_t end = str.size() - 1;
    while (end >= 0 && isspace(str[end])) {
        end--;
    }
    return str.substr(start, end - start + 1);
}

int main() {
    std::string str = " Example   3";
    std::cout << fix_spaces(str) << std::endl;
}