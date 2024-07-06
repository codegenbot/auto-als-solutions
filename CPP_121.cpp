```cpp
#include <iostream>
#include <vector>

int sumOdd(std::string str) {
    int sum = 0;
    for (char c : str) { 
        if (static_cast<int>(c) % 2 != 0) {
            // Convert char to int and add it to sum
            sum += static_cast<int>(c);
        }
    }
    return sum;
}

int main() {
    std::cout << sumOdd("Hello") << std::endl; 
    return 0;
}