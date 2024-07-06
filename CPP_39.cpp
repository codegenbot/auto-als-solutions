#include <iostream>

using namespace std;

bool isPrime(int num) {
    if (num <= 1)
        return false;
    for (int i = 2; i * i <= num; i++)
        if (num % i == 0)
            return false;
    return true;
}

int prime_fib(int n) {
    int a = 0, b = 1, fib = 0;
    for (int i = 0; ; i++) {
        if (i == n - 1)
            return a;
        fib = a + b;
        a = b;
        b = fib;
        while (!isPrime(fib))
            fib++;
    }
}