#include <cmath>

bool is_multiply_prime(int a) {
    for (int i = 2; i <= sqrt(a); i++) {
        int temp = a;
        bool prime = true;
        for (int j = 2; j <= sqrt(i); j++) {
            if (i % j == 0) {
                prime = false;
                break;
            }
        }
        if (prime) {
            for (int k = i; temp > 1; k++) {
                if (temp % k == 0) {
                    int multiple = 1;
                    for (int l = 2; l <= sqrt(k); l++) {
                        if (k % l == 0) {
                            multiple++;
                            break;
                        }
                    }
                    if (multiple > 1) {
                        return true;
                    }
                    temp /= k;
                } else {
                    temp /= k;
                }
            }
        }
    }
    return false;
}