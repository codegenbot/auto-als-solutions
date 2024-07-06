#include <cmath>

bool is_multiply_prime(int a) {
    for (int i = 2; i <= sqrt(a); i++) {
        int remainder = a % i;
        if (remainder == 0) {
            int count = 0;
            for (int j = 2; j * j <= i; j++) {
                if (i % j == 0) {
                    count++;
                    while (i % j == 0) {
                        i /= j;
                    }
                }
            }
            if (count > 1 && a / i <= 100) {
                for (int k = 2; k * k <= a / i; k++) {
                    int remainder2 = (a / i) % k;
                    if (remainder2 == 0) {
                        int count2 = 0;
                        for (int j = 2; j * j <= k; j++) {
                            if (k % j == 0) {
                                count2++;
                                while (k % j == 0) {
                                    k /= j;
                                }
                            }
                        }
                        if (count2 > 1 && a / i / k <= 100) {
                            for (int l = 2; l * l <= a / i / k; l++) {
                                int remainder3 = (a / i / k) % l;
                                if (remainder3 == 0) {
                                    int count3 = 0;
                                    for (int j = 2; j * j <= l; j++) {
                                        if (l % j == 0) {
                                            count3++;
                                            while (l % j == 0) {
                                                l /= j;
                                            }
                                        }
                                    }
                                    return count + count2 + count3 > 1;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    return false;
}