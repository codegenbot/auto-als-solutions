#include <iostream>
#include <vector>
#include <string>

int sumOdd(int x) {
    int sum = 0;
    for (int i = 1; i <= 10; i++) { 
        if (i % 2 != 0) {
            sum += i;
        }
    }
    std::string output = "The sum of odd numbers is: ";
    output += std::to_string(sum);
    return output;
}

int main() {
    std::cout << sumOdd(0) << std::endl;
    return 0;
}