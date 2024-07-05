#include <stdio.h>

using namespace std;

int prime_fib(int n) {
    int a = 0, b = 1;
    for (int i = 1; ; i++) {
        if (i == n) return b;
        int temp = a + b;
        a = b;
        b = temp;
        while (b % 2 == 0) {
            b /= 2;
        }
        while (b % 3 == 0) {
            b /= 3;
        }
        while (b % 5 == 0) {
            b /= 5;
        }
        for (int j = 7; ; j++) {
            if (b % j == 0) break;
            if (j * j > b) return b;
            j += 2;
        }
    }
}