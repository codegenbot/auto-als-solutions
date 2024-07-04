#include <iostream>
#include <string>
#include <map>

using namespace std;

int main() {
    string cipher1, cipher2, message;
    cin >> cipher1 >> cipher2 >> message;

    map<char, char> cipher_map;
    for (size_t i = 0; i < cipher1.size(); ++i) {
        cipher_map[cipher1[i]] = cipher2[i];
    }

    string deciphered_message;
    for (char c : message) {
        deciphered_message += cipher_map[c];
    }

    cout << deciphered_message << endl;
    return 0;
}