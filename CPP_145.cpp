#include <algorithm>

vector<int> order_by_points(vector<int> nums) {
    vector<pair<int, int>> numWithIndex;
    
    for (int i = 0; i < nums.size(); ++i) {
        numWithIndex.push_back({getDigitSum(nums[i]), i});
    }
    
    sort(numWithIndex.begin(), numWithIndex.end());
    
    vector<int> result;
    for (const auto& pair : numWithIndex) {
        result.push_back(nums[pair.second]);
    }
    
    return result;
}

int getDigitSum(int n) {
    int sum = 0;
    while (n != 0) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}