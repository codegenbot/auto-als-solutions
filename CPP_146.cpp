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
    std::vector<int> nums = {123, -456, 789, -111};
    int result = specialFilter(nums);
    std::cout << "Result: " << result << std::endl;
    return 0;
}