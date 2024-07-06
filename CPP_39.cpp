int prime_fib(int n) {
    int a = 0, b = 1, fib = 0;
    for (int i = 0; i < n; i++) {
        if (i == n - 2)
            return a;
        fib = a + b;
        a = b;
        b = fib;
        while (!isPrime(fib))
            fib++;
    }
}