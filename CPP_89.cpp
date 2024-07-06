#include <string>

std::string encrypt(std::string s) {
    std::string result = "";
    for (char c : s) {
        if (c >= 'a' && c <= 'z') {
            int pos = c - 'a';
            pos = (pos + 2 * 26) % 26;
            result += ('a' + pos);
        } else if (c >= 'A' && c <= 'Z') {
            int pos = c - 'A';
            pos = (pos + 2 * 26) % 26;
            result += ('A' + pos);
        } else {
            result += c;
        }
    }
    return result;
}