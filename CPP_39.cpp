#include <vector>
#include <algorithm>

int prime_fib(int n) {
    int fib = 0;
    int a = 1;
    int b = 1;
    int count = 0;

    while (true) {
        if (b > n) break;
        if (is_prime(b)) {
            fib = b;
            count++;
            if (count == n) return b;
        }
        int temp = a + b;
        a = b;
        b = temp;
    }

    return 0; // or some other default value
}

bool is_prime(int num) {
    if (num <= 1) return false;
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0) return false;
    }
    return true;
}