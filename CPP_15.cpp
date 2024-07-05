```
#include <iostream>
#include <sstream>
#include <string>

std::string string_sequence(int n) {
    std::wostringstream oss;
    for (int i = 0; i <= n; ++i) {
        oss << i << " ";
    }
    return oss.str();
}

int main() {
    int n;
    std::cout << "Enter a number: ";
    std::cin >> n;
    std::cout << string_sequence(n) << std::endl;
    return 0;
}