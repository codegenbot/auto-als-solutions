#include <vector>
#include <iostream>

int specialFilter(std::vector<int> nums) {
    int count = 0;
    for (int num : nums) {
        if (abs(num) > 10 && ((num / 100) % 10) % 2 != 0 && (num % 10) % 2 != 0) {
            count++;
        }
    }
    return count;
}

int main() {
    assert(specialFilter({}) == 0);
    std::vector<int> test = {123, -12, 101, 102};
    int result = specialFilter(test);
    std::cout << "The number of integers in the vector that satisfy the condition is: " << result << std::endl;
    return 0;
}