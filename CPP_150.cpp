#include <cmath>
int x_or_y(int n, int x, int y) {
    bool isPrime = true;
    if (n <= 1) {
        return y;
    }
    for (double i = 2.0; i <= sqrt(n) && i * i <= n; i++) {
        if (n % i == 0) {
            isPrime = false;
            break;
        }
    }
    return isPrime ? x : y;
}