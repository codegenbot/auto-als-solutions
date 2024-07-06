#include <vector>

int starts_one_ends(int n) {
    int count = 0;
    for (long long i = 1; ; i *= 10) {
        if (i > n) break;
        count += 2;
        for (long long j = 0; ; j++) {
            long long num = i + j * (i != 1);
            if (num > n) break;
            if (num < 10 || num % 100 == 1 || num % 10 == 1) count++;
        }
    }
    return count;
}