#include <iostream>
#include <string>

std::string encrypt(std::string s) {
    std::string result = "";
    for (char c : s) {
        if (c >= 'a' && c <= 'z') {
            int val = (int(c) - 97 + 3) % 26;
            result += (char)(val + 97);
        } else if (c >= 'A' && c <= 'Z') {
            int val = (int(c) - 65 + 3) % 26;
            result += (char)(val + 65);
        } else {
            result += c;
        }
    }
    return result;
}

int main() {
    assert(encrypt("a") == "d");
    return 0;
}