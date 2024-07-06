bool is_multiply_prime(int a) {
    for (int i = 2; i <= 100; i++) {
        if (isPrime(i)) {
            int temp = a / i;
            for (int j = 2; j <= 100; j++) {
                if ((temp % j == 0) && isPrime(j)) {
                    int k = temp / j;
                    if ((k % i != 0) || (k < 2)) return true;
                }
            }
        }
    }
    return false;
}

bool isPrime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}