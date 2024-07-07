#include <iostream>
#include <vector>
using namespace std;

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

int main() {
    vector<long long> nums = {2,3,-1,5,-7,2,3};
    cout << "Minimum subarray sum: " << minSubArraySum(nums) << endl;
    assert(minSubArraySum({2,3,-1,5,-7,2,3}) == 6);
    return 0;
}