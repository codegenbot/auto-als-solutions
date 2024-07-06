#include <iostream>
#include <vector>

int specialFilter(std::vector<int> nums) {
    int count = 0;
    for (int num : nums) {
        if (abs(num) > 10 && (num % 10) % 2 != 0 && (num / 10) % 10 % 2 != 0) {
            count++;
        }
    }
    return count;
}

int main() {
    std::vector<int> numbers = {};
    std::cout << "Enter some numbers (negative to stop):" << std::endl;
    for (int &num : numbers) {
        std::cin >> num;
        if (num < 0) break;
    }
    
    int result = specialFilter(numbers);
    std::cout << "The count is: " << result << std::endl;