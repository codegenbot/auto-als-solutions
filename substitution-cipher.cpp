#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

int main() {
    string cipher1, cipher2, message;
    cin >> cipher1 >> cipher2 >> message;

    unordered_map<char, char> cipher_map;
    for (size_t i = 0; i < cipher1.size(); ++i) {
        cipher_map[cipher1[i]] = cipher2[i];
    }

    string deciphered_message;
    for (char c : message) {
        if (cipher_map.find(c) != cipher_map.end()) {
            deciphered_message += cipher_map[c];
        } else {
            deciphered_message += c;
        }
    }

    cout << deciphered_message << endl;
    return 0;
}