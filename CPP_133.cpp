int sum_squares(const std::vector<float>& lst) {
    long long result = 0;
    for (float x : lst) {
        long long ceil_x = ceil(x);
        result += pow(ceil_x, 2);
    }
    return result;
}