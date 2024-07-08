#include <string>
#include <iostream>
using namespace std;

#include <cctype>

string camelCase(string s) {
    string result = "";
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == '-') {
            i++; // skip the '-'
            while (i < s.size() && s[i] == ' ') {
                i++; // skip the spaces
            }
            if (result != "") {
                result += char(toupper(s[i])); // capitalize the first letter of each word
            } else {
                result = toupper(s[i]) + ""; // capitalize the first letter of the first word
            }
        } else if (s[i] == ' ') {
            continue; // skip the spaces
        } else {
            if (result != "") {
                result += char(tolower(s[i])); // add the rest of the letters in lowercase
            } else {
                result = tolower(s[i]) + ""; // add the first letter of the first word in lowercase
            }
        }
    }
    return result;
}

int main() {
    string s;
    while (true) {
        cout << "Enter a string: ";
        cin >> s;
        cout << "camelCase: " << camelCase(s) << endl;
    }
    return 0;
}