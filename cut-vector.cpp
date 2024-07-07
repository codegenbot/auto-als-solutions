#include <vector>
#include <climits>

using namespace std;

struct CutResult {
    vector<int> left;
    vector<int> right;
};

CutResult cutVector(vector<int>& nums) {
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

    vector<int> left = vector<int>(nums.begin(), nums.begin() + cutIndex);
    vector<int> right = vector<int>(nums.begin() + cutIndex, nums.end());

    return CutResult{left, right};
}