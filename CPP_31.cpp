bool is_one = (n == 1);
if (is_one) return false;

for (long long i = 2; i * i <= n; ++i) {
    bool is_divisor = (n % i == 0);
    if (is_divisor) return false;
}

return true;