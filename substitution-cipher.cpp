#include <vector>
#include <iostream>
#include <string>

std::string substitutionCipher(const std::string &cipherMap, const std::string &input) {
    std::string output;
    for (char c : input) {
        if (c >= 'a' && c <= 'z') {
            int index = c - 'a';
            if (index < cipherMap.size()) {
                c = cipherMap[index];
            }
        } else if (c >= 'A' && c <= 'Z') {
            int index = c - 'A';
            if (index < cipherMap.size()) {
                c = toupper(cipherMap[index] - 'a' + 'A');
            }
        }
        output += c;
    }
    return output;
}

int main() {
    std::string cipherMap, input;
    std::cout << "Enter the cipher map: ";
    std::cin >> cipherMap;
    std::cout << "Enter the message to decipher: ";
    std::cin >> input;
    std::cout << "Deciphered message: " << substitutionCipher(cipherMap, input) << std::endl;
    return 0;
}