#include <vector>
#include <iostream>

int main() {
    int count = 0;
    std::cout << "Enter numbers (space-separated): ";
    std::string input;
    std::getline(std::cin, input);
    std::istringstream iss(input);
    int num;
    while (iss >> num) {
        if (abs(num) > 10 && (num % 10) % 2 != 0 && (abs(num) / 10) % 2 != 0) {
            count++;
        }
    }
    std::cout << "Number of special numbers: " << count << std::endl;
    return 0;
}