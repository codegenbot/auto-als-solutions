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
    int fibNum = 0, fibPrev = 0, fibCurr = 1;
    int count = 0;

    while (true) {
        fibCurr += fibPrev;
        fibPrev = fibCurr - fibPrev;
        if (isPrime(fibCurr)) {
            count++;
            if (count == n)
                return fibCurr;
        }
    }
}

int main() {
    cout << prime_fib(1) << endl; // 2
    cout << prime_fib(2) << endl; // 3
    cout << prime_fib(3) << endl; // 5
    cout << prime_fib(4) << endl; // 13
    cout << prime_fib(5) << endl; // 89

    return 0;
}