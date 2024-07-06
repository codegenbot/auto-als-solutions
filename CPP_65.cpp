#include <string>

using namespace std;

string circular_shift(int x, int shift) {
    string s = to_string(x);
    int n = s.length();
    shift %= n;
    if (shift == 0) return s;
    return s.substr(shift) + s.substr(0, shift);
}