#include <iostream>
using namespace std;

long long minSubArraySum(vector<long long> nums) {
    long long min_sum = LLONG_MAX;
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
    vector<long long> input;
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;
    
    for(int i=0; i<n; i++) {
        long long x;
        cout << "Enter element " << i+1 << ": ";
        cin >> x;
        input.push_back(x);
    }
    
    cout << "The minimum subarray sum is: " << minSubArraySum(input) << endl;

    return 0;
}