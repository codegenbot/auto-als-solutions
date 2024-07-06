int modp(int n, int p) {
    if (n < 0)
        return modp(-n, p);
    if (n == 0)
        return 1;
    long long res = 1;
    while (n > 0) {
        if (n % 2)
            res = (res * p) % p;
        p = (p * p) % p;
        n /= 2;
    }
    return res;
}