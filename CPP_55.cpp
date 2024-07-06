#include <iostream>
using namespace std;

int fib(int n) {
    if (n <= 1)
        return n;
    int a = 0, b = 1, result = 1;
    for (int i = 2; i < n; i++) {
        a = b;
        b = a + b;
    }
    return b;
}

int main() 
{
    int n;
    cout << "Enter the value of n: ";
    cin >> n;
    cout << "The " << n << "-th Fibonacci number is: " << fib(n) << endl;
    return 0;
}