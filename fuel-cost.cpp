#include <vector>

int fuelCost(vector<int> nums) {
    int sum = 0;
    for (int num : nums) {
        long long temp = num / 3;
        temp = static_cast<int>(temp);
        temp -= 2;
        sum += temp;
    }
    return sum;