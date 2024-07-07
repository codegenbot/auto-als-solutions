#include <iostream>
#include <vector>
using namespace std;

int gcd(int a, int b) {
    if (b == 0)
        return a;
    else
        return gcd(b, a % b);
}

int main() {
    int a,b;
    cout << "Enter the value of a: ";
    cin >> a;
    cout << "Enter the value of b: ";
    cin >> b;
    
    cout << "GCD of " << a << " and " << b << " is " << gcd(a, b);
    
    return 0;
}