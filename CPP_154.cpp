#include <string>
using namespace std;

bool cycpattern_check(string a, string b) {
    int n = a.length(), m = b.length();
    for (int i = 0; i < n - m + 1; i++) {
        string substr = a.substr(i, m);
        if (substr == b || substr.rotate(1) == b ||
            substr.rotate(2) == b || substr.rotate(3) == b)
            return true;
    }
    return false;
}