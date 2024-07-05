#include <iostream>
#include <string>

using namespace std;

string change_base(int x, int base) {
    string res = "";
    while (x > 0) {
        int rem = x % base;
        if (rem < 10) {
            res = to_string(rem) + res;
        } else {
            res = (char)(65 + rem - 10) + res;
        }
        x /= base;
    }
    return res;
}

int main() {
    int num, base_num;
    cout << "Enter a number: ";
    cin >> num;
    cout << "Enter the base: ";
    cin >> base_num;
    cout << change_base(num, base_num);
    return 0;
}