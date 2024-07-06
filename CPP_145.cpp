#include <algorithm>
using namespace std;

vector<int> order_by_points(vector<int> nums) {
    auto f = [&](int x) {
        int sum = 0;
        while (x > 0) {
            sum += x % 10;
            x /= 10;
        }
        return make_pair(sum, distance(nums.begin(), find(nums.begin(), nums.end(), x)) + 1);
    };
    nums.sort([](int a, int b) { return f(a) > f(b); });
    return nums;
}