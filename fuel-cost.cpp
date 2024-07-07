```cpp
#include <vector>
#include <cmath>

int fuelCost(std::vector<int> nums) {
    int sum = 0;
    for (int num : nums) {
        long long temp = static_cast<long long>(num) / 3;
        temp = std::floor(temp);
        temp -= 2;
        sum += temp;
    }
    return sum;
}