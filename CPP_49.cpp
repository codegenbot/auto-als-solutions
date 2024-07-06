int modp(int n, int p) {
    if(p == 0)
        return 0; // avoid undefined behavior for division by zero
    long long res = 1;
    while(n > 0) {
        if(n % 2 != 0)
            res = (res * p) % p;
        n /= 2;
        p = (p * p) % p;
    }
    return res;
}