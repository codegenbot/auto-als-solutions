Here is the completed code:

long long minSubArraySum(vector<long long> nums) {
    long long res = LLONG_MAX;
    for (int i = 0; i < nums.size(); i++) {
        long long sum = 0;
        for (int j = i; j < nums.size(); j++) {
            sum += nums[j];
            res = min(res, sum);
        }
    }
    return res;
}