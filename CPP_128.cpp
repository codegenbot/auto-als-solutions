int prod_signs(vector<int> arr) {
    long long product = 1;
    int sum = 0;

    for (int x : arr) {
        product *= ((x > 0) ? 1 : ((x < 0) ? -1 : 0));
        sum += abs(x);
    }

    return product * sum > INT_MAX ? -32768 : product * sum;
}