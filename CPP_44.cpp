#include <string>
#include <sstream>

string change_base(int x, int base) {
    string res = "";
    while (x > 0) {
        int rem = x % base;
        if (rem < 10) {
            res = to_string(rem) + res;
        } else {
            res = char('A' + rem - 10) + res;
        }
        x /= base;
    }
    return res;
}