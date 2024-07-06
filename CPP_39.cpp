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
    int a = 0, b = 1, fibNum = 0;
    int count = 0;

    while (true) {
        fibNum = a + b;
        if (isPrime(fibNum)) {
            if (++count == n)
                return fibNum;
            a = b;
            b = fibNum;
        } else {
            a = b;
            b = fibNum;
        }
    }
}

int main() {
    int n;
    cout << "Enter the number: ";
    cin >> n;
    cout << "Prime Fibonacci number is: " << prime_fib(n) << endl;
    return 0;
}