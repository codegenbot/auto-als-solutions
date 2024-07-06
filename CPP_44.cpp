```
#include <iostream>
using namespace std;

string change_base(int x, int base) {
    char res[1000];
    string s = "";
    size_t size = 0;
    while (x > 0) {
        int rem = x % base;
        char c = rem < 10 ? '0' + rem : rem > 9 ? 'A' + rem - 10 : '-';
        s.push_back(c);
        x /= base;
        size++;
    }
    return s.substr(0, size);
}

cout << "Enter a number: ";
int num;
cin >> num;

cout << "Enter the base: ";
int base;
cin >> base;

cout << "The conversion result is: " << change_base(num, base);