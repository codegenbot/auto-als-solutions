#include <vector>
using namespace std;

int basement(vector<int>& nums) {
    int sum = 0;
    for (int i = 0; i < nums.size(); i++) {
        sum += nums[i];
        if (sum < 0) return i;
    }
    return -1;

}

int main() {
    vector<int> nums = {-1,2,3,-7,23,11,-4,13,-4,21,6,26};
    cout << basement(nums) << endl;
    return 0;
}