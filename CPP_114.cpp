```cpp
#include <iostream>
#include <vector>

using namespace std;

int main() {
    vector<long long> nums = {1,-5,-X,7};
    cout << minSubArraySum(nums) << endl;
    return 0;
}

long long minSubArraySum(vector<long long> nums) {
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