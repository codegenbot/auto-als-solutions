#include <stdio.h>
#include <iostream>

using namespace std;

int prime_fib(int n) {
    int a = 0, b = 1;
    for (int i = 2; ; i++) {
        int temp = a + b;
        if (temp > n)
            return temp;
        if (is_prime(temp)) {
            a = b;
            b = temp;
            if (b == n) return b;
        }
    }
}

bool is_prime(int num) {
    if (num <= 1) return false;
    for (int i = 2; i * i <= num; i++) {
        if (num % i == 0)
            return false;
    }
    return true;
}

int main() {
    int n;
    cout << "Enter a number: ";
    cin >> n;
    cout << "The " << n << "th prime Fibonacci number is: " << prime_fib(n) << endl;
    return 0;
}