#include <string>

std::string encrypt(std::string s) {
    std::string encrypted = "";
    for (char c : s) {
        if (isalpha(c)) {
            if (isupper(c))
                encrypted += (c + 3 <= 'Z') ? (char)(c + 3) : 'A' + ((c - 'A' + 3) % 26);
            else
                encrypted += (c + 3 <= 'z') ? (char)(c + 3) : 'a' + ((c - 'a' + 3) % 26);
        } else 
            encrypted += c;
    }
    return encrypted;
}