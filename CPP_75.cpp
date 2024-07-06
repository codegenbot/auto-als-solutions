#include <vector>

bool is_multiply_prime(int a) {
    for (int i = 2; i <= 100; ++i) {
        for (int j = i; j <= 100; ++j) {
            for (int k = j; k <= 100; ++k) {
                if (i * j * k == a) {
                    vector<int> primes = {i, j, k};
                    bool is_prime = true;
                    for (int prime : primes) {
                        for (int p = 2; p * p <= prime; ++p) {
                            if (prime % p == 0) {
                                is_prime = false;
                                break;
                            }
                        }
                    }
                    return is_prime;
                }
            }
        }
    }
    return false;
}