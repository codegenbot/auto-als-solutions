int prod_signs(vector<int> arr) {
    int sign = 1;
    long long sum = 0;
    for (int num : arr) {
        if (num == 0) {
            return -32768; // Return -32768 for empty array or an array containing zero.
        }
        sign *= (num > 0 ? 1 : (num < 0 ? -1 : 0));
        sum += abs(num);
    }
    return sum * sign;
}