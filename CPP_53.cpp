```cpp
#include <iostream>
using namespace std;

int main() {
    int x, y;
    cout << "Enter two numbers: ";
    cin >> x >> y;
    cout << "The sum is: " << add(x, y) << endl;
    return 0;
}

int add(int a, int b) {
    return a + b;
}