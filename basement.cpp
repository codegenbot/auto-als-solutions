int basement(const std::vector<int>& v) {
    int sum = 0;
    for (int i = 0; i < v.size(); i++) {
        sum += v[i] - sum;
        if (sum < 0)
            return i + 1;
    }
    return -1;
}