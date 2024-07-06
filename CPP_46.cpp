int fib4(int n) {
    if (n < 0 || n > 4) return 0;
    int a = 0, b = 0, c = 2, d = 0;
    for (int i = 5; i <= n; ++i) {
        int temp = a + b + c + d;
        a = b;
        b = c;
        c = d;
        d = temp;
    }
    return d;
}