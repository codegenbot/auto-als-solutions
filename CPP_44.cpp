#include <iostream>
#include <string>

using namespace std;

string change_base(int x, int base) {
    string res = "";
    while (x > 0) {
        int rem = x % base;
        if (rem < 10) {
            res = to_string(rem) + res; // added parentheses for concatenation
        } else {
            res = char('A' + rem - 10) + res; // changed type of expression to 'char'
        }
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
    string result = change_base(num, base);
    cout << "The number in the new base is: " << result << endl;
    return 0;
}