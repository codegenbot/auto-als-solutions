```cpp
#include <iostream>

using namespace std;

int fib(int n) {
    if (n <= 1)
        return n;
    int a = 0, b = 1, result = 1;
    for (int i = 2; i <= n; i++) {
        result = a + b;
        a = b;
        b = result;
    }
    return result;
}

int main() 
{
    int n;
    cout << "Enter the value of n: ";
    cin >> n;
    cout << "The " << fib(n) << "-th Fibonacci number is: " << endl;
    return 0;
}