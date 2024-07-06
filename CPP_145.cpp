#include <algorithm>
using namespace std;

vector<int> order_by_points(vector<int> nums) {
    vector<pair<int, int>> numPairs;
    for (int i = 0; i < nums.size(); i++) {
        numPairs.push_back({getDigitSum(nums[i]), i});
    }
    sort(numPairs.begin(), numPairs.end());
    vector<int> result;
    for (const auto& pair : numPairs) {
        result.push_back(nums[pair.second]);
    }
    return result;
}

int getDigitSum(int n) {
    int sum = 0;
    while (n) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}