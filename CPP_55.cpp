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
    int n;
    cout << "Enter the value of n: ";
    cin >> n;
    ostringstream oss;
    oss << "The " << to_string(n) << "-th Fibonacci number is: " << fib(n);
    string output = oss.str();
    cout << output << endl;
    return 0;
}