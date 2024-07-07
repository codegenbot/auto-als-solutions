int fuelCost(vector<int> nums) {
    int sum = 0;
    for (int num : nums) {
        long long temp = num / 3;
        temp = floor(temp);
        temp -= 2;
        sum += temp;
    }
    return sum;
}