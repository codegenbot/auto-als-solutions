```cpp
#include <iostream>
#include <vector>

int sumOdd(const char* str) {
    int sum = 0;
    for (size_t i = 0; str[i]; ++i) { 
        if ((unsigned)str[i] % 2 != 0) {
            sum += (unsigned)str[i];
        }
    }
    return sum;
}

int main() {
    std::cout << sumOdd("Hello") << std::endl; 
    return 0;
}