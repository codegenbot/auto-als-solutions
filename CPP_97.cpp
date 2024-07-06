#include <iostream>
using namespace std;

int multiply(int a, int b) {
    int unitA = a % 10;
    int unitB = b % 10;
    return (unitA * unitB);
}

int main() {
    assert(multiply(0, 0) == 0);
    
    int num1, num2;
    cout << "Enter the first number: ";
    cin >> num1;
    cout << "Enter the second number: ";
    cin >> num2;
    cout << "Product of " << num1 << " and " << num2 << " is: " << multiply(num1, num2);
    
    return 0;
}