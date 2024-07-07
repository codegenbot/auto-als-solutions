#include <iostream>
using namespace std;

long long minSubArraySum(vector<long long> nums) {
    long long min_sum = INT_MAX;
    long long current_sum = 0;

    for (int i = 0; i < nums.size(); i++) {
        current_sum += nums[i];
        min_sum = min(min_sum, current_sum);
        if (current_sum > 0) {
            current_sum = 0;
        }
    }

    return min_sum;
}

int main() {
    long long sum1 = minSubArraySum({1, -1});
    cout << "Minimum Subarray Sum: " << sum1 << endl;

    int numTests;
    cin >> numTests;
    
    for(int i=0; i<numTests; i++) {
        long long n;
        cin >> n;
        vector<long long> nums(n);
        for(long long &num : nums) {
            cin >> num;
        }
        long long sum2 = minSubArraySum(nums);
        cout << "Minimum Subarray Sum: " << sum2 << endl;
    }

    return 0;
}