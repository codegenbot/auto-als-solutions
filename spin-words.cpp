#include <vector>
#include <iostream>
#include <string>

using namespace std;

string spinWords(string str) {
    string result = "";
    for (int i = 0; i < str.length(); i++) {
        if (str[i] == ' ') {
            result += " ";
        } else if (i >= str.length() - 5) {
            for (int j = i; j >= i - 4; j--) {
                result += str[j];
            }
            i -= 4;
        } else {
            result += str[i];
        }
    }
    return result;
}

int main() {
    string input;
    cout << "Enter a sentence: ";
    getline(cin, input);
    cout << spinWords(input) << endl;
    return 0;
}