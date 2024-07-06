bool isPrime(int num) {
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0)
            return false;
    }
    return true;
}

int prime_fib(int n) {
    int a = 0, b = 1, fib = 0;
    for (int i = 0; i < n; i++) {
        if (i == n - 1)
            return b;
        fib = a + b;
        a = b;
        b = fib;
        while (!isPrime(fib))
            fib++;
    }
}