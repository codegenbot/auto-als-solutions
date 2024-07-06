#include <string>

std::string encrypt(std::string s) {
    std::string result = "";
    for (char c : s) {
        if (c >= 'a' && c <= 'z') {
            if ((c - 'a' + 3) % 26 < 0) {
                c += 26;
            }
            result += (c);
        } else {
            result += c;
        }
    }
    return result;
}