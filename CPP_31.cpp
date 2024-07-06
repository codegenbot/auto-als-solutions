#include <math.h>

using namespace std;

long long is_prime(long long n) {
    if (n <= 1)
        return -1;
    if (n == 2)
        return 2;
    for (long long i = 2; i * i <= n; i++) {
        if (n % i == 0)
            return -1;
    }
    return n;
}