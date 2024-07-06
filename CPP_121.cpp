```cpp
#include <iostream>
#include <vector>

int sumOdd(int x) {
    int sum = 0;
    for (int i = 1; i <= 10; i++) { 
        int y;
        std::cin >> y;
        if (y % 2 != 0) {
            sum += y;
        }
    }
    return sum;
}

std::cout << sumOdd(0) << std::endl;