int fib4(int n) {
    if (n < 0) return -1; // handle invalid input
    int a = 0, b = 2, c = 2, d = 0;
    for (int i = 4; i <= n; ++i) {
        int temp = a + b + c + d;
        d = c;
        c = b;
        b = a;
        a = temp;
    }
    return a;
}