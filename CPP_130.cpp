vector<int> tri(int n) {
    vector<int> result(n + 1);
    if (n >= 0) {
        result[0] = 3;
        if (n > 0) {
            if (n % 2 == 0) {
                result[1] = 1 + n / 2;
            } else {
                result[1] = 3;
            }
            for (int i = 2; i <= n; i++) {
                if (i % 2 == 0) {
                    result[i] = 1 + i / 2;
                } else {
                    result[i] = result[i - 1] + result[i - 2] + (i < n ? tri(i + 1)[n + 1 - i - 1] : 3);
                }
            }
        }
    }
    return result;
}