int basement(vector<int>& v) {
    int sum = 0;
    for (int i = 0; i < v.size(); ) {
        sum += v[i];
        if (sum < 0)
            return i + 1;
        i++;
    }
    return -1;
}