```cpp
#include <iostream>
#include <string>

std::string string_sequence(int n);
int main() {
    int n;
    std::cout << "Enter a number: ";
    std::cin >> n;
    std::cout << string_sequence(n) << std::endl;
    return 0;
}

std::string string_sequence(int n) {
    std::string result = "";
    for (int i = 1; i <= n; i++) {
        result += std::to_string(i) + " ";
    }
    return result;
}