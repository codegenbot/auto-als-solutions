#include <vector>
#include <iostream>
#include <string>

std::string decipher(std::string cipher_text, std::string key) {
    string result = "";
    for (int i = 0; i < cipher_text.length(); i++) {
        if (i >= key.length()) {
            result += cipher_text[i];
        } else {
            result += key[i];
        }
    }
    return result;
}

int main() {
    std::string s1, s2, s3;
    std::cin >> s1 >> s2 >> s3;
    std::cout << decipher(s3, s1) << std::endl;
    return 0;
}