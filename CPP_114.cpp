Here is the completed code:

long long minSubArraySum(vector<long long> nums) {
    long long total_sum = 0;
    for (int i = 0; i < nums.size(); ++i) {
        total_sum += nums[i];
        if (total_sum > 0) break;
    }
    return total_sum;
}