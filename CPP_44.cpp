#include <iostream>
#include <string>
using namespace std;

string change_base(int x, int base) {
    string res = "";
    while (x > 0) {
        int rem = x % base;
        char c = rem < 10 ? '0' + rem : rem > 9 ? 'A' + rem - 10 : '-';
        res.push_back(c);
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