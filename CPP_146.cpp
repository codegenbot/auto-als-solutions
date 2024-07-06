```cpp
#include <vector>
#include <iostream>

int specialFilter(std::vector<int> nums) {
    int count = 0;
    for (int num : nums) {
        if (abs(num) > 10 && (num % 10) % 2 != 0 && (abs(num) / 10) % 2 != 0) {
            count++;
        }
    }
    return count;
}

int main() {
    std::cout << specialFilter({1, 2, 3}) << std::endl;
    return 0;
}