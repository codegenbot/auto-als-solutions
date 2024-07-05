#include <iostream>
#include <sstream>
#include <string>

std::ostringstream string_sequence(int n) {
    std::ostringstream oss;
    for (int i = 0; i <= n; ++i) {
        oss << i << " ";
    }
    return oss;
}

int main() {
    int n;
    std::cout << "Enter a number: ";
    std::cin >> n;
    std::cout << string_sequence(n).str() << std::endl;
    return 0;
}