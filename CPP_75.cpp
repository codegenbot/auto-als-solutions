bool has_prime_factor(int n, int start, int end) {
    for (int i = start; i <= end; ++i) {
        if (n % i == 0) {
            return true;
        }
    }
    return false;
}

bool is_multiply_prime(int a) {
    bool found_prime_factors[3] = {false};

    int prime_factors[100] = {};
    int count = 0;

    for (int i = 2; i <= 100; ++i) {
        if (!has_prime_factor(i, 2, i)) continue;
        for (int j = i * i; j <= 100; j += i) {
            prime_factors[count++] = j;
        }
    }

    for (int i = 0; i < count; ++i) {
        for (int j = 0; j < count; ++j) {
            if (prime_factors[i] * prime_factors[j] > a) break;
            for (int k = 0; k < count; ++k) {
                if (prime_factors[i] * prime_factors[j] * prime_factors[k] == a) {
                    found_prime_factors[0] = true;
                    found_prime_factors[1] = i != j;
                    found_prime_factors[2] = k != i && k != j;
                    return true;
                }
            }
        }
    }

    return false;
}