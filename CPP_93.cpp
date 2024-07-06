#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

string encode(string message) {
    string result = "";
    for (char c : message) {
        if (isalpha(c)) {
            char baseChar = tolower(c);
            if (baseChar == 'a' || baseChar == 'e' || baseChar == 'i' || baseChar == 'o' || baseChar == 'u') {
                result += static_cast<char>(baseChar + 2);
            } else {
                result += (c == toupper(c)) ? tolower(c) : toupper(c);
            }
        } else {
            result += c;
        }
    }
    return result;
}

int main() {
    string message;
    cout << "Enter a message: ";
    getline(cin, message);
    cout << "Encoded message: " << encode(message) << endl;
    return 0;
}