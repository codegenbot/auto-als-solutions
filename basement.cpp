#include <vector>
using namespace std;

int findIndexToMakeSumNegative(const vector<int>& nums) {
    int sum = 0;
    for (int i = 0; i < nums.size(); ++i) {
        sum += nums[i];
        if (sum < 0)
            return i;
    }
    return -1; // or throw an exception, depending on your preference
}

int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; ++i) {
        cin >> nums[i];
    }
    cout << findIndexToMakeSumNegative(nums) << endl;
    return 0;
}