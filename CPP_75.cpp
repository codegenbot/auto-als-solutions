#include <cmath>

bool is_multiply_prime(int a) {
    for (int i = 2; i <= sqrt(a); i++) {
        int counter = 0;
        for (int j = 2; j <= i / 2; j++) {
            if (i % j == 0) {
                counter++;
            }
        }
        if (counter == 0 && a % i == 0) {
            int b = a / i;
            int c = b / i;
            return isPrime(c);
        }
    }
    return false;
}

bool isPrime(int n) {
    if (n <= 1) {
        return false;
    }
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}