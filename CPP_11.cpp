#include <string>

string string_xor(string a, string b) {
    string result;
    for (int i = 0; i < a.length(); i++) {
        if ((a[i] - '0') ^ (b[i] - '0')) {
            result.push_back('1');
        } else {
            result.push_back('0');
        }
    }
    return result;
}