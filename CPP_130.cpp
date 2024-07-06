vector<int> tri(int n) {
    vector<int> result(1, 3);
    if (n > 0) {
        for (int i = 1; i <= n - 2; i++) {
            int sum = 0;
            if (i % 2 == 0) {
                sum = 1 + i / 2;
            } else {
                sum = result[i-1] + result[i-2] + result[i+1];
            }
            result.push_back(sum);
        }
    }
    return result;
}