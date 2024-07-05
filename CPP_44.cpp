```cpp
#include <bits/stdc++.h>
using namespace std;

string change_base(int x, int base) {
    string res = "";
    while (x > 0) {
        int rem = x % base;
        if (rem < 10) {
            res = to_string(rem) + res;
        } else {
            res = (rem < 10) ? to_string(rem) : string(1,"A") + res;
        }
        x /= base;
    }
    return res;
}

int main() {
    // your test cases here
}