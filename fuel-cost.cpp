int solve(vector<int>& v) {
    int sum = 0;
    for (int num : v) {
        int new_num = (num / 3) - 2;
        sum += new_num;
    }
    return sum;
}