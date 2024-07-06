#include <algorithm>

vector<int> order_by_points(vector<int> nums) {
    sort(nums.begin(), nums.end(), [&] (int a, int b) {
        if (getSum(a) == getSum(b)) {
            return a > b;
        }
        return getSum(a) < getSum(b);
    });
    return nums;
}

int getSum(int n) {
    int sum = 0;
    while (n) {
        sum += n % 10;
        n /= 10;
    }
    return sum;
}