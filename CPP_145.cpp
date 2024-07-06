#include <algorithm>

vector<int> order_by_points(vector<int> nums) {
    vector<int> result = nums;
    sort(result.begin(), result.end(),
         [&nums](int a, int b) {
             if (abs(a) == abs(b)) {
                 return nums.find(a) > nums.find(b);
             }
             return abs(a) < abs(b);
         });
    return result;
}