int prod_signs(vector<int> arr) {
    int product = 1;
    int sum = 0;

    for (int num : arr) {
        if (num == 0) {
            return -32768; // empty array or contains zero
        }
        product *= (num > 0 ? 1 : -1);
        sum += abs(num);
    }

    return product * sum;
}