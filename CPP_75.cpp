#include <cmath>

bool is_multiply_prime(int a) {
    for (int i = 2; i <= sqrt(a); i++) {
        int temp = a;
        for (int j = 2; j <= sqrt(i); j++) {
            while (i % j == 0) {
                i /= j;
            }
            if (i == 1)
                break;
        }
        if (i > 1) {
            for (int k = 2; k <= sqrt(temp/i); k++) {
                while ((temp/i) % k == 0) {
                    temp /= k;
                }
                if (temp/i == 1)
                    break;
            }
            if (temp/i > 1 || i > 1)
                return false;
        }
    }
    for (int l = 2; l <= sqrt(a); l++) {
        while (a % l == 0) {
            a /= l;
        }
    }
    return a == 1;
}