```cpp
#include <iostream>
#include <string>

using namespace std;

string change_base(int x, int base) {
    if (base <= 1) {
        return to_string(x);
    }
    string res = "";
    while (x > 0) {
        res = to_string(x % base) + res;
        x /= base;
    }
    return res;
}

int main() {
    int x;
    cout << "Enter a number: ";
    cin >> x;
    assert (change_base(x, x + 1) == to_string(x));
    return 0;
}