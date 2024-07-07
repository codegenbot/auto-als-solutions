Here is the completed code:

#include <vector>
#include <iostream>
#include <string>

using namespace std;

string camelCase(string s) {
    string result = "";
    for (char c : s) {
        if (c == '-') {
            result += c + ((result.length() > 0) ? "" : " ");
        } else {
            result += topperCase(c);
        }
    }
    return result;
}

string topperCase(char c) {
    return (c >= 'a' && c <= 'z') ? (char)(c - 32) : c;
}

int main() {
    string input;
    cout << "Enter a sentence in kebab-case: ";
    cin >> input;
    cout << "The result in camelCase is: " << camelCase(input) << endl;
    return 0;
}