#include <cmath>

int modp(int n, int p) {
    return pow(n, p) % p;
}