#include <string>
#include <iostream> 
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
    int n, b;
    cout << "Enter a number: ";
    cin >> n;
    cout << "Enter the base: ";
    cin >> b;
    cout << "Base " << b << " representation of " << n << " is " << change_base(n, b);
    return 0;
}