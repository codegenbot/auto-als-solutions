#include <cctype>
#include <string>

using namespace std;

string encode(string message) {
    string result = "";
    for (char c : message) {
        if (isalpha(c)) {
            char base = isupper(c) ? 'A' : 'a';
            c = ((c - base + 2) % 26) + base;
            if (c == ' ') {
                result += ' ';
            } else {
                result += c;
            }
        } else {
            result += c;
        }
    }
    return result;
}