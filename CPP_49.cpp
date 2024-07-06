#include <stdio.h>
using namespace std;

int modp(int n, int p) {
    if (p == 1)
        return n % p;
    else if (n < p)
        return n;
    else {
        n %= p;
        if (n == 0)
            return 0;
        else
            return modp(n * 2, p);
    }
}