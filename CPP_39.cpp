#include <iostream>

using namespace std;

int prime_fib(int n) {
    int a = 0, b = 1, count = 0;
    while (count <= n) {
        if (isPrime(b)) {
            if (count == n)
                return b;
            count++;
        }
        int temp = a;
        a = b;
        b = temp + b;
    }
    return -1; // or throw an exception
}

bool isPrime(int num) {
    if (num <= 1)
        return false;
    for (int i = 2; i * i <= num; i++)
        if (num % i == 0)
            return false;
    return true;
}