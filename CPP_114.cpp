```
long long minSubArraySum(vector<long long> nums) {
    long long sum = 0, min_sum = LLONG_MAX;
    for (int i = 0; i < nums.size(); i++) {
        sum += nums[i];
        min_sum = min(min_sum, sum);
        if (sum > 0) {
            sum = 0;
        }
    }
    return min_sum;
}

#include <vector>
#include <cassert>

int main() {
    std::vector<long long> nums = {2,3,-1,-5};
    assert(minSubArraySum(nums) == -1);
    return 0;
}