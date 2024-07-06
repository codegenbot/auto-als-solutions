int modp(int n, int p) {
    if (n < 0) return modp(-n, p);
    long long res = 1;
    for (int i = 0; i < __builtin_clz(n); i++) {
        if (!(n & 1)) {
            p = (long long)p * p % p;
        }
        n >>= 1;
    }
    while (n) {
        if (n & 1) res = (long long)res * p % p;
        n >>= 1;
        p = (long long)p * p % p;
    }
    return res;
}