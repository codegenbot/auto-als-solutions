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
    // You can test your function with different inputs here
    std::vector<int> numbers = {123, -12, 15, -145, 120};
    int result = specialFilter(numbers);
    std::cout << "The number of filtered values is: " << result << std::endl;
    return 0;
}