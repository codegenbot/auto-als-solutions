```cpp
#include <iostream>
#include <sstream>

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
    cin.ignore();
    string input;
    getline(cin, input);
    int n = stoi(input);
    cout << "The " << n << "-th Fibonacci number is: " << fib(n) << endl;
    return 0;
}