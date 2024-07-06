#include <math.h>

using namespace std;

int is_prime(long long n) {
    if (n <= 1)
        return 0;
    if (n == 2)
        return 1;
    for (long long i = 2; i * i <= n; i++) {
        if (n % i == 0)
            return 0;
    }
    return 1;
}