#include <vector>
long long minSubArraySum(vector<long long> nums) {
    long long min_sum = INT_MAX;
    long long current_sum = 0;

    for (int i = 0; i < nums.size(); i++) {
        current_sum += nums[i];

        if (current_sum < min_sum) {
            min_sum = current_sum;
        }

        while (current_sum > 0 && i < nums.size() - 1) {
            current_sum -= nums[i];
            i++;
        }
    }

    return min_sum;
}
int main() {
    assert(minSubArraySum({1, -1}) == -1);
}