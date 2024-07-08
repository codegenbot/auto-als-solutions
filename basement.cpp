int basement(const std::vector<int>& v) {
    int sum = v[0];
    for (int i = 1; i < v.size(); i++) {
        sum += v[i];
        if (sum < 0)
            return i + 1;
    }
    return -1;
}