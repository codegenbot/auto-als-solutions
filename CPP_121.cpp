#include <iostream>
#include <vector>

int sumOdd(int) {
    int sum = 0;
    for (int i = 1; i <= 10; i++) { 
        std::string y;
        std::cout << "Enter an odd number: ";
        std::getline(std::cin, y);
        if (std::stoi(y) % 2 != 0) {
            sum += std::stoi(y);
        }
    }
    return sum;
}

int main() {
    std::cout << sumOdd(0) << std::endl;
}