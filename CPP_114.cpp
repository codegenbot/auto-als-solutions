```cpp
#include <iostream>
#include <vector>

long long minSubArraySum(std::vector<long long> nums) {
    int n = nums.size();
    long long sum = 0;
    long long min_sum = LLONG_MAX;

    for (int i = 0; i < n; i++) {
        sum += nums[i];
        if (sum > min_sum)
            return min_sum;
        else
            min_sum = min(min_sum, sum);
    }
    return min_sum;
}

int main() {
    std::vector<long long> nums = {2, 3, -1, 5, -3, 2};
    std::cout << "The minimum subarray sum is: " << minSubArraySum(nums) << std::endl;
    return 0;
}