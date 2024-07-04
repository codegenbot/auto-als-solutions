#include <iostream>
#include <string>

using namespace std;

int main() {
    string input;
    cin >> input;
    int len = input.length();
    if (len % 2 == 0) {
        cout << input.substr(len / 2 - 1, 2) << endl;
    } else {
        cout << input.substr(len / 2, 1) << endl;
    }
    return 0;
}