Here is the completed code:

int fib4(int n) {
    if (n < 0) return -1; // Return error for negative input
    int fib4[5] = {0, 0, 2, 0, 0}; // Base cases
    for (int i = 5; i <= n; ++i) {
        int sum = fib4[i-1] + fib4[i-2] + fib4[i-3] + fib4[i-4];
        for (int j = 4; j > 0; --j)
            fib4[j] = fib4[j-1];
        fib4[0] = sum;
    }
    return fib4[n];
}