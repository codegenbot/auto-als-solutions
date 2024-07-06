```cpp
#include <iostream>
#include <sstream>
#include <string>

std::string string_sequence(int n) {
    std::ostringstream oss;
    for (int i = 1; i <= n; ++i) {
        if(i != 1)
            oss << " ";
        oss << i;
    }
    return std::string(oss.str());
}

int main() {
    int n;
    std::cout << "Enter a number: ";
    std::cin >> n;
    std::cout << string_sequence(n) << std::endl;
}