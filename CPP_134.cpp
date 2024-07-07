```cpp
#include <iostream>
#include <string>
using namespace std;

bool check_if_last_char_is_a_letter(string txt) {
    if (txt.empty()) return false;
    string lastChar = txt.substr(txt.length() - 1);
    return isalpha(lastChar[0]) && !isalnum(lastChar[0]);
}

int main() {
    string text;
    cout << "Enter a string: ";
    cin >> text;

    if (check_if_last_char_is_a_letter(text)) {
        cout << "The last character of the entered string is a letter." << endl;
    } else {
        cout << "The last character of the entered string is not a letter." << endl;
    }

    return 0;
}