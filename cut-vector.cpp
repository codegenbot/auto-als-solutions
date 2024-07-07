#include <vector>
using namespace std;

vector<int> cutVector(vector<int>& nums) {
    int minDiff = INT_MAX;
    int splitIndex = 0;
    
    for (int i = 1; i < nums.size(); i++) {
        int diff = abs(nums[i] - nums[i-1]);
        
        if (diff == 0 || diff < minDiff) {
            minDiff = diff;
            splitIndex = i;
        }
    }
    
    vector<int> left(nums.begin(), nums.begin() + splitIndex);
    vector<int> right(nums.begin() + splitIndex, nums.end());
    
    return {left, right};
}

int main() {
    int n;
    cin >> n;
    vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        cin >> nums[i];
    }
    
    auto result = cutVector(nums);
    
    cout << result[0].size() << endl;
    for (int num : result[0]) {
        cout << num << " ";
    }
    cout << endl;
    
    cout << result[1].size() << endl;
    for (int num : result[1]) {
        cout << num << " ";
    }
    cout << endl;
    
    return 0;
}