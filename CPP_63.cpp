int fibfib(int n) {
    if (n <= 1)
        return 0;
    int prev = 0;
    int cur = 0;
    for (int i = 2; i <= n; ++i) {
        int temp = cur + prev + (cur > prev ? 0 : 1);
        prev = cur;
        cur = temp;
    }
    return cur;
}