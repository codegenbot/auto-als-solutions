#include <iostream>

int sumOdd(int x) {
    int sum = 0;
    for (int i = 1; i <= 10; i++) { 
        std::cin >> x;
        if (x % 2 != 0) {
            sum += x;
        }
    }
    return sum;
}

int main() {
    std::cout << sumOdd(0) << std::endl;
    return 0;
}