#include <iostream>
#include <string>

using namespace std;

string flip_case(string str) {
    string result = "";
    for (char c : str) {
        if (islower(c)) {
            result += toupper(c);
        } else {
            result += tolower(c);
        }
    }
    return result;
}

int main() {
    string str;
    cout << "Enter a string: ";
    getline(cin, str);
    cout << "Flipped case: " << flip_case(str) << endl;
    return 0;
}