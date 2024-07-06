```cpp
#include <iostream>
using namespace std;

string change_base(int x, int base) {
    char res[1001];
    string s = "";
    size_t size = 0;
    while (x > 0) {
        int rem = x % base;
        char c = rem < 10 ? '0' + rem : rem > 9 ? 'A' + rem - 10 : '-';
        res[size++] = c;
        x /= base;
    }
    res[size] = '\0';
    return string(res);
}

int main() {
    int num, base;
    cout << "Enter a number: ";
    cin >> num;
    cout << "Enter the base: ";
    cin >> base;
    cout << "The conversion result is: " << change_base(num, base) << endl;
}