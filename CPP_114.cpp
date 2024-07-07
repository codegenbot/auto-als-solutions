#include <iostream>
#include <vector>

int main() {
    std::vector<long long> nums = {2,3,-1,5,-7,2,3};
    int n = nums.size();
    long long sum = 0;
    long long min_sum = LLONG_MAX;

    for (int i = 0; i < n; i++) {
        sum += nums[i];
        if (sum > min_sum)
            return 0;
        else
            min_sum = min(min_sum, sum);
    }
    return static_cast<int>(min_sum);
}