```cpp
#include <iostream>
#include <vector>

int sumOdd(const char* str) {
    int sum = 0;
    for (char c : std::string(str)) { 
        if (static_cast<int>(c) % 2 != 0) {
            sum += static_cast<int>(c);
        }
    }
    return sum;
}

int main() {
    std::cout << sumOdd("Hello") << std::endl; 
    return 0;
}