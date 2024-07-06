```cpp
#include<iostream>
using namespace std;

int main() {
    int x, y;
    cout << "Enter first number: ";
    cin >> x;
    cout << "Enter second number: ";
    cin >> y;
    cout << "Sum is : " << add(x,y);
}

int add(int x, int y) {
    return x + y;
}