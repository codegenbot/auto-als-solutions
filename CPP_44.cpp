```
#include <iostream>
using namespace std;

string change_base(int x, int base) {
    char res[1000];
    string s = "";
    while (x > 0) {
        int rem = x % base;
        if(rem >= 10) res[--x] = (char)(rem - 55);
        else res[--x] = '0' + rem;
    }
    return string(res);
}

int main() {
    int num, base;
    cout << "Enter a number: ";
    cin >> num;
    cout << "Enter the base: ";
    cin >> base;
    cout << "The conversion result is: " << change_base(num, base);
}