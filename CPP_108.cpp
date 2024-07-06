```cpp
#include <iostream>
#include <vector>

int count_nums(std::vector<int> n) {
    int count = 0;
    for (int num : n) {
        if (num < 0) {
            num = -num;
        }
        int sum = 0;
        while (num > 0) {
            sum += num % 10;
            num /= 10;
        }
        if (sum > 0) {
            count++;
        }
    }
    return count;
}

int main() {
    std::vector<int> nums = {1};
    int result = count_nums(nums);
    std::cout << "The number of positive sums is: " << result << std::endl;
    return 0;
}