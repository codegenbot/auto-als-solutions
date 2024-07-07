```cpp
#include <vector>
using namespace std;

int basement(vector<int>& nums) {
    int sum = 0;
    for (int i = 0; i < nums.size(); i++) {
        sum += nums[i];
        if (sum < 0)
            return i;
    }
    return -1; // not found
}

int main() {
    vector<int> nums = {-5, 2, -4, 3, -1};
    int result = basement(nums);
    cout << "Result: " << result << endl;
    return 0;
}