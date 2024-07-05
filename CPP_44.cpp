#include <string>

std::string change_base(int x, int base) {
    if (x < base) {
        return std::to_string(x);
    }
    std::string res = "";
    while (x > 0) {
        res = std::to_string(x % base) + res;
        x /= base;
    }
    return res;
}