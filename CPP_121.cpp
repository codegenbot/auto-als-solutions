```cpp
#include <iostream>
#include <vector>

int sumOdd(int x) {
    int sum = 0;
    for (int i = 1; i <= 10; i++) { 
        if (i % 2 != 0) {
            sum += i;
        }
    }
    return sum;
}

int main() {
    std::cout << sumOdd(0) << std::endl;
    return 0;
}