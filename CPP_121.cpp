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

int main() {
    int inputNumber = 0;
    std::cout << "Enter an integer: ";
    std::cin >> inputNumber;

    int solutions(int x) {
        return sumOdd(x);
    }

    assert(sumOdd(inputNumber) == 3);

    return 0;
}