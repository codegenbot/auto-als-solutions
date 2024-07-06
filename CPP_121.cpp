#include <iostream>
#include <vector>

int sumOdd(std::string str) {
    int sum = 0;
    for (char c : str) { 
        int i = std::stoi(&c, nullptr, 10);
        if (i % 2 != 0) {
            sum += i;
        }
    }
    return sum;
}

int main() {
    std::cout << sumOdd("Hello") << std::endl; 
    return 0;
}