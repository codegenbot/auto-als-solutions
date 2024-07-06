vector<int> order_by_points(vector<int> nums) {
    sort(nums.begin(), nums.end(), [](int a, int int b) {
        return tie(getSum(a), make_tuple(a)) < tie(getSum(b), make_tuple(b)));
    });
    return nums;
}

int getSum(int n) {
    int sum = 0;
    while (n != 0) {
        sum += abs(n % 10);
        n /= 10;
    }
    return sum;
}