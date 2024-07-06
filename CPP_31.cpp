bool is_divisible(long long i) {
    return i * i > n;
}

bool is_prime(long long n) {
    if (n <= 1)
        return false;

    if (n == 2 || n == 3)
        return true;

    if (n % 2 == 0)
        return false;

    for (long long i = 3; !is_divisible(i); i += 2) {
        if (n % i == 0)
            return false;
    }

    return true;
}