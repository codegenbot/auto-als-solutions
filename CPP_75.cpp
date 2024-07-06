bool is_multiply_prime(int a) {
    for (int i = 2; i <= 100; i++) {
        int count = 0;
        for (int j = 2; j <= i; j++) {
            if (i % j == 0) {
                count++;
            }
        }
        if (count == 1 && a % i == 0) {
            int b = a / i;
            int c = b / i;
            if (isPrime(c)) {
                return true;
            }
        }
    }
    return false;
}

bool isPrime(int n) {
    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}