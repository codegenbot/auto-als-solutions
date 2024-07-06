```
#include <iostream>
using namespace std;

string change_base(int x, int base) {
    string res = "";
    while (x > 0) {
        int rem = x % base;
        if(rem >= 10) res = char('A' + rem - 10) + res;
        else res = char('0' + rem) + res;
        x /= base;
    }
    return res;
}

int main() {
    int num, base;
    cout << "Enter a number: ";
    cin >> num;
    cout << "Enter the base: ";
    cin >> base;
    cout << "The conversion result is: " << change_base(num, base);
}