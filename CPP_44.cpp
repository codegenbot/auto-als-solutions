#include <string>
#include <stringstream>

string change_base(int x, int base) {
    string res = "";
    while (x > 0) {
        int rem = x % base;
        if (rem < 10) {
            res = to_string(rem) + res;
        } else {
            res = static_cast<char>(55 + rem - 10) + res;
        }
        x /= base;
    }
    return res;
}