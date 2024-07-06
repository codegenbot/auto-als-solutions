#include <cmath>

bool is_multiply_prime(int a) {
    for (int i = 2; i <= sqrt(a); i++) {
        int count = 0;
        for (int j = 2; j <= i / 2; j++) {
            if (i % j == 0)
                count++;
        }
        if (count == 0) {
            int b = a / i;
            int c = a % i;
            if (c != 0) continue;
            for (int k = 2; k <= sqrt(b); k++) {
                int tempCount = 0;
                for (int j = 2; j <= k / 2; j++) {
                    if (k % j == 0)
                        tempCount++;
                }
                if (tempCount == 0) {
                    int d = b / k;
                    int e = b % k;
                    if (e != 0) continue;
                    for (int j = 2; j <= sqrt(d); j++) {
                        int tempCount1 = 0;
                        for (int l = 2; l <= j / 2; l++) {
                            if (j % l == 0)
                                tempCount1++;
                        }
                        if (tempCount1 == 0) return true;
                    }
                }
            }
        }
    }
    return false;
}