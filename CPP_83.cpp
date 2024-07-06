int starts_one_ends(int n) {
    int count = 0;
    for (long long i = 1; i <= 9LL; i++) {
        if ((i == 1 || i % 10 == 1) && (n - 1 >= 1 && (i / pow(10, n - 1)) % 10 != 1))
            count++;
        for (long long j = 2; j <= 9LL; j++) {
            if ((i == 1 || i % 10 == 1) && (n - 1 >= 1 && (i / pow(10, n - 1)) % 10 != 1))
                count++;
        }
    }
    return count;
}
#include <cmath>