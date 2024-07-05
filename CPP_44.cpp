#include <iostream>
#include <string>

using namespace std;

string change_base(int x, int base) {
    string res = "";
    while (x > 0) {
        int rem = x % base;
        if (rem <= 9) {
            res = to_string(rem) + res;
        } else {
            char c = 'A' + rem - 10;
            res = c + res;
        }
        x /= base;
    }
    return res;
}

int main() {
    int x, b;
    cout << "Enter a number: ";
    cin >> x;
    cout << "Enter the base (2-36): ";
    cin >> b;
    
    if(b < 2 || b > 36) {
        cout << "Invalid base";
    } else {
        string result = change_base(x, b);
        cout << "In base " << b << ": " << result << endl;
    }
    return 0;
}