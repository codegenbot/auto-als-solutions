#include <vector>
#include <climits>
#include <cmath>

using namespace std;

struct Result {
    vector<int> left;
    vector<int> right;
};

Result cutVector(vector<int>& nums) {
    int n = nums.size();
    int minDiff = INT_MAX;
    int cutIndex = 0;

    for (int i = 1; i < n; i++) {
        int diff = abs(nums[i-1] - nums[i]);
        if (diff <= minDiff) {
            minDiff = diff;
            cutIndex = i;
        }
    }

    Result result;
    result.left = vector<int>(nums.begin(), nums.begin() + cutIndex);
    result.right = vector<int>(nums.begin() + cutIndex, nums.end());

    return result;
}