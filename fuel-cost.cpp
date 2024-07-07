#include <iostream>
#include <vector>

int fuelCost(std::vector<int> nums) {
    int sum = 0;
    for (int num : nums) {
        long long temp = num / 3;
        temp = temp - static_cast<long long>(floor(temp));
        sum += temp - 2;
    }
    return sum;
}