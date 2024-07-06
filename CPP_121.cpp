```cpp
#include <iostream>
#include <vector>

int sumOdd(const std::string& str) {
    int sum = 0;
    for (char c : str) { 
        if ((int)c % 2 != 0) {
            sum += (int)c;
        }
    }
    return sum;
}

int main() {
    std::cout << sumOdd("Hello") << std::endl; 
    return 0;
}